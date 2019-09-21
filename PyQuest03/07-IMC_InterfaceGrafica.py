from tkinter import *
class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "12")
        self.container01 = Frame(master)
        self.container01["pady"] = 10
        self.container01.pack()

        self.container02 = Frame(master)
        self.container02["padx"] = 10
        self.container02.pack()

        self.container03 = Frame(master)
        self.container03["padx"] = 10
        self.container03.pack()

        self.container04 = Frame(master)
        self.container04["pady"] = 10
        self. container04.pack  ()

        self.titulo = Label(self.container01, text = "Calculadora IMC")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.alturaLabel = Label(self.container02, text = "Altura  ", font=self.fontePadrao)
        self.alturaLabel.pack(side=LEFT)

        self.altura = Entry(self.container02)
        self.altura["width"] = 5
        self.altura["font"] = self.fontePadrao
        self.altura.pack(side=LEFT)

        self.massaLabel = Label(self.container03, text = "Massa", font = self.fontePadrao)
        self.massaLabel.pack(side=LEFT)

        self.massa = Entry(self.container03)
        self.massa["width"] = 5
        self.massa["font"] = self.fontePadrao
        self.massa.pack(side=LEFT)

        self.calcular = Button(self.container04)
        self.calcular["text"] = "CALCULAR!"
        self.calcular["width"] = 12
        self.calcular["font"] = ("Calibri", "8")
        self.calcular["command"] = self.calculoIMC
        self.calcular.pack()

        self.result = Label(self.container04, text = "INDICE IMC: ", font = self.fontePadrao)
        self.result["width"] = 12
        self.result.pack(side=LEFT)

        self.resultado = Label(self.container04, text = "", font= self.fontePadrao)
        self.resultado.pack()


    def calculoIMC(self):
        massa =  self.massa.get()
        altura = self.altura.get()
        resultado = float(massa) / (float(altura) * float(altura))
        self.resultado["text"] = ('{:.2f}'.format(resultado))

root = Tk()
Application(root)
root.mainloop()