import math

#****************************************************************
# ESSE MODULO SERVE PARA FAZER CONTAS MATEMATICAS MAIS FACILMENTE
#****************************************************************



# lemrando q voce nao pode ter o nome de um arquivo iguala um modulo,
# pq quando vc for importar ele vai dar erro, no caso desse arquivo tem um 2- na frente, entao nao é igual a o outro math_operations


# 1 - acessar o numero pi


print(math.pi)
print(f'{math.pi:.2f}')


# numero de Euler
print(math.e)
print(f'{math.e:.2f}')


# 3 - Arrendodar numeros para cima e para baixo
num = 10.14
print(math.ceil(num))
print(math.floor(num))



# 4 - fatorial de um numero
num2 = int(input("digite um numero: "))
print(math.factorial(num2))


 # 5 - potencia de numeros
print(math.pow(5, 5)) # o primeiro é a base e o segundo numero é o expoente


# 6 - raiz quadrada de um numero
print(math.sqrt(169))


# 7 - Maior divisor comum (MDC)
print(math.gcd(90, 1000))


# 8 logaritimo
print(math.log(10))