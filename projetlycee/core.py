from importxlsx import *
from exportxlsx import *


class core():

    def __init__(self):
        self.importxlsx = importxlsx()
        self.exportxlsx = exportxlsx()
        self.spec = list()
        self.listEleve = None
        

    def getImportxlsx(self):
        # set le document xlsx sur lequel est stocker toute les donné
        return self.importxlsx
    
    def setlisteleve(self,nameDir):
        # permet de separer les eleve de 1er generale des autres
        self.importxlsx.setdirectory(nameDir)
        self.importxlsx.setfile()
        self.importxlsx.setsheet()
        self.importxlsx.setlines()
        self.listEleve = self.importxlsx.geteleve()
        for i in self.listEleve:
            if '1générale' not in i:
                del i


    def setnbprof(self,name,value):
        # regarde si la spe est deja existente sinon la rajoute a la liste
        if name not in self.spec:
            self.spec.append(name)
            attr_name = f"spe{name}"
            setattr(self, attr_name, list())
        # atribue le nombre de prof a la spe mis en paramettre
        attr_name = f"nbProf{name}"
        setattr(self, attr_name, value)

    def separation(self):
        # permet de repartir les eleve dans les spe qui les concerne
        for i in self.spec:
            for j in self.listEleve:
                if i in j:
                    attr_name = f"spe{i}"
                    getattr(self, attr_name).append(j)
        
        # permet de connaitre le nombre optimal d'heure pour chaque spe en fonction du nombre de prof de chacune
        for i in self.spec:
            attr_namelist = f"spe{i}"
            attr_nb = f"nbProf{i}"
            eleveParSpe = getattr(self, attr_namelist)
            nbProfParSpe = getattr(self, attr_nb)
            heuremin = 0
            tempo = 100

            for h in range(1,4):
                clac = len(eleveParSpe) / (h * int(nbProfParSpe))
                if (abs(clac - 20) < abs(tempo - 20)) and (clac <= 35):
                    heuremin = h
                    tempo = clac
            print("eleve par groupe de " + i +" : " + str(tempo))
            if tempo == 100:
                return i

            # creation de la taille des groupe dans chaque spé
            attr_taillegroupe = f"taillegroupe{i}"
            setattr(self, attr_taillegroupe, tempo)

            # creation du nombre d'heure pour chaque spé
            attr_nbhoraire = f"nbHoraire{i}"
            setattr(self, attr_nbhoraire, heuremin)
            print("nbHeure: " + str(getattr(self,attr_nbhoraire)))

            # creation des groupe associter a chaque spe
            for j in range(heuremin):
                for p in range(int(nbProfParSpe)):
                    attr_nbgroupetotal = f"groupe{p}{j}{i}"
                    setattr(self, attr_nbgroupetotal, None)

            #print(int(18.7)!=(18.7))

    

        

    

    
