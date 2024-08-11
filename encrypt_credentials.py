from cryptography.fernet import Fernet

def generate_key():
    # Genera una clave de cifrado usando Fernet (que es un sistema de cifrado simétrico).
    key = Fernet.generate_key()
    # Guarda la clave generada en un archivo llamado "secret.key".
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Carga la clave de cifrado desde el archivo "secret.key".
    return open("secret.key", "rb").read()

def encrypt_file(file_name):
    # Carga la clave de cifrado.
    key = load_key()
    # Crea un objeto Fernet con la clave cargada.
    fernet = Fernet(key)
    
    # Abre el archivo que se desea cifrar en modo de lectura binaria.
    with open(file_name, "rb") as file:
        file_data = file.read()  # Lee el contenido del archivo.

    # Cifra el contenido del archivo usando la clave.
    encrypted_data = fernet.encrypt(file_data)
    
    # Guarda los datos cifrados en un nuevo archivo con la extensión ".enc".
    with open(f"{file_name}.enc", "wb") as file:
        file.write(encrypted_data)

if __name__ == "__main__":
    generate_key()  # Genera y guarda una nueva clave de cifrado.
    encrypt_file("CRDT.txt")  # Cifra el archivo CRDT.txt y guarda el resultado en CRDT.txt.enc.
