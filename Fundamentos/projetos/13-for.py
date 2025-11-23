MovieList = ["Titanic","Homem aranha","The Batman"]
numeros = [10,30,40,50]
# 1 - iterando valores da lista. para cada ___ in MovieList
for  Movie in MovieList:
    print(Movie)

# 2 - quando a condicao e atendida o loop sera encerrado
for movie in MovieList:
    if movie == "Homem aranha":
        break
    print(movie)

# 3 - Quando  a condicao for atendida, o loop vai para proxima iteracao
for movie in MovieList:
    if movie == "Titanic":
        continue
    print(movie)


movieName =  input("digite o nome do filme:\n")
movieRating = int(input("quantas avaliacoes deseja fazer?:\n"))

total = 0 
for i in range(movieRating):
    note = float(input("nota do filme: "))
    total += note

if movieRating > 0:
    average = total/movieRating

else:
    average = 0 

print(f"A media das suas notas para o filme {movieName} foi de {average:.2f}")





















 # nao tem aver com o curso
 # testando o continue

import random

numero = random.randint(1,10000)

while True:
    chute = int(input("seu chute: "))
    if chute == numero:
        print("voce ganhou")
        break
    else:
        continue