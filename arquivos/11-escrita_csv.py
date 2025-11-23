import csv

linguagem = input("informe uma lingugem de programacao: ")
categoria = input("informe a categoria que a linguagem esta contida: ")


with open("dados/cursos.csv", "a", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\n")
    writer.writerow([linguagem, categoria])