cursos = []

with open("dados/cursos.csv", "r", encoding="utf-8") as file:
    for line in file:
        linguagem, categoria = line.rstrip().split(",")
        curso = {}
        curso["lenguage"] = linguagem
        curso["category"] = categoria
        cursos.append(curso)


print(cursos)

for curso in sorted(cursos, key=lambda course: course["category"]):
    # voce queira ordenar por linguagem
    print(f"{curso['lenguage']}-{curso['category']}")