import gradio as gr

def reverter_string(texto):
    texto_revertido = texto[::-1]
    return texto_revertido, len(texto)

#print(reverter_string(f"DUDU, sigma da bahia"))


iface = gr.Interface(
    fn=reverter_string,
    inputs="text",
    outputs=["text", "number"],
    title="Escreva uma palavra e eu vou invertela",
    description="coloque sua palavra de tras para frente",

)

iface.launch()