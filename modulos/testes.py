import math

def soma(a, b):
    print(f"Resultado: {a + b}")

def subtracao(a, b):
    print(f"Resultado: {a - b}")

def multiplicacao(a, b):
    print(f"Resultado: {a * b}")

def divisao(a, b):
    if b == 0:
        print("Erro: divisão por zero!")
    else:
        print(f"Resultado: {a / b}")

def potencia(a, b):
    print(f"Resultado: {math.pow(a, b)}")

def raiz_quadrada(a):
    if a < 0:
        print("Erro: não existe raiz quadrada de número negativo!")
    else:
        print(f"Resultado: {math.sqrt(a)}")

# ...continue para as outras funções seguindo esse padrão...

while True:
    print("="*20)
    print("Seja bem vindo à Calculadora do dudu")
    print("="*20)
    print("\nOperações disponíveis:")
    print(" +  soma")
    print(" -  subtração")
    print(" *  multiplicação")
    print(" /  divisão")
    print(" ^  potência")
    print(" sqrt  raiz quadrada")
    print(" sin  seno (ângulo em radianos)")
    print(" cos  cosseno (ângulo em radianos)")
    print(" log  logaritmo natural")
    print(" pi  número pi")
    print(" e  número de Euler")
    print(" mdc  máximo divisor comum")
    print(" digite 'sair' para encerrar")

    escolha = input("Escolha uma operação: ").lower()
    if escolha == "sair":
        break

    try:
        if escolha in ["+", "-", "*", "/", "^", "mdc"]:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        elif escolha in ["sqrt", "sin", "cos", "log", "fatorial"]:
            a = float(input("Digite o número: "))
        else:
            a = b = None
    except ValueError:
        print("Entrada inválida! Tente novamente.")
        continue

    # Chame a função correspondente aqui...