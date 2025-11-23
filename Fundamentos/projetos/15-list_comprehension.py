for i in range(10):
    if i < 4:
        print( i )

# listando valores  de 0 a 10 que sejam menores do que 4 
ListNumbers = [i for i in range(11) if i < 11]
print(ListNumbers)


# filmes que possuem a letra a no titulo
MovieList = ["Titanic","Homem aranha","The Batman","He has rizz "]

filmes =[movie for  movie in MovieList if "a" in movie.lower()]
print(filmes)

 
# filmes que eu ja assiti, nesse caso eu nao assisti o The Batman                    eu na vdd ja assiti, isso foi um exemplo kkkkkkkkk

moviesWatched = [movie for movie in MovieList if movie != "The Batman"]
print(moviesWatched)


print((" Digite o nome do filme para ver se ta na lista ou nao, ou escreva sair para encerrar: "))
while True:
    searchName = input("nome do filme ou sair: ")
    if searchName.lower == "sair":
        print("Programa encerrado, flw man")
        break

    foundMovies = [movie for movie in MovieList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme(s) encotrado(s), seu nome: {searchName}:")
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print("GABO")

# se voce colocar espaco no input ele procura todos os filmes com nome composto