#name = input("Digite o noem do filme:\n")
#yearRelease = int(input("Ano de lancamento do filme:\n"))
#rating  = float(input("digite a nota do filme:\n"))

#Condicoes para o filme
#if rating > 7.5 and yearRelease > 1970:
#    print(f"o filme {name} e muito show de bola")
#else:
#    print(f"o filme {name} nao e show de bola")



num1 = float(input("Digite um numero:\n"))
num2 = float(input("Digite outro numero:\n"))
operation = input("Digite a opercao a ser realizada: (+) ou (-) ou (*) ou (/)\n")

if operation == "+":
    resultado = num1 + num2
    print(resultado)

elif operation == "-":
    resultado = num1 - num2

elif operation == "*":
    resultado = num1 * num2

elif operation == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("nao da para dividir por 0 ne, pensa um pouco")
        resultado = 0
else:
    print("operacao invalida, tente novamente com os caracteres do enunciado")


print(resultado)