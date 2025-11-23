import gradio as gr

def processar_dados(texto, numero, imagem, lista_texto, cor, opcoes):
    texto_revertido = texto[::-1]
    dobro_numero = numero * 2
    texto_maiusculo = lista_texto.upper()
    mensagem_imagem ="A imagem foi recebida" if imagem is not None else "não tem essa coisa aqui não man"

    
    return(
        texto_revertido,
        dobro_numero,
        mensagem_imagem,
        texto_maiusculo,
        f"Cor selecionada: {cor}",
        opcoes
    )  

iface = gr.Interface(
    fn=processar_dados,
    inputs=[
        gr.Textbox(label="Texto", placeholder="Digite um texto aqui..."),
        gr.Slider(minimum=0, maximum=100, label="numero", value=0),
        gr.Image(type="pil", label="imagem"),
        gr.Textbox(label="lista de itens", lines=4, placeholder="item 1\nitem2"),
        gr.ColorPicker(label="selecione uma cor"),
        gr.CheckboxGroup(
            choices = ['Skibidi', 'Rizz', 'GYAT'],
            label="escolha uma das opcoes",
        )
    ],
    outputs=[
        gr.Textbox(label="texto revertido"),
        gr.Number(label="dobro do numero"),
        gr.Textbox(label="mensagem sobre a imagem"),
        gr.Textbox(label="Texto em maisculo"),
        gr.Textbox(label="cor selecionada"),
        gr.Textbox(label="opcoes selecionadas")
    ],
    title="verificardor de tipos de entrada e saida",
    description="insira um texto um numero, uma imagem, uma lista de itens, uma cor e uma opcao"
)

iface.launch()