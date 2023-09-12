class Demineur:
    def __init__(self, tailleCadr, nbBombes):
        pass

    def generationCadr(self):
        """
        Génère le Cadrillage en fonction du nombre de bombe
        """
        pass

    def drapeau(self):
        """
        Met un drapeau sur la case ou l'enlève s'il y en a déjà un
        """
        pass

    def decouvrirCase(self):
        """
        Découvre la case choisit :

        - Si c'est une bombe, appelle la fonction gameOver
        - Sinon Si toutes les cases non-bombes sont découvertes, appelle la fonction gameWon
        - Sinon découvre la case
        """
        pass

    def gameOver(self):
        """
        -écran d'affichage de de fin de jeu lorsqu'un joueur à perdu
        -affiche l'emplacement de toutes les bombes sur le plateau
        -met un message disant qu'on a perdu
        """
        pass


    def gameWon(self):
        """
        -écran d'affichage de de fin de jeu lorsqu'un joueur à gagner
        -nous informe qu'on a gagner
        """
        pass


    def __str__(self):
        """
        affiche d'une bonne maniere dans le terminale le cadrillage
        """
        pass

