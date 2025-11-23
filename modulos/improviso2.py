import hashlib


senha = input("Digite sua senha: ")
print("Senha registrada com sucesso!")



algoritim = hashlib.sha256()
senha_coode = senha.encode()
algoritim.update(senha_coode)
print(f"sua senha criptografada:    {algoritim.hexdigest()}")