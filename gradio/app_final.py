import gradio as gr

def converter_temperatura(temperatura, escala):
    if escala == "Celsius":
        return(temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9
    
def analisar_texto(texto):
    texto_limpo = texto.transalte(str.maketrans("","",string.punctuation))
    palavras = texto_limpo.split()
    num_palavras = len(palavras)
    num_caracteres = len(texto)

    frequencia = Counter(palavras)
    frequencia_hmtl = "<br>".join([f"{palavras}: {contagem}" for palavra, contagem in frequencia.items])

    return num_palavras, num_caracteres, frequencia_hmtl

def criar_relatorio(temperatura, escala, condicao, texto):
    temperatura_convertida = converter_temperatura(temperatura, escala)
    num_palavras, num_caracteres, frequencia = analisar_texto(texto)


    relatorio = (
        f"**Relatorio de Clima**\n\n"
        f"Temperatura: {temperatura_convertida:.2f}{'F' if escala=='Celsius' else 'C'}\n"
        f"Conidacao: {condicao}\n"
        f"descircao: {texto}\n\n"
        f"numero de palavras: {num_palavras}\n\n"
        f"numero de caracteres: {num_caracteres}"   
    )
