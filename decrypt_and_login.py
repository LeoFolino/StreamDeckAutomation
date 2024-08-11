from cryptography.fernet import Fernet
import pyautogui
import time
import sys

def load_key():
    # Carga la clave de cifrado desde el archivo "secret.key".
    return open("secret.key", "rb").read()

def decrypt_file(file_name):
    # Carga la clave de cifrado.
    key = load_key()
    # Crea un objeto Fernet con la clave cargada.
    fernet = Fernet(key)
    
    # Abre el archivo cifrado en modo de lectura binaria.
    with open(file_name, "rb") as file:
        encrypted_data = file.read()  # Lee el contenido cifrado del archivo.

    # Descifra los datos leídos usando la clave de cifrado.
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Devuelve el contenido descifrado como una cadena de texto (string).
    return decrypted_data.decode()

def get_credentials(service_name):
    # Descifra el archivo que contiene las credenciales.
    decrypted_data = decrypt_file("CRDT.txt.enc")
    # Divide el contenido del archivo descifrado en líneas.
    lines = decrypted_data.split('\n')
    # Busca la línea que comienza con el nombre del servicio solicitado.
    for line in lines:
        if line.startswith(service_name):
            # Si encuentra la línea, separa el usuario y la contraseña.
            _, creds = line.strip().split(': ')
            username, password = creds.split(', ')
            # Devuelve el usuario y la contraseña.
            return username, password
    # Si no encuentra el servicio, devuelve None.
    return None, None

def login(service_name):
    # Obtiene las credenciales para el servicio especificado.
    username, password = get_credentials(service_name)
    if username and password:
        # Simula la escritura del nombre de usuario.
        pyautogui.typewrite(username)
        pyautogui.press('tab')  # Presiona la tecla "Tab" para moverse al siguiente campo.
        # Simula la escritura de la contraseña.
        pyautogui.typewrite(password)
        pyautogui.press('enter')  # Presiona la tecla "Enter" para iniciar sesión.
    else:
        # Si no se encuentran credenciales para el servicio, imprime un mensaje.
        print(f"Credenciales para {service_name} no encontradas.")

if __name__ == "__main__":
    # Verifica que se haya pasado el nombre del servicio como argumento al ejecutar el script.
    if len(sys.argv) != 2:
        print("Uso: python decrypt_and_login.py <nombre_del_servicio>")
    else:
        service_name = sys.argv[1]  # Toma el nombre del servicio del argumento pasado.
        login(service_name)  # Intenta iniciar sesión usando las credenciales del servicio.
