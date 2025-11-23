import gradio as gr

def customizar_texto(texto, cor_fundo, cor_texto, tamanho_fonte, estilo_fonte):
    try:
        tamanho = int(tamanho_fonte)  # garante que é número
    except (TypeError, ValueError):
        tamanho = 20  # valor padrão se algo der errado

    estilo = (
        f"color: {cor_texto};"
        f"background-color: {cor_fundo};"
        f"font-size: {tamanho}px;"
        f"font-family: {estilo_fonte};"
    )

    return f'<div style="{estilo}">{texto}</div>'


iface = gr.Interface(
    fn=customizar_texto,
    inputs=[
        gr.Textbox(label="texto", placeholder="Digite seu texto aqui"),
        gr.ColorPicker(label="Cor de fundo"),
        gr.ColorPicker(label="Cor do texto"),
        gr.Slider(minimum=10, maximum=100, step=1, value=20, label="SEILA PORRA"),
        gr.Radio(
            choices=["Arial", "Courier New", "georgia", "Time new roman", "Verdana"],
            label="Estilo da fonte")
    ],
    outputs=gr.HTML(label="texto customizado"),
    title="customizador de interface",
    description="Customize essa interface como desejar",

)


iface.launch()
