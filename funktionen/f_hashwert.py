import hashlib

def f_hashwert(hash_element = str, salt = None):
    """Die Funktion "haswert" erzeugt Hashwerte von Strings. Dies geschieht unter Berücksichtigung eines "Salts".
    Soll ein zufälliger "Salt" genutzt werden, so muss dieser extra Übergeben werden, ansonsten wird der
    Standard "Salt" genutzt. "b".encode() - konvertiert "b" in eine Bytefolge.

    Args:
        hash_element (String): Der String, von dem der Hashwert erstellt werden soll
        salt (Byte): Eine 16 Byte lange zufällige Sequenz. Defaults to None

    Returns:
        String: Der Hashwert im Hexadezimalen Format
    """

    if salt is None:
        salt = "b".encode()
        
    hashwert = hashlib.pbkdf2_hmac("sha256", hash_element.encode(), salt, 1000000)
        
    return hashwert.hex()