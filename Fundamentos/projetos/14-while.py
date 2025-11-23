
# AAATTEEEENNNCAAAOOOOO 
#    counter = 5
#    counter += 3  # This is the same as counter = counter + 3
#    print(counter)



MovieList = ["dudu","skibidi toilet","GYAT","Rizz"]


# Iterando valores de uma lista usando while
index = 0 
print(len(MovieList))
while index < len(MovieList):
    print(MovieList[index])
    index += 1 




# quando a condicao for atendida o loop sera encerrado

index = 0 
print(len(MovieList))
while index < len(MovieList):
    if MovieList[index] == "GYAT":
        break
    print(MovieList[index])
    index += 1 



# quando a condicao for atendida o loop vai para proxima iteracao


index = 0 
print(len(MovieList))
while index < len(MovieList):
    if MovieList[index] == "GYAT":
        index += 1 
        continue
    print(MovieList[index])
    index += 1 

# avaliacao do filme usando while

movieName =  input("digite o nome do filme:\n")
movieRating = int(input("quantas avaliacoes deseja fazer?:\n"))

total = 0 
count = 0 

while count < movieRating:
    note = float(input("digite uma nota para o filme\n"))
    total += note
    count += 1 

if movieRating > 0:
    average = total/movieRating
else:
    average = 0
print(f"A media das suas notas para o filme {movieName} foi de {average:.2f}")