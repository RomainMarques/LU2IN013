class Plateforme(object):
    L=0
    l=0
    Plate=[]
    def __init__(self, longueur, largeur):
        global L
        global l
        L=longueur
        l=largeur
        self.longueur = longueur
        self.largeur = largeur
        self.map = []
        
    @staticmethod
    def initPlateforme():
        global Plate
        map=[]
        for i in range (L):
            liste=[]
            for j in range (l):
                liste.append(0)
            map.append(liste)
        Plate = map
        return Plate

    @staticmethod
    def getLongueur(self):
        return L
    @staticmethod
    def getLargeur(self):
        return l
    