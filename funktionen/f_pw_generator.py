import secrets

# Deklaration der Passwort Symobolliste
passwort_symbole = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                    "v", "w", "x", "y", "z", "!", "@", "#", "$", "%", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A",
                    "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
                    "W", "X", "Y", "Z", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "<", ">", ",",
                    ".", "?", "/", "|", "\\", "'", '"', "`", "~"]

max_laenge = 256

def f_pw_generator(passwort_laenge):
    """Die Funktion "pw_generator" erzeugt Passwörter bis zu einer max Länge von 256 Zeichen basierend auf
    einer vorab im Modul deklarierten Symbolliste.

    Args:
        passwort_laenge (Integer): Übergabewert der Passwortlänge

    Returns:
        String: Das fertig generierte Passwort
    """

    # Deklaration der Variable "passwort", als leer String
    passwort = ""

    while True:
        try:
            #passwort_laenge = int(input("Geben Sie die gewünschte Passwortlänge an (max. 256 Zeichen): "))
            # Kontrolle, ob die max. Länge nicht überschritten wurde
            if passwort_laenge >= max_laenge:
                print(f"\nIhre gewünschte Passwortlänge entspricht nicht der maximal zulässigen Passwortlänge von <<{max_laenge}>>")
            else:
                print(f"Ihr Passwort mit der einer Länge von <<{passwort_laenge}>> wird erstellt.")
                # Erstellen des Passwortes
                for i in range(passwort_laenge):
                    passwort += secrets.choice(passwort_symbole)
                break
        except ValueError as e:
            print(f"Bitte geben Sie eine eine Ganzzahl ein.\nFehlercode: {e}")

    return passwort