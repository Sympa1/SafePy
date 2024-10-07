from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from f_salt import f_salt

def f_erzeuge_schluessel(master_passwort):
    master_passwort = master_passwort.encode("utf-8")
    # erzeugt eine 16 Byte lange zufällige Sequenz
    salt = f_salt()
    # Schlüsselableitungsfunktion (Key Derivation Function - KDF)
    # Erstellen des instanziierten Objektes "kdf" der Klasse PBKDF2HMAC
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=300000)

    # Ableitung des Schlüssels mit der Klassenmethode "derive"
    abgeleiteter_schluessel = kdf.derive(master_passwort)

    return abgeleiteter_schluessel, salt