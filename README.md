# Linuxcli

A simple web application to demonstrate security practices and measures learned
in Module 183 at the college GIBB in Bern, Switzerland.

## Security measures

### Login/Register
Das login & register erfolgt erfolgt über ein http post request mit benutzername und passwort von index.html an die endpoint /login/ bzw. /register/ in views.py.

### Sessions
Mit der eingebaute django methode login(), wird ein session automatisch erstellt (views.py). Dies können mit der ausführen von logout() wieder gelöscht werden bzw. ausloggen.

### Systemkommandos
- ls (-la)
- pwd
- date (-u)
- lsblk (-lm)
- uname (-ap)
- cal (-my)

### Logging
Commands werden ausgedruckt mit python print() ins terminal

### Passwort sicherung
Wir nutzen die default django authentification um benutzer zu erstellen und persistent speichern in einer mysql datenbank. Django hashed und saltet der passowrt automatisch mit pbkdf2_sha256.

### SSL/TLS
Ist mit nginx gemacht.

### Brute-force/DOS
Wir nutzen das paket django-axes um brute force & DOS angriffen zu verhindern. axes erlaubt 3 login attempts. Nacher werden die ip auf ein blacklist gesetzt und die login funktionalität wird für die IP gesperrt.
