names = []




with open("dados/exemplo1.txt", "r", encoding="utf-8") as file:
    for line in file:
        names.append(line.rstrip)

for name in sorted(names, reverse=True):
    print(f"ola, {name}")


# seila, nao funciona direito, dudu do futuro, caso queira corrigir, ou pedir para alguem corrigir, fique a vontade, tmj mlk