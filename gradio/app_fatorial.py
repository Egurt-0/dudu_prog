import gradio as gr
import math

def fatorial(num):
    if num < 0:
        print("deu nao man, nao da para fazer fatorial desse numero")
    else:
        return math.factorial(num)
    

iface = gr.Interface(
    fn=fatorial,
    inputs="number",
    outputs="number",
    title="Calculando fatorial",
    description="Calcule o fatorial de um numero",
)

iface.launch(True) # quando coloco o True, estou deixando esse link Publico
