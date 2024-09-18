from klassen.clMasterAccount import *
from funktionen import f_pw_generator

class BenutzerschnittstelleKonsole:
    """Eine Klasse für die Benutzeroberfläche der Konsole. Diese bietet Methoden für die Anmeldung und das Hauptmenü.
    """
    def userinterface_login(self):
        """Diese Methode bietet die Möglichkeit sich einzuloggen oder einen neuen Account zu erstellen"""
        while True:
            try:
                input1 = input("Möchtest du dich einloggen, oder einen neuen Account erstellen? (1 = Einloggen | 2 = Neuer Account)\nEingabe: ")

                if int(input1) == 1:
                    input_nutzername = input("Nutzername: ")
                    input_passwort = input("Passwort: ")

                    login = LoginMasterAccount(input_nutzername, input_passwort)
                    if login.login_account() == True:
                        self.userinterface_hauptmenue()
                        break
                    else:
                        print("Das eingegebenene passwort ist nicht korrekt!")
                elif int(input1) == 2:
                    # TODO: Eine Überprüfungen erstellen, ob Leerzeichen enthalten sind
                    input_nutzername = input("Nutzername: ")
                    input_passwort = input("Passwort: ")

                    erstelle_master_account = ErstelleMasterAccount(input_nutzername, input_passwort)
                    erstelle_master_account.erstelle_account()
                    break
                else:
                    print(f"\nDu hast mit << {input1} >> eine ungültige Zahl eingegeben.\n")

            except ValueError as e:
                print(f"\nFehlercode: {e}\nDu hast mit << {input1} >> eine ungültige Eingabe getätigt.\n")

    def userinterface_hauptmenue(self):
        """"Diese Methode bietet die Möglichkeit, verschiedene Aktionen auszuführen,
        wie z.B. das Generieren eines Passworts oder das Anlegen eines neuen Dienstes."""
        while True:
            print("\nDu hast folgende Eingabeoptionen:")
            print(40 * "-")
            print(f"- {1:<5} = {"Passwort generieren" :>25}")
            # TODO: "Passwort generieren" auch bei Anlegung eines neuen eintrags anbieten
            print(f"- {2:<5} = {"Neuen Eintrag anlegen" :>25}")
            print(f"- {3:<5} = {"Eintrag anzeigen" :>25}")
            print(f"- {4:<5} = {"Eintrag bearbeiten" :>25}")
            print(f"- {5:<5} = {"Eintrag löschen" :>25}")
            print(f"- {6:<5} = {"Accountpasswort ändern" :>25}")
            print("\n")
            input2 = input("Eingabe:")

            # TODO: eine try/except Fehlerbehandlung hinzufügen

            if input2 == str(1):
                generiertes_passwort = f_pw_generator(int(input("Geben Sie die gewünschte Passwortlänge an (max. 256 Zeichen): ")))
                print(generiertes_passwort)
            else:
                print(f"<<{str(input2)}>> ist keine gültige Eingabe!")
