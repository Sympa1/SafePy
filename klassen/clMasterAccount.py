import sqlite3
from klassen.clDatenbank import Datenbank, DatenbankMaster, DatenbankDienst
from funktionen import f_salt, f_hashwert

class MasterAccount:
    """Basisklasse für die Verwaltung von Master-Accounts"""
    def __init__(self, nutzername, passwort) -> None:
        """Initialisiert die Instanz der Klasse mit einem Nutzernamen und Passwort"""
        self._nutzername = nutzername
        self._passwort = passwort

    def erstelle_hashwert(self):
        """Erstellt einen Hash-Wert für den Nutzernamen und Passwort"""
        self._nutzername_hash = f_hashwert(self._nutzername) # TODO: prüfen ob man die Zeile wirklich benötigt
        # Erstelle einen Salt-Wert, wenn keiner vorhanden ist
        if self._salt is None:
            self._salt = f_salt()
        # Erstelle einen Hash-Wert für das Passwort mit dem Salt-Wert
        self._passwort_hash = f_hashwert(self._passwort, self._salt)


class ErstelleMasterAccount(MasterAccount):
    """Klasse zur Erstellung eines Master-Accounts und erbt von der Basisklasse: MasterAccount"""
    def __init__(self, nutzername, passwort, salt = None, dienst = "Passwort_Manager") -> None:
        """Initialisiert die Instanz der Klasse mit einem Nutzernamen, Passwort, Salt-Wert, Dienst, sowie den Hashwerten"""
        super().__init__(nutzername, passwort)
        self._salt = salt
        self._nutzername_hash = None
        self._passwort_hash = None
        self._dienst = dienst
    
    def erstelle_account(self):
        """
        Erstellt einen neuen Account. Dieser Prozess umfasst folgende Schritte:
        
        1. Erstellt einen Hash-Wert für den Nutzernamen und Passwort, einschließlich des Salts.
        2. Erstellt eine Verbindung zur SQLite-Datenbank und erstellt einen Cursor.
        3. Erstellt die Tabelle in der Datenbank, wenn sie noch nicht existiert.
        4. Konvertiert den Salt-Wert in ein Binär-Format für die Datenbank.
        5. Trägt die Daten für die SQLite-Datenbank zusammen.
        6. Speichert die Daten in der Datenbank.
        7. Commit die Änderungen in der Datenbank.
        8. Schließt die Verbindung zur Datenbank.
        """
        self.erstelle_hashwert()

        datenbank = DatenbankMaster(self._nutzername)
        datenbank.db_connection_herstellen()
        datenbank_cursor =  datenbank.db_cursor()

        datenbank_cursor.execute(datenbank.tabelle_erstellen())
        datenbank.aenderung_commit()
        
        self._salt_blob = sqlite3.Binary(self._salt)
        sql_daten = (str(self._dienst), self._salt_blob, str(self._nutzername), str(self._passwort_hash))
        
        datenbank_cursor.execute(datenbank.daten_speichern(), sql_daten)

        datenbank.aenderung_commit()

        datenbank.db_connection_schliessen()


class LoginMasterAccount(MasterAccount):
    """Klasse zum Login des Master-accounts. Erbt von der Basisklasse: MasterAccount"""

    def __init__(self, nutzername, passwort, salt = None) -> None:
        """Initialisiert die Instanz der Klasse mit einem Nutzernamen, Passwort, Salt-Wert, sowie deren Hashwerten"""
        super().__init__(nutzername, passwort)
        self._salt = salt
        self._nutzername_hash = None
        self._passwort_hash = None

    def login_account(self):
        self.erstelle_hashwert()

        datenbank = DatenbankMaster(self._nutzername)
        datenbank.db_connection_herstellen()
        datenbank_cursor =  datenbank.db_cursor()
        
        datenbank_cursor.execute(datenbank.passwort_abrufen())
        rueckgabewerte = datenbank_cursor.fetchone()
 
        # TODO: Einfügen der Passwortüberprüfung