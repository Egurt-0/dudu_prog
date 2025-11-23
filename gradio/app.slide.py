import gradio as gr
import numpy as np
from PIL import Image 
import io
import base64


def criar_slide(titulo, texto, imagem, cor_fundo, cor_texto):
    estilo = (
        f"background-color: {cor_fundo}; !important; " # esse importante faz com que ele de priroridade a esse elementos, e evita que algum CSS do gradio sobreescreva os elementos
        f"color: {cor_texto}; !important; "
        "padding: 20px; "
        "text-align: center; " 
    )  

    # converta a imgagem para base 64 se estiver presente
    imagem_html = ""
    if imagem is not None:
        buffered = io.BytesIO()
        img_pil = Image.fromarray(np.uint8(imagem))
        img_pil.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        imagem_html =(f"<img src='data:image/png;base64,{img_str}' style='max-width: 100%; height: auto;'>"
        )
    
    slide_hmtl = f"""
        <div style="{estilo}">
            <h1>{titulo}</h1>
            <p>{texto}</p>
            {imagem_html}      
        </div
    """


    return slide_hmtl

iface = gr.Interface(
    fn=criar_slide,
    inputs=[
        gr.Textbox(label="Titulo do slide", placeholder="Digite o titulo"),
        gr.Textbox(label="Texto do slide", placeholder="Digite o Texto"),
        gr.Image(type="numpy", label="imagem do slide"),
        gr.ColorPicker(label="Cor do fundo"),
        gr.ColorPicker(label="Cor do texto"),
  ],
  outputs=gr.HTML(label="slide customizado"),
  title="craidor de slide",
  description="crie seu slide ai",
)


iface.launch()