from tkinter import *
root = Tk()


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.fontePadrao = ("Arial", "12")
#   Container1
        self.container01 = Frame(master)
        self.container01["pady"] = 10
        self.container01.pack()
#   Container2
        self.container02 = Frame(master)
        self.container02["padx"] = 10
        self.container02.pack()
#   Container3
        self.container03 = Frame(master)
        self.container03["padx"] = 10
        self.container03.pack()
#  Container4
        self.container04 = Frame(master)
        self.container04["pady"] = 10
        self. container04.pack()
#   Container5
        self.container05 = Frame(master)
        self.container05["pady"] = 10
        self.container05.pack()
#   Container6
        self.container06 = Frame(master)
        self.container06["pady"] = 10
        self.container06.pack()
#   Rodape
        self.Rodape = Frame(master)
        self.Rodape["padx"] = 10
        self.Rodape.pack(side=BOTTOM)
#   Titulo
        self.titulo = Label(self.container01, text="Calculadora IMC")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()
#   altura
        self.alturaLabel = Label(self.container02, text="Altura em metros", font=self.fontePadrao)
        self.alturaLabel["width"] = 20
        self.alturaLabel.pack(side=LEFT)
#   entrada altura
        self.altura = Entry(self.container02)
        self.altura["width"] = 5
        self.altura["font"] = self.fontePadrao
        self.altura.pack(side=LEFT)
#   massa
        self.massaLabel = Label(self.container03, text="Massa em quilograma", font=self.fontePadrao)
        self.massaLabel["width"] = 20
        self.massaLabel.pack(side=LEFT)
#   entrada massa
        self.massa = Entry(self.container03)
        self.massa["width"] = 5
        self.massa["font"] = self.fontePadrao
        self.massa.pack(side=LEFT)
#   botao calcular
        self.calcular = Button(self.container04)
        self.calcular["text"] = "CALCULAR!"
        self.calcular["width"] = 12
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["command"] = self.calculoIMC
        self.calcular.pack()
#   resultado
        self.result = Label(self.container04, text="INDICE IMC: ", font=self.fontePadrao)
        self.result["width"] = 18
        self.result.pack(side=LEFT)
        self.result.configure(relief="ridge", font="Arial 9 bold", border=5, background="white")
#   resultado indice
        self.indice = Label(self.container05, text="", font=self.fontePadrao)
        self.indice["width"] = 20
        self.indice.pack(side=LEFT)
        self.indice.configure(relief="ridge", font="Arial 12 bold", border=4, background="white")
#   peso ideal
        self.ideal = Label(self.container06, text="-"*30, border=4, background="white")
        self.ideal.pack(side=BOTTOM)
        self.indice.configure(relief="ridge", font="Arial 12 bold", border=4, background="white")
#   rodape
        self.lblRodape = Label(self.Rodape, text="Codigo por Vítor Eduardo Bragança", font="Arial 7 bold")
        self.lblRodape.pack(side=BOTTOM)


    def calculoIMC(self):
        massa =  self.massa.get()
        altura = self.altura.get()
        indice = float(massa) / (float(altura) * float(altura))
        self.result.configure(relief="ridge", font="Arial 9 bold", border=5, background="white", text="INDICE IMC: {:.2f}".format(indice))
        if indice <= 18.5:   self.indice.configure(relief="ridge", font="Arial 12 bold", border=4, background="orange", text="ABAIXO DO PESO")
        elif (indice >= 18.6) and (indice <= 24.9):   self.indice.configure(relief="ridge", font="Arial 12 bold", border=4, background="green", text="SAUDAVEL")
        elif (indice >= 24.9) and (indice <= 29.9):   self.indice.configure(relief="ridge", font="Arial 12 bold", border=4, background="yellow", text="ACIMA DO PESO")
        elif (indice >= 29.9) and (indice <= 34.9):   self.indice.configure(relief="ridge", font="Arial 12 bold", border=4, background="orange", text="OBESIDADE GRAU I")
        elif (indice >= 34.9) and (indice <= 39.9):   self.indice.configure(relief="ridge", font="Arial 12 bold", border=4, background="red", text="OBESIDADE GRAU II")
        else:   self.indice.configure(relief="ridge", font="Arial 12 bold", border=4, background="red", text="OBESIDADE GRAU III")

        ideal = (float(altura)*72.7)-58
        self.ideal.configure(relief="ridge", font="Arial 12 bold", border=1, background="white", foreground="black", text="Sua massa ideal seria: {:.2f} kg".format(ideal))


app = Application()
app.master.title("IMC")
app.master.geometry("400x280")
mainloop()
