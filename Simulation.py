from Plateforme import *
from Robot import *

class Simulation(object):

  def __init__(self, longeur, largeur, posXRobot, posYRobot):
      self.plateforme = Plateforme(longeur, largeur)
      self.robot = Robot(posXRobot, posYRobot)