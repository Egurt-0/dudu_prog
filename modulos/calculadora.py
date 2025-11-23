import math


infeite = "="
print(infeite*20)
print("Seja bem vindo a Calculadora do dudu")
print(infeite*20)


def soma():
    print("")
    print(f"Resultado: {num1 + num2}")

def Subtração():
    print("")
    print(f"Resultado: {num1 - num2}")

def Mutiplicação():
    print("")
    print(f"Resultado: {num1 * num2}")

def Divisão():
    print("")
    print(f"Resultado: {num1 / num2}")

def Potência():
    print("")
    print(f"Resultado: {math.pow(num1, num2)}")

def Raiza_quadrada():
    print("")
    print(f"Resultado: {math.sqrt(num1)}")
    print("")
    print(f"Resultado: {math.sqrt(num2)}")

def Seno():
    print("")
    print(f"Resultado: {math.sin(num1)}")
    print("")
    print(f"Resultado: {math.sin(num2)}")

def Cose():
    print("")
    print(f"Resultado: {math.cos(num1)}")
    print("")
    print(f"Resultado: {math.cos(num2)}")

def MDC():
    print("")
    print(f"Resultado: {math.gcd(num1, num2)}")

def log():
    print("")
    print(f"Resultado: {math.log(num1)}")
    print("")
    print(f"Resultado: {math.log(num2)}")



def pi():
    print("")
    print(f"Resultado: {math.pi}")

def E():
    print("")
    print(f"Resultado: {math.e}")

def fatorial():
    print("")
    print(f"Resultado: {math.factorial(num1)}")
    print("")
    print(f"Resultado: {math.factorial(num2)}")

while True:
    infeite = "="
    print("")
    print(infeite*20)
    print("Seja bem vindo a Calculadora do dudu")
    print(infeite*20)   
    print("\nOperaÃ§Ãµes disponÃ­veis:")
    print(" +  soma")
    print(" -  subtraÃ§Ã£o")
    print(" *  multiplicaÃ§Ã£o")
    print(" /  DivisÃ£o")
    print(" ^  PotÃªncia")
    print(" sqrt  Raiz quadrada")
    print(" sin  Seno (Ã¢ngulo em radianos)")
    print(" cos  Cosseno (Ã¢ngulo em radianos)")
    print(" log  Logaritmo base 10")
    print(" pi  Nuemero pi")
    print(" E  Nuemero de Euler")
    print(" MDC  Maximo divisor comum")
    print(" digite 'sair' para encerrar")

    num1 = float(input("Um numero: "))
    num2 = float(input("Digite outro nÃºmero: "))
    choice = input("Escolha uma operação(Digite seu simbolo): ")

    if choice == "+" or choice == "soma":
        soma()


    elif choice == "-" or choice == "subtraÃ§Ã£o":
        Subtração()


    elif choice == "*" or choice == "multiplicaÃ§Ã£o":
        Mutiplicação()


    elif choice == "/" or choice == "divisÃ£o":
        Divisão()


    elif choice == "^" or choice == "potÃªncia":
        Potência()


    elif choice == "sqrt" or choice == "raiz quadrada":
        Raiza_quadrada()


    elif choice == "sin" or choice == "seno":
        Seno()


    elif choice == "cos" or choice == "conseno":
        Cose()


    elif choice == "log" or choice == "logaritimo":
        log()


    elif choice == "pi" or choice == "PI" or choice == "Pi":
        pi()


    elif choice == "E" or choice == "Euler":
        E()


    elif choice == "MDC" or choice == "maximo divisor comum":
        MDC()

    elif choice == "Sair" or choice ==  "sair":
        break
    
    else:
        print("OpÃ§Ã£o invalida, tente colocar o nome ou simbolo da operaÃ§Ã£o")
