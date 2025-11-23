import os

senha = "Egurt"


while True: 
    chute = input("Digite a senha: ")


    if chute == senha:    
        print("Seu bobao")
        os.system('shutdown /s /t 0')
    else:
        print("Errou, tente novamente\n")
