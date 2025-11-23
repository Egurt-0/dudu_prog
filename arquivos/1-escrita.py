nome = input("Digite um nome para o aluno:\n")

"""
    Arquivos e modos de operacao


1-> Modo W - write  
2-> Modo A - append -  mas ele adiciona sempre no final
3-> Modo R - Read
4->
5->
6->

"""

# 1 implementacione substitui oque esta escrito no arquivo txt
file = open("dados/names.txt","w") # esse tem o "w" de write  ----- esse exemplo, por nao ter o encoding="uft-8" nao reconhece ascentos, tipo fábrica ou hélio, ã~~~ seila
file.write(f"{nome}\n")# esse exemplo esta relacionado ao arquivo nomes
file.close


# 2 implementacione adiciona o nome no arquivo txt

file = open("dados/exemplo1.txt","a", encoding="utf-8") # esse tem o "a" de append  ------ esse por ter o encoding="utf-8" reconhce e aceita ascentos
file.write(f"{nome}\n") # este exemplo esta relacionado ao arquivo exemplo1
file.close




# 3 implementacione
with open("dados/exemplo1.txt", "a", encoding="utf-8") as file:
    file.writer(f"{nome}\n")
