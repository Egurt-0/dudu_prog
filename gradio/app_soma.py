import gradio as gr


def somar(num1, num2):
    return num1 + num2


iface = gr.Interface(
    fn=somar,
    inputs=["number", "number"],
    outputs= "number",
    title= "calculadora de soma",
    description="Digite qualquer numero para somar",
    theme="default"
)

iface.launch()