cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        curso = {}
        curso["lenguage"] = linguagem
        curso["category"] = categoria
        cursos.append(curso)


def get_lenguage(cuourse):
    return cuourse["lenguage"]


def get_category(cuourse):
    return cuourse["category"]


print(cursos)
for curso in sorted(cursos, key=get_category): # ou voce pode mudar a key= para get_lenguage caso
    # voce queira ordenar por linguagem
    print(f"{curso['lenguage']}-{curso['category']}")