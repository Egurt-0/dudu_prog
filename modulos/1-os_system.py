import os


#************************************************
# ESSE MODULO E LIGADO AO SEU PC E SISTEMA
#************************************************


 
# 1 -  Retornar a pasta atual
print(os.getcwd())




# 2 - listas arquivos e pastas 
print(os.listdir())



# 3 - versao do Sistema operacional (SO)
os.system("ver")



# 4 - tras as configuracoes da maquina
os.system('systeminfo')



# 5 - limpar a tela do terminal
os.system('cls')



# 6 - desligar o PC
os.system('shutdown /s') # desliga o pc em 1 min
os.system('shutdown /a') # cancela o desligar de 1 min
os.system('shutdown /s /t 0') # desliga o pc imediatamente, sem chance irmao


# funcao para desligar o pc em uma hora
def turn_off_hour():
    os.system('shutdown /s /t 3600')# o /t define o tempo q vai demorar para desligar, e ele sempre tem que estar em segundos, nesse caso 3600 = 1h

# funcao para desligar em 30 min
def turn_off_half_hour():
    os.system('shutdown /s /t 1800')


# funcao para desligar o pc em 5 segudos
def turn_off_5s():
    os.system('shutdown /s /t 5')

def cancel_shutdown():
    os.system('shutdown /a')


