import sqlite3

class Datenbank:
    """Basisklasse für die Verwaltung von Datenbankoperationen"""
    def __init__(self, nutzername) -> None:
        """Initialisiert die Instanz der Klasse mit einem Nutzernamen"""
        self._nutzername = nutzername

    def db_connection_herstellen(self):
        """Stellt eine Verbindung zur SQLite-Datenbank her und speichert die Verbindung in self._connection"""
        try:
            self._connection = sqlite3.connect("data.db")
        except sqlite3.Error as e:
            print(f"Fehler beim herstellen einer Datenbankverbindung: {e}")
    
    def db_connection_schliessen(self):
        """Schließt die Verbindung zur SQLite-Datenbank"""
        self._connection.close()

    def db_cursor(self):
        """Gibt einen Cursor für die SQLite-Datenbank zurück"""
        self._cursor = self._connection.cursor()
        return  self._cursor

    def daten_speichern(self):
        """Gibt eine SQL-INSERT-Abfrage zurück, um Daten in die Tabelle des Nutzers zu speichern"""
        sql_query1 = f'''INSERT INTO {str(self._nutzername)} (Dienst, Salt, Nutzername, Passwort) VALUES (?, ?, ?, ?)'''
        return sql_query1
    
    def aenderung_commit(self):
        """Führt einen Commit für die SQLite-Datenbank aus"""
        self._connection.commit()


class DatenbankMaster(Datenbank):
    """Verwaltet das Datenbankbasierte Passwort-Management für einen bestimmten Nutzer und erbt von der Basisklasse: Datenbank"""
    def __init__(self, nutzername) -> None:
        """Initialisiert die Instanz der Klasse mit einem Nutzernamen"""
        super().__init__(nutzername)

    def tabelle_erstellen(self):
        """Erstellt eine Tabelle in der Datenbank mit dem Namen des Nutzers, wenn sie noch nicht existiert"""
        sql_query2 = f'''CREATE TABLE IF NOT EXISTS {str(self._nutzername)} (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Dienst TEXT,
            Salt BLOB,
            Nutzername TEXT,
            Passwort TEXT
        )'''
        return sql_query2
    
    def passwort_abrufen(self):
        """Gibt eine SQL-Abfrage zurück, die das Passwort & den Salt eines Nutzers aus der SQLite-Datenbank liest"""
        sql_query = f'''SELECT Passwort, Salt FROM {str(self._nutzername)} WHERE ID = 1'''
        return sql_query


class DatenbankDienst(Datenbank):
    """Verwaltet die Datenbankbasierten Dienst-Informationen für einen bestimmten Nutzer und erbt von der Basisklasse: Datenbank"""
    pass # In Progress
    """def alle_daten_abrufen(self):
        query = f"SELECT * FROM {str(self._nutzername)}"
        cursor = self.db_cursor()
        cursor.execute(query)
        return cursor.fetchall()"""
