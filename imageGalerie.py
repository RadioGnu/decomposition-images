"""Fichier contenant la definition de la classe permettant de crÃ©er les objet image a partir des photos de la galeries d'image"""

import PIL.Image as PIL
import time


class image_galerie :
    def __init__(self, chemin):
        """
        initialisation de l'objet

        Parameters
        ----------
        image : chemin d'accès de l'image dans le gestionaire de fichier
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.chemin = chemin 
        self.image = PIL.open(chemin) #ouvre l'image avec la bibliothèque pour pouvoir utiliser les fonctions
        self.auto_rescale()
        self.width = self.image.width
        self.height = self.image.height
        
        
        
    def liste_RGB(self):
        """
        création d'une liste contenant les tuples des valeurs en rouge, vert et bleu pour chaque pixel de l'image
        

        Returns
        -------
        None.

        """
        self.couleur = []
        for i in range (self.width):
            for j in range(self.height):
                RGB = self.image.getpixel((i,j)) #retourne un tupple RGB du pixel de position i, j
                self.couleur.append(RGB)
                
    def couleur_moyenne(self):
        """
        renvoie un tuple RGB correspondant a la couleur moyenne de l'image

        Returns
        -------
        TYPE
            tuple des couleurs moyennes.

        """
        
        self.liste_RGB()
        rouge = 0
        vert = 0
        bleu = 0
        for RGB in self.couleur: #parcour de la liste de pixel (pas fait de tableau car plus simple a parcourir)
            rouge += RGB[0]
            vert += RGB[1]
            bleu += RGB[2]
        
        mr = rouge/len(self.couleur)
        mv = vert/len(self.couleur)
        mb = bleu/len(self.couleur)
        
        self.moyenne = (mr, mv, mb)
        return self.moyenne
    
    
    def auto_rescale(self):
        """
        distord et retrecie l'image pour en faire un carré de 500*500, taille maximale ou elles seront affiché sur le canevas
        
        Returns
        -------
        None.

        """
        width = 500
        height = 500
        self.image = self.image.resize((width, height))
        
    
    
    def rescale(self, coef):
        """permet de mettre l'image a la taille voulu pour le caneva"""
        width = int(self.width * coef)
        height = int(self.height * coef)
        rescaled_image = self.image.resize((width, height))
        return rescaled_image


<<<<<<< Updated upstream:Class galerie.py

        
    
=======
    


>>>>>>> Stashed changes:imageGalerie.py
