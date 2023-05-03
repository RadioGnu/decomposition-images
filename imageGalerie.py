"""Fichier contenant la definition de la classe permettant de creer les objets
image a partir des photos de la galerie d'images"""

import PIL.Image as PIL

class imageGalerie :
    def __init__(self, chemin):
        """
        initialisation de l'objet

        Parameters
        ----------
        chemin : chemin d'accès de l'image dans le gestionaire de fichier

        Returns
        -------
        None.

        """
        self.chemin = chemin 
        #ouvre l'image avec la bibliothèque pour pouvoir utiliser les fonctions
        self.image = PIL.open(chemin) 
        #permet que toutes les images soient dans les dimensions voulues
        self.auto_rescale()
        self.width = self.image.width
        self.height = self.image.height
        
        
        
    def liste_RGB(self):
        """Création d'une liste contenant les tuples des valeurs 
        en rouge, vert et bleu pour chaque pixel de l'image.        

        Returns
        -------
        None.

        """
        self.couleur = []
        for i in range (self.width):
            for j in range(self.height):
                #retourne un tuple RGB du pixel de position (i, j)
                RGB = self.image.getpixel((i,j)) 
                self.couleur.append(RGB)
                
    def couleur_moyenne(self):
        """Renvoie un tuple RGB correspondant a la couleur moyenne de l'image

        Returns self.moyenn
        -------
        TYPE : tuple 
        tuple des trois moyenne de couleurs.
        """
        
        self.liste_RGB()
        #initialisation
        rouge = 0 
        vert = 0
        bleu = 0
        #parcours de la liste de pixel
        for RGB in self.couleur: 
            rouge += RGB[0]
            vert += RGB[1]
            bleu += RGB[2]
        
        #calcul des moyennes
        mr = rouge/len(self.couleur) 
        mv = vert/len(self.couleur)
        mb = bleu/len(self.couleur)
        
        self.moyenne = (mr, mv, mb)
        #permet d'acceder à la valeur lorsque la fonction est appelée
        return self.moyenne
    
    def auto_rescale(self):
        """Distord et rétrécit l'image pour en faire un carré de 500*500, 
        taille maximale où elle sera affichée sur le canevas.
        
        Returns
        -------
        None.

        """
        #dimensions voulue pour les images
        width = 600 
        height = 600
        self.image = self.image.resize((width, height))
        
    def rescale(self, cote):
        """Permet de mettre l'image a la taille voulue pour le canevas
        
        Parameters
        ----------
        cote : float
            Taille de l'image finale (carrée)

        Returns
        -------
        rescaled_image : image (jpeg, png ... en fonction de l'image d'origine)
        """
        
        # +1 pour eviter davoir des trous dans la grille => arondi au dessus plutot que au dessous
        width = int(cote)+1
        height = int(cote)+1
        rescaled_image = self.image.resize((width, height))
        return rescaled_image
