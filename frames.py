from tkinter import *

from cores import *

janela = Tk()
janela.title('Calculadora de IMC')
janela.geometry('295x230')
janela.configure(bg=branco)

# Frames ----------------------------------------------------------------------------------

frame_cima = Frame(janela, width=295, height=50, bg=branco, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=180, bg=branco, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Calculo Peso ----------------------------------------------------------------------------------

def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    resultado = imc

    if resultado < 18.5:
        l_resultado_imc['text'] = 'O seu IMC é: Abaixo do Peso'
    elif resultado >= 18.5 and resultado < 25:
        l_resultado_imc['text'] = 'O seu IMC é: Normal'
    elif resultado >= 25 and resultado < 30:
        l_resultado_imc['text'] = 'O seu IMC é: Sobrepeso'
    else:
        l_resultado_imc['text'] = 'O seu IMC é: Obesidade'

    l_resultado['text'] = '{:.{}f}'.format(resultado, 2)

# Título ----------------------------------------------------------------------------------

app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat',
                 anchor='center', font=('Ivy 16 bold'), bg=preto, fg=amarelo)
app_nome.place(x=0, y=5)

# Linha ----------------------------------------------------------------------------------

app_linha = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat',
                 anchor='center', font=('Ivy 1'), bg=amarelo, fg=amarelo)
app_linha.place(x=0, y=35)

# Peso ----------------------------------------------------------------------------------

l_peso = Label(frame_baixo, text='Insira seu peso: ', height=1, padx=0, relief='flat',
                 anchor='center', font=('Ivy 10 bold'), bg=branco, fg=preto)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

e_peso = Entry(frame_baixo, width=4,relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

# Altura ----------------------------------------------------------------------------------

l_altura = Label(frame_baixo, text='Insira sua altura: ', height=1, padx=0, relief='flat',
                 anchor='center', font=('Ivy 10 bold'), bg=branco, fg=preto)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

e_altura = Entry(frame_baixo, width=4,relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

# Resultado ----------------------------------------------------------------------------------

l_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=6, pady=12, relief='flat',
                 anchor='center', font=('Ivy 24 bold'), bg=preto, fg=amarelo)
l_resultado.place(x=175, y=10)

# Resultado IMC ----------------------------------------------------------------------------------

l_resultado_imc = Label(frame_baixo, text=' ', width=37, height=1, padx=0, pady=10, relief='flat',
                 anchor='center', font=('Ivy 10 bold'), bg=branco, fg=preto)
l_resultado_imc.place(x=0, y=90)

# Botão ----------------------------------------------------------------------------------

b_calcular = Button(frame_baixo, command=calcular, text='Calcular ', width=34, height=1, overrelief=SOLID, relief='raised',
                 anchor='center', font=('Ivy 10 bold'), bg=preto, fg=amarelo)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=35)