import sqlite3
from klassen.clDatenbank import Datenbank, DatenbankMaster, DatenbankDienst
from funktionen import f_salt, f_hashwert

class MasterAccount:
    def __init__(self, nutzername, passwort) -> None:
        self._nutzername = nutzername
        self._passwort = passwort

    def erstelle_hashwert(self):
        self._nutzername_hash = f_hashwert(self._nutzername) # Die Zeile ist aktuell überflüssig
        if self._salt is None:
            self._salt = f_salt()
        self._passwort_hash = f_hashwert(self._passwort, self._salt)


class ErstelleMasterAccount(MasterAccount):
    def __init__(self, nutzername, passwort, salt = None, dienst = "Passwort_Manager") -> None:
        super().__init__(nutzername, passwort)
        self._salt = salt
        self._nutzername_hash = None
        self._passwort_hash = None
        self._dienst = dienst
    
    def erstelle_account(self):
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
    def __init__(self, nutzername, passwort, salt = None) -> None:
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