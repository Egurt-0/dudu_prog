import random


# 1 - selecionar valor aleatorio de uma lista
# coloca em um while True para ficar mais legal


numeros = [1,4,5,3,7,88,44,6,27]
print(random.choice(numeros))

# 2 - gera um numero aleatorio em um intervalo de valores

r1 = random.randint(1,100000)
print(r1)


# 3 - seleciona caracter aleatorio de uma string
name = "Curso de python com mais de 700 aulas, que doideira"
r2 = random.choice(name)
print(r2)

# 4 - seleciona mais de um valor aleatorio

# random.sample(variavel, tamanho)

print(random.sample(numeros, 5))
print(random.sample(name, 10))
s = "ola mundo"
print(random.sample(s, 2))



# 5 - Programa de sorterio
while True:
    print("oque voce deseja fazer?")
    print("1. adivinhar o numero")
    print("2. Sair do programa")

    choice = input(">")
    if choice == '1':
        print("=========Adivinhe o numero de 1 a 10=========")
        chute = int(input("seu Chute: "))
        number = random.randint(1,10)
        if chute == number:
            print("UAUU MEU QUEIRIDO, COISA BOA, VOCE ACERTOU")
        else:
            continue
    elif choice == "2":
        print("TMJ MLK, ATE")
        break
    else:
        print("opcao invalida, e facil man, escolhe 1 ou 2")

# no curso o cara fez diferente, mas eu gostei do jeito q eu fiz ent vou deixar, qualquer coisa vai na aula 38 no final dela ele monta esse mesmo joguinho de uma forma diferente