from tkinter import *
import tkinter.messagebox

cor0 = "#444466"  # Preta
cor1 = "#feffff"  # branca
cor2 = "#004338"

janela = Tk()
janela.title("Color Picker")
janela.geometry("530x205")
janela.resizable(width=False, height=False)
janela.config(bg=cor1)



tela = Label(janela, bg='black', width=40, height=10, bd=1)
tela.grid(row=0, column=0)

frame_direita = Frame(janela, bg=cor1)
frame_direita.grid(row=0, column=1)

frame_baixo = Frame(janela, bg=cor1)
frame_baixo.grid(row=1, column=0,pady=15, columnspan=2)


def escala(valor):
    r=s_red.get()
    g=s_green.get()
    b=s_blue.get()

    e_cor.config(state="normal")
    hexadecimal = "#%02x%02x%02x" % (r,g,b)
    tela.config(bg=hexadecimal)
    e_cor.delete(0,END)
    e_cor.insert(0,hexadecimal)
    e_cor.config(state="readonly")

def clicar():
    tkinter.messagebox.showinfo("Color Picker", "A código foi copiado.")
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(e_cor.get())
    clip.destroy()


l_red = Label(frame_direita, text='Red', width=7, bg=cor1, fg='Red', anchor='nw', font=("Time New Roman", 12, "bold"))
l_red.grid(row=0, column=0)
l_red.place(x=0,y=8)
s_red=Scale(frame_direita, from_=0,command=escala, to=255, length=150, bg=cor1, fg="red", orient=HORIZONTAL)
s_red.grid(row=0, column=1)

l_green = Label(frame_direita, text='Green', width=7, bg=cor1, fg='Green', anchor='nw', font=("Time New Roman", 12, "bold"))
l_green.grid(row=1, column=0)
l_green.place(x=0,y=48)
s_green=Scale(frame_direita, from_=0,command=escala, to=255, length=150, bg=cor1, fg="Green", orient=HORIZONTAL)
s_green.grid(row=1, column=1)

l_blue = Label(frame_direita, text='Blue', width=7, bg=cor1, fg='Blue', anchor='nw', font=("Time New Roman", 12, "bold"))
l_blue.grid(row=2, column=0)
s_blue=Scale(frame_direita, from_=0,command=escala,to=255, length=150, bg=cor1, fg="Blue", orient=HORIZONTAL)
s_blue.grid(row=2, column=1)


l_rgb = Label(frame_baixo, text='CÓDIGO HEX:', bg=cor1, font=("Ivy", 10, "bold"), anchor=CENTER)
l_rgb.grid(row=0,column=0, padx=5)

e_cor= Entry(frame_baixo, width=12, font=("Ivy", 10, 'bold'), justify=CENTER, state="readonly")
e_cor.grid(row=0, column=1,padx=5)

if e_cor.get() == '':
    e_cor.config(state="normal")
    e_cor.insert(0, '#000000')
    e_cor.config(state="readonly")

l_botao = Button(frame_baixo,command=clicar, text='COPIAR CÓDIGO', bg=cor1, font=("Ivy", 8, "bold"), relief=RAISED, overrelief=RIDGE)
l_botao.grid(row=0,column=2, padx=5)

l_app_nome = Label(frame_baixo, text='COLOR PICKER', bg=cor1, font=("Ivy", 15, "bold"), anchor=CENTER)
l_app_nome.grid(row=0,column=3, padx=20)

janela.mainloop()