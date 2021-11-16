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
        self.force_attaque = random.randint(1, 6)
        # force défense
        self.force_defense = random.randint(1, 6)

    def attaque(self):
        """
        faire une attaque. Retourne une valeur de 1d6 plus la force d’attaque
        :return: None
        """
        return random.randint(1, 6) + self.force_attaque

    def dommages(self, dommage):
        """
        recevoir des dommages. Accepte en paramètre le nombre de dommage.
        hp -= dommage - force_defense
        :param dommage: Dommage reçu
        :return: None
        """
        self.vie -= dommage - self.force_defense
        print(f"Hero {self.nom} got damage, {self.vie} hp left")

        if self.est_vivant():
            print("Target is still alive")
        else:
            print("Target dies")

    def est_vivant(self):
        """
        méthode est_vivant qui retourne une booléenne qui est logiquement associée au nom de la méthode
        :return: booléenne qui indique si l'héro est vivant
        """
        return 0 < self.vie

