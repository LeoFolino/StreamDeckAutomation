# StreanDeckAutomation **LOGIN**

En el documento se explica la instalación y uso.
---
Se debe descargar el .zip que tiene la siguiente distribución de carpetas

StreamDeckAutomation/
├── CRDTmuestra.txt
├── decrypt_and_login.exe
├── decrypt_and_login.py
├── encrypt_credentials.exe
├── encrypt_credentials.py
├── login_facebook.bat
├── login_google.bat
└── login_twitter.bat

- Se debe crear un archivo `CRDT.txt` con el formato expuesto en `CRDTmuestra.txt`, ahi es donde se van a escribir los servicios y el respectivo usuario y contraseña.
- Una vez creado, se debe ejecutar encrypt_credentials.exe el cual va a generar el archivo `secret.key` y `CRDT.txt.enc`. Proteger estos archivos ya que son las encriptaciones de las pass.
- `CRDT.txt` puede ser eliminado ya que el programa no usa este archivo mas alla de para generar un archivo encriptado con sus logins. Considerar que en caso de añadir otro login, se debe actualizar desde este `CRDT.txt`, en caso de borrarlo, debera generar uno nuevo.
- Se debe crear un archivo .bat para cada servicio y es el que se va a añadir como acceso rapido en StreamDeck.

*A continuacion se explica la creacion del .bat para cada servicio:*
```
@echo off
D:\StreamDeckAutomation\dist\decrypt_and_login.exe Google
```

@echo off se debe colocar siempre, debajo se encuentra la ruta del ejecutable que desencripta y realiza la ejecucion del logeo, y tiene que ir separado de un espacio y a continuacion el nombre del servicio como se define en el `CRDT.txt`, si añadimos el servicio **TikTok:** y su clave, TikTok es el nombre del servicio que debe ir acompañado de la ruta, considerar que la ruta **depende siempre de donde vayas a descomprimir el .zip**.
