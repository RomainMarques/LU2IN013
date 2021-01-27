from Plateforme import *

class Robot(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def accelerer(self):
        #a implementer
        return
    def ralentir(self):
        #a implementer
        return
    def bouger(self, direction):
        #a implementer
        return

    def carre(self):
        self.setLong(1)
        self.setLarg(1)
        self.setLong(-1)
        self.setLarg(-1)
        
    def setLong(self, lg):
        self.x=self.x + lg
    def setLarg(self, lg):
        self.y = self.y + lg
    def positionRobot(self):
        return (self.x, self.y)

    