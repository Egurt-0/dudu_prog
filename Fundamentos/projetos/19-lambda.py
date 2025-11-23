# funcao de potencia de um numero
power = lambda num: num**2


# funcao que verifica se um numero e par
is_even = lambda x: x % 2 == 0 


# funcao que divide um numero por outro
div_num = lambda x,y: x / y

# funcao que inverte uma string
reverse = lambda s: s[::-1]

print(power(5))
print(power(4921))
print(is_even(27))
print(is_even(2988))
print(div_num(7,7))
print(div_num(8,4))
print(reverse("comedor de pao"))
print(reverse("cuscuz"))

# funcionalidades relacionadas a filmes:
movie_lista = ["DUDUU","Titanic","eversonzoio","labubu e a volta dos bob goodies","The matrix"]
ratings = {
    "Titanic":[8.5, 9.0, 8,0],
    "DUDUU":[10.0, 10.0, 10.0],
    "eversonzoio":[9.0, 7.6, 6.0],
    "labubu e a volta dos bob goodies":[10.0, 10.0, 9.0],
    "The matrix":[8.0, 7.6, 8.4],

}

# funcao para calcular a media do filme
    
average = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name  ])
print(f"meida de avaliacao do filme de matrix: {average("The matrix")}")

# verifica se o filme esta na lista
check = lambda movie_name: movie_name in movie_lista

print(f"meida de avaliacao do filme de matrix: {average("The matrix")}")
print(f"labubu e a volta dos bob goodies esta na lista?: {check("labubu e a volta dos bob ggoodies")}")       