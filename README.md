# Linuxcli

A simple web application to demonstrate security practices and measures learned
in Module 183 at the college GIBB in Bern, Switzerland.

## Security measures

### Login/Register
Das Login & Registriereb erfolgt über eine HTTP-POST Abfrage mit Benutzername und Passwort von index.html an den Endpunkt /login/ bzw. /register/ in views.py.

### Sessions
Mit der eingebaute Django Methode login(), wird ein Session automatisch erstellt (views.py). Diese kann mit logout() wieder gelöscht werden bzw. der Benutzer wird ausgeloggt.

### Systemkommandos
* ls (-la)
* pwd
* date (-u)
* lsblk (-lm)
* uname (-ap)
* cal (-my)

Die Systemkommandos werden im Django konfiguriert. Dort können Kommand, eine Beschreibüng sowie die Parameter der Kommands definiert werde. Sobald der Benutzer dann eine Abfrage auf den Endpunkt /command/ls (Beispiel) macht, wird veirfiziert ob das Kommando konfiguriert ist und ob alle Parameter ebenfalss im Django enthalten sind. Falls nicht wird das Kommando nicht ausgeführt oder die Parameter werden nicht angefügt.

### Logging
Jedes mal wenn ein Kommando ausgeführt wird, wird der Befehl in fogendem Format ins STDOUT gelogged: `['ls', '-a', '-l']`.

### Passwort sicherung
Wir nutzen die default Django Authentifikation um Benutzer zu erstellen und persisten in einer MySQL zu speichern. Django hashed und saltet das Passwort automatisch mit pbkdf2-sha256.

### SSL/TLS
Wir haben einen NGINX Server der die TLS / HTTPS Verbindung übernimmt. Dort haben wir ein selbst signiertes Zertifikat.

### Brute-force/DOS
Wir nutzen das Paket django-axes um Brute-Force Angriffe zu verhindern. axes erlaubt 3 login Versuche. Nacher werden die ip auf ein blacklist gesetzt und die login funktionalität wird für die IP gesperrt.
Um DoS Attacken vorzubeugen, limitieren wir den NGINX Server auf maximal 30 Anfragen pro Minute.

### Register
Ein Benutzer kann sicher via HTTPS erstellt werden.
