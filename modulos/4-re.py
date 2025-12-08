import re

#*********************************************************************************************
#permite buscar, manipular e extrair padrões complexos de texto de forma poderosa e flexível,
#como encontrar todos os emails, números de telefone ou validar formatos                               #
# ********************************************************************************************



text = "Udemy - uma plataforma com muitos cursos"
# 1 - indice inicial e final de palavras
# o r significa um raw string(string bruta)
match = re.search(r'uma plataforma',text)
print(f"indice inicial: {match.start()}")
print(f"indice final: {match.end()}")


# 2 - buscando o indice que possiu o ponto
site = "https://udemy.com"
match = re.search(r'\.',site)
print(match)

# 3 - uma lista de caracteres dentro de uma frase
pattern = r"[aeriou]" # todas as vogais
result = re.findall(pattern, text)
print(result)

# 4 - verificando o inicio de uma string
rule = r'^A'
phrases = ['A casa esta suja',' voce esta linda','vamos passear']
for f in phrases:
    if re.match(rule, f):
        print(f"corresponde: {f}")
    else:
        print(f"nao corresponde: {f}")

# 5 - verificando o sinal de uma string
rule_end = r'!$'
phrase2 = "O dia esta lindo"
match = re.search(rule_end, phrase2)
if match:
    print("sim,corresponde")
else:
    print("Nao corresponde") 