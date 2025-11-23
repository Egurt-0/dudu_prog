
# funcao para imprir uma mensagem

# quantas_vezes = int(input("quantas vezes?: "))
# def welcome():
#     print(""""
#           UAAAUUUU VOCE CHEGOU
#           seja bem vindo meu nobre, aqui e o escritorio
#           virtual do seu grande amigo dudu, fique a von
#           tade, pois o unico limite aqui, e seu conhecimento
#           de python
#           """)
    
# for i in range(quantas_vezes):
#     welcome()

# funcao para calcular a media de notas

def average():
    numero_AV = int(input("quantas avaliacoes voce deseja fazer para o filme?: "))
    total = 0 
    for i in range(numero_AV):
        note = float(input("sua nota para o filme: "))
        total += note

    if numero_AV > 0:
        average = total / numero_AV
    else:
        average = 0 

    return average

print(f"a media das suas avaliacoes:{average():.2f}")