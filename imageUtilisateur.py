import tkinter as tk
from PIL import Image

class imageUtilisateur():
    def __init__(self):
        self.fichier_image = Image.open("gallerie/test.jpg")
        self.width = self.fichier_image.width
        self.height = self.fichier_image.height
        self.crop()

    def __str__(self):
        pass
    
    def __pass__(self):
        pass

    def crop(self):
        if self.width > self.height:
            length = self.height
        else:
            length = self.width

        boite = (0,0, length, length)
        self.fichier_image = self.fichier_image.crop(boite)


    def subdivision(self, facteur:int):
        """Subdivise l'image en 4^facteur sous-images.
        """
        pass


test = imageUtilisateur()
