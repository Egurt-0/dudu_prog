import os
from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipher_suite = Fernet(key)
print(f"Chave gerada: {key.decode()}")
cipher = Fernet(key)
mensagem = input("Digite a mensagem que deseja criptografar: ")
mensagem_bytes = mensagem.encode()
cipher_text = cipher.encrypt(mensagem_bytes)
print(f"Mensagem criptografada: {cipher_text.decode()}")

