import os 
def f_salt():
    """
    Die Funktion "salt" erstellt eine 16 Byte (128 Bit) lange zufällige Sequenz, welche als Salt
    beim erstellen eines Hashwerts verwendet wird.

    Returns:
        salt
    """
    salt = os.urandom(16)
    return salt