# Importer le nombre pi
from math import pi


class Cercle:
    """
    La classe de cercle
    """

    def __init__(self, rayon):
        """
        Initializer la cercle avec la rayon
        :param rayon: rayon de cercle
        """
        self.rayon = rayon

    def calcul_aire(self):
        """
        Calculer et returner l'aire de cercle
        :return: aire de cercle
        """
        aire = pi * (self.rayon ** 2)
        return aire

    def calcul_circonference(self):
        """
        Calculer et returner la circonference de cercle
        :return: circonference de cercle
        """
        circonference = 2 * pi * self.rayon
        return circonference
