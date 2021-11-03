# Impoter random
import random


class Hero:
    """
    Class de héro
    """

    def __init__(self, nom):
        """
        Initializer la class hero et lui donnant un nom
        :param nom: Nom de héro
        """
        self.nom = nom
        # nombre point de vie
        self.vie = random.randint(1, 10) + random.randint(1, 10)
        # force d’attaque
        self.attaque = random.randint(1, 6)
        # force défense
        self.defense = random.randint(1, 6)

    def attaque(self, target_hero):
        """
        Attaquer un héro
        :param target_hero: L'héro à attaquer
        :return: None
        """
        target_hero.dommages(random.randint(1, 6) + self.attaque)

    def dommages(self, dommage):
        """
        Recevoir la dommage
        :param dommage: Dommage reçu
        :return: None
        """
        self.vie -= dommage - self.defense
        print(f"Hero {self.nom} got damage, {self.vie} heart left")

    def est_vivant(self):
        """
        Si l'héro est vivant
        :return: booléenne qui indique si l'héro est vivant
        """
        return 0 < self.vie

