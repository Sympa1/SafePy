import hashlib

def f_hashwert(hash_element = str, salt = None):
    """Diese Funktion erzeugt Hashwerte von Strings. Dies unter Berücksichtigung eines "Salts". Soll ein zufälliger "Salt" genutzt werden,
    so muss dieser extra Übergeben werden, ansonsten wird der Standard "Salt" genutzt. "b".encode() - konvertiert "b" in eine Bytefolge.

    Keyword Arguments:
        hash_element {String},
        salt {None}

    Returns:
        hashwert {Hexadezimal}
    """
    if salt is None:
        salt = "b".encode()
        
    hashwert = hashlib.pbkdf2_hmac("sha256", hash_element.encode(), salt, 1000000)
        
    return hashwert.hex()