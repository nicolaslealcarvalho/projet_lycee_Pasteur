from tkinter import *
import tkinter.filedialog as tkd
from tkinter import messagebox

from core import *


class interfaceJournéePre(Frame):

    def __init__(self):

        self.app = Tk()
        super().__init__(self.app)

        self.app.geometry("700x420")
        self.bg = PhotoImage(file = "comp\lycée.png")

        self.choix = None
        self.core = core()

        self.fenetrechoixfile()

        self.pack()

    def fenetrechoixfile(self):

        canvas1 = Canvas( self.app, width = 700, height = 420)
        canvas1.pack(fill = "both", expand = True)
        canvas1.create_image( 0, 0, image = self.bg, anchor = "nw")

        canvas1.create_text( 350, 20, text = "Choix du fichier xlsx :",fill="white")

        buttonchoixfile = Button(self.app, text="choix", command = self.choixfichier)
        canvas1.create_window( 340, 120, anchor = "nw",window = buttonchoixfile)

        buttonValider = Button(self.app, text="Continuer", command=self.fichierValider)
        canvas1.create_window( 330, 380, anchor = "nw",window = buttonValider)

        self.canvas = canvas1

    def choixfichier(self):

        self.choix = tkd.askopenfilename()
        #set le directory depuis core -> import
        self.core.setlisteleve(self.choix)

    def fichierValider(self):

        if self.choix == None or (".xlsx" not in self.choix):
            messagebox.showwarning("choix impossible", "Vous devait choisir un fichier correcte")
        else:
            self.canvas.destroy()
            self.fenetrenombreprof()

    def fenetrenombreprof(self):

        canvas2 = Canvas( self.app, width = 700, height = 420)
        canvas2.pack(fill = "both", expand = True)
        canvas2.create_image( 0, 0, image = self.bg, anchor = "nw")
        canvas2.create_text( 350, 20, text = "nombres professeurs par matière:",fill="white")

        canvas2.create_text( 200, 50, text = "ÉDUCATION PHYSIQUE, PRATIQUES ET CULTURE SPORTIVES",fill="white")
        canvas2.create_text( 200, 80, text = "HIST-GÉO. GÉOPOLITIQUE & SC. POLITIQUES",fill="white")
        canvas2.create_text( 200, 110, text = "HUMANITÉS, LITTÉRATURE ET PHILOSOPHIE",fill="white")
        canvas2.create_text( 200, 140, text = "LANGUES, LITTÉRATURE & CULTURES ÉTRANGÈRES - ANGLAIS",fill="white")
        canvas2.create_text( 200, 170, text = "LANGUES, LITTÉRATURE & CULTURES ÉTRANGÈRES - ANGLAIS MONDE CONTEMPORAIN",fill="white")
        canvas2.create_text( 200, 200, text = "LANGUES, LITTÉRATURE & CULTURES ÉTRANGÈRES - ESPAGNOL",fill="white")
        canvas2.create_text( 200, 230, text = "MATHÉMATIQUES",fill="white")
        canvas2.create_text( 200, 260, text = "NUMÉRIQUE ET SCIENCES INFORMATIQUES",fill="white")
        canvas2.create_text( 200, 290, text = "PHYSIQUE-CHIMIE",fill="white")
        canvas2.create_text( 200, 320, text = "SC. ÉCONO. & SOCIALES",fill="white")
        canvas2.create_text( 200, 350, text = "SCIENCES VIE & TERRE",fill="white")

        self.a1 =Entry(self.app)
        canvas2.create_window(600, 50, window= self.a1)
        self.a2 =Entry(self.app)
        canvas2.create_window(600, 80, window=self.a2)
        self.a3 =Entry(self.app)
        canvas2.create_window(600, 110, window=self.a3)
        self.a4 =Entry(self.app)
        canvas2.create_window(600, 140, window=self.a4)
        self.a5 =Entry(self.app)
        canvas2.create_window(600, 170, window=self.a5)
        self.a6 =Entry(self.app)
        canvas2.create_window(600, 200, window=self.a6)
        self.a7 =Entry(self.app)
        canvas2.create_window(600, 230, window=self.a7)
        self.a8 =Entry(self.app)
        canvas2.create_window(600, 260, window=self.a8)
        self.a9 =Entry(self.app)
        canvas2.create_window(600, 290, window=self.a9)
        self.a10 =Entry(self.app)
        canvas2.create_window(600, 320, window=self.a10)
        self.a11 =Entry(self.app)
        canvas2.create_window(600, 350, window=self.a11)

        buttonValider = Button(self.app, text="Continuer", command=self.nbvalider)
        canvas2.create_window( 330, 380, anchor = "nw",window = buttonValider)

        self.canvas2 = canvas2

    def nbvalider(self):

        listMatiere = ["ÉDUCATION PHYSIQUE, PRATIQUES ET CULTURE SPORTIVES", 
                       "HIST-GÉO. GÉOPOLITIQUE & SC. POLITIQUES",
                       "HUMANITÉS, LITTÉRATURE ET PHILOSOPHIE",
                       "LANGUES, LITTÉRATURE & CULTURES ÉTRANGÈRES - ANGLAIS",
                       "LANGUES, LITTÉRATURE & CULTURES ÉTRANGÈRES - ANGLAIS MONDE CONTEMPORAIN",
                       "LANGUES, LITTÉRATURE & CULTURES ÉTRANGÈRES - ESPAGNOL",
                       "MATHÉMATIQUES",
                       "NUMÉRIQUE ET SCIENCES INFORMATIQUES",
                       "PHYSIQUE-CHIMIE",
                       "SC. ÉCONO. & SOCIALES",
                       "SCIENCES VIE & TERRE"]

            
        for i in range(11):
            attr_nametext = f"a{i+1}"
            valuetext = getattr(self, attr_nametext)
            if valuetext.get() == "":
                messagebox.showwarning("choix impossible", "Vous devait remplir tout les champs avec des nombre different de 0")
                return
                    
            self.core.setnbprof(listMatiere[i],valuetext.get())

        sep = self.core.separation()

        if sep != None: 
             messagebox.showwarning("choix impossible", "le nombre de professeur doit etre coherent dans la matiere: " + sep )
             return 
        
        self.canvas2.destroy()

if __name__ == '__main__':
    a = interfaceJournéePre()
    a.mainloop()