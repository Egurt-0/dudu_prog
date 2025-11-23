import gradio as gr

def converter_temperatura(temperatura, escala):
    if escala == "Celsius":
        return(temperatura * 9/5) + 32
    else:
        return (temperatura - 32) * 5/9
    

iface = gr.Interface(
    fn=converter_temperatura,
    inputs=[
        gr.Number(label="temperatura", precision=2),
        gr.Radio(
            choices=["Celsius", "fahrenhit"],
            label="Converte de "
        )
    ],
    outputs=gr.Number(label="Resultado"),
    title="Conversor de temperatura",
    description="de celsius para fahrenhit e viseversa"

)

iface.launch()