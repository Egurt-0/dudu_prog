import tkinter as tk

#==============================
# modulo para interface grafica
#==============================

# 1 criando janela
window = tk.Tk()# Criando a janela
window.geometry("300x150") # dando o tamanho da janela
window.title("Frases") # Titulo da janela


# 2 - Adiciona um Frame
frame = tk.Frame(window)   # esta falando que o frame que voce criou esta dentro da janela(window)
frame.pack(padx=10, pady=10, fill="x", expand=True)


# 3 - ADICIONAR label
labell = tk.Label(frame, text="Ola, mundo")
labell.pack(fill='x', expand=True)

# 4 - Adicionando o input text 
frase_lab = tk.Label(frame, text="Frase")
frase_lab.pack(fill='x', expand=True)

frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True)

# 5 - funcao para alterar o texto do label
def click():
    labell.config(text=frase_inp.get())

# 6 - Adicionando botÃ£o
button = tk.Button(frame, text="Enviar", command=click)
button.pack()


window.mainloop() # isso sempre fica no final do codigo