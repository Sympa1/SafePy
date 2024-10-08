# SafePy
Ein einfacher Passwort-Manager in Python, der Passwörter verschlüsselt und sicher speichert.
___
## Python Passwort-Manager - SafePy 

Dieser Passwort-Manager wurde vollständig in Python entwickelt und bietet eine sichere Möglichkeit, Passwörter zu generieren,
zu speichern und zu verwalten. Im Folgenden werden einige der wichtigsten Entscheidungen und Funktionen des Programms erläutert:

### 1. Verwendung von secrets statt random

Anstelle des Moduls random verwende ich das Python-Modul secrets, da es speziell für kryptografisch sichere Zufallszahlen
entwickelt wurde. Im Gegensatz zu random, das den Zufall nur simuliert, berücksichtigt secrets echte physikalische Phänomene
wie das Rauschen von elektrischen Bauteilen, was den "Zufallsfaktor" signifikant erhöht. Dadurch wird die Sicherheit der
generierten Passwörter stark verbessert.

### 2. Hashverfahren: hashlib

Für das Hashing der Passwörter verwende ich das Python-Modul hashlib, welches eine Vielzahl von sicheren Hashfunktionen bereitstellt.
Insbesondere nutze ich SHA-256, da es ein starkes und weit verbreitetes kryptografisches Hashverfahren ist, das ausreichenden
Schutz vor Brute-Force-Angriffen bietet.
Die Verwendung von hashlib bietet Flexibilität und eine zuverlässige Lösung für die sichere Speicherung von Passwörtern.

### 3. Speicherung von Login-Daten für den Passwort-Manager

Der Nutzername und das Masterpasswort werden in der ersten Zeile der jeweiligen Datenbanktabelle gespeichert. Die Tabelle
selbst trägt den Namen des Nutzernamens.
Mithilfe des Moduls hashlib und einem 16-Bit langen Salt wird der Hashwert des Masterpassworts im Hexadezimalformat in der
Datenbank abgelegt. Der Salt wird zusätzlich separat gespeichert. Das hinzufügen des "Salts" soll die sicherheit erhöhen.

Die Speicherung im Hexadezimalformat hat den Vorteil, dass es weniger Speicherplatz beansprucht und die Verarbeitung effizienter
gestaltet. Der Salt wird jedoch im Binärformat gespeichert, da dies die Arbeit mit dem Salt vereinfacht und die Integration
in die Hashing-Prozesse optimiert.

### 4. Problem bei der Accounterstellung / Standard-Login

Während der Entwicklung gab es ein Problem bei der Erstellung der Datenbanktabellen. Mein Ziel war es, die Tabellennamen
anhand des Hashwerts des Benutzernamens im Hexadezimalformat zu generieren, um zusätzliche Sicherheit zu gewährleisten.
Leider konnte ich keine Möglichkeit finden, den Hashwert als Tabellennamen zu verwenden – es funktionierte nur mit dem
"Klarnamen" des Nutzers.
Standard-Login:

Nutzername: HansDampf
Passwort: Milchstraße123

### 5. Inpelmentierung einer simplen Login-Funktion

Eine simple Login-Funktion  wurde implementiert, das Passwort des Nutzers überprüft. Jedoch aktuell nicht den Nutzernamen. 
Hierzu werden die Haswerte des eingegeben Passwortes und die des gespeicherten Passwortes verglichen.

### 6. Hinzufügen der Funktion um den Symmetrischer Schlüssel von dem Master Passwort abzuleiten

Der symmetrischer Schlüssel wird von dem jeweiligen Master Passwort abegeleitet und erstellt.
Hierzu wird das optionale Python Modul "cryptography" genutzt. 
Um Rainbowtable Angriffe zu erschweren wird wieder ein Salt (eine 16 Byte lange zufällige Sequenz) und wird ebenfalls abgespeichert.
Es wird zur Erstellung die SHA 256 Hash Funktion genutzt um einen 256 Bit langen Schlüssel zu erzeugen.