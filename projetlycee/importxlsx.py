from openpyxl import *

class importxlsx:
    
    def __init__(self):
        self.directory = None
        self.file = None
        self.sheet = None
        self.eleve = []

    def setdirectory(self,name):
        self.directory = name

    def setfile(self):
        self.file = load_workbook(self.directory, read_only = True, data_only = True)

    def setsheet(self):
        self.sheet = self.file['Travail']

    def setlines(self):
        for row in self.sheet:
            l = list()
            for cell in row:
                l.append(cell.value)
            self.eleve.append(l)

    def geteleve(self):
        return self.eleve[1:]
