import os
import random
import hashlib

# ESSE E MEU PROGRAMA
# EU JUNTEI O IMPROVISO 2 E COLOQUEI NO 1
infeite = "="
print(infeite*15)
print("seja bem vindo ao gerenciador de sistema")
print(infeite*15)

while True:
    print("1 - Desligar o PC em:")
    print("2 - Desligar o PC em quantidade de tempo randomica ")
    print("3 - Ver configuracoes da sua maquina")
    print("4 - Versao do seu sistema operacional")
    print("5 - Lista de arquivos e pastas")
    print("6 - Criptografar uma senha")
    print("7 - Sair do gerenciador de sistema")
    escolha = int(input("Quero a opcao: "))

    if escolha == 1:
       tempo = int(input("Digite um tempo em que seu pc vai ser desligado(em segundos): "))
       os.system(f'shutdown /s /t {tempo}')
    elif escolha == 2:
        os.system(f'shutdown /s /t {random.randint(1, 1000)}')
    elif escolha == 3:
        os.system('systeminfo')
    elif escolha == 4:
        os.system("ver")
    elif escolha == 5:
        print(os.listdir())
    elif escolha == 7:
        break
    elif escolha == 6:
        senha = input("Digite sua senha: ")
        print("Senha registrada com sucesso!")
        algoritim = hashlib.sha256()
        senha_coode = senha.encode()
        algoritim.update(senha_coode)
        print(f"sua senha criptografada:    {algoritim.hexdigest()}")
        print("")
    else:
        print("Opcao invalida,tente novamente") 
