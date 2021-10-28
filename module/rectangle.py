class Rectangle:
    """
    La classe de Rectangle
    """

    # Aire de rectangle
    aire: float

    def __init__(self, largeur, longueur):
        """
        Initializer une classe rectangle
        :param largeur: Largeur de rectangle
        :param longueur: Longueur de rectangle
        """
        self.largeur = largeur
        self.longueur = longueur

    def calcul_aire(self):
        """
        Calculer l'aire de rectangle
        :return: None
        """
        self.aire = self.largeur * self.longueur

    def afficher_infos(self):
        """
        Afficher les informations de rectangle
        :return: None
        """
        print(f"Largeur: {self.largeur}")
        print(f"Longueur: {self.longueur}")
        print(f"Aire: {self.aire}")
