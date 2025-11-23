with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linha = line.rstrip().split(",") # isso faz com que ele separe as linhas e separe os item por um virgula
        print(linha[1]) # essa lista ali, eu posso colocar 0 ou 1, isso representa o Ã­ndice, ou seja,
        # se colocar 0 ele vai pegar os valores antes da virgula do arquivo csv, e se colocar 1
        # ele vai pegar os valores depois da virgula


        linguagem, categoria = line.rstrip().split(",")
        print(f" {linguagem} ->{categoria} ")
         