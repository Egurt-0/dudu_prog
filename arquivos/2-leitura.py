"""
    Arquivos e modos de operacao


1-> Modo W - write  
2-> Modo A - append -  mas ele adiciona sempre no final
3-> Modo R - Read
4->
5->
6->

"""

# simplismente retorna oque esta escrito no arquivo, essa funcao le o arquivo exemplo1.txt e retorna oq ele leu
def ler_arquivo():
    with open("dados/exemplo1.txt", "r", encoding="utf-8") as file:
        print(file.read())


ler_arquivo()


def ler_arquivo_arrumado(): # outro exemplo similar, porem ele formata o retonro de cada linha, com "ola," antes do texto que tem na linha  
    with open("dados/exemplo1.txt", "r", encoding="utf-8") as file:
        for line in file:
            print(f"ola, {line.rstrip()}")

ler_arquivo_arrumado()
