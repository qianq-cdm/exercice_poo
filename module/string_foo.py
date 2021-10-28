class StringFoo:
    """
    La classe de String
    """

    # String sauvegardé
    string: str

    def set_string(self, string):
        """
        Accepte une string en paramètre et la sauvegarde dans un attribut
        :param string: String à sauvegarder
        :return: None
        """
        self.string = string

    def print_string(self):
        """
        Afficher la string sauvegardé en majuscule
        :return: None
        """
        print(self.string.upper())
