"""Fichier contenant la definition de la classe permettant de creer les objets
image a partir des photos de la galerie d'images"""


import PIL.Image as PIL

class imageGalerie :
    def __init__(self, chemin, taille_canevas):
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
        self.dimension = taille_canevas
        
        self.auto_rescale()        
        

    def __str__(self):
        """Permet d'identifier l'image plus facilement.
        """
        return f"{self.chemin_acces}"
    

    def liste_RGB(self):
        """Création d'une liste contenant les tuples des valeurs 
        en rouge, vert et bleu pour chaque pixel de l'image.        

        Returns
        -------
        None.

        """
        self.couleur = []
        
        for i in range (self.dimension):
            for j in range(self.dimension):
                #retourne un tuple RGB du pixel de position (i, j)
                RGB = self.image.getpixel((i,j)) 
                self.couleur.append(RGB)
        

    def couleur_moyenne(self):
        """Renvoie un tuple RGB correspondant a la couleur moyenne de l'image

        Returns self.moyenn
        -------
        TYPE : tuple 
        tuple des trois moyenne de couleurs et de la luminosité.
        """
        
        #getdata(band) renvoie une liste des valeurs des pixels
        #pour la band rouge, verte ou bleue.
        #On somme ces contributions et on les divise par la longeur,
        #pour obtenir la valeur moyenne rouge, verte et bleue.
        taille = len(self.image.getdata(1))
        moyenne_rvb = tuple(sum(self.image.getdata(band))/taille
                    for band in range(3))
       
        rouge, vert, bleu = moyenne_rvb
        
        #La luminance de l'image permet de la convertir
        #en nuances de gris.
        lum = 0.299 * rouge + 0.587 * vert + 0.114 * bleu
        moyenne = (rouge, vert, bleu, lum)
        return moyenne
    
    def auto_rescale(self):
        """Distord et rétrécit l'image pour en faire un carré de 500*500, 
        taille maximale où elle sera affichée sur le canevas.
        
        Returns
        -------
        None.

        """
        #dimensions voulue pour les images
        width = self.dimension 
        height = self.dimension
        self.image = self.image.resize((width, height))
        

"""
objet = imageGalerie("C:/Users/solen/OneDrive/Documents/decomposition-images/galerie/2.jpg")
image = objet.image
nb = image.convert("L")
nb.show()
"""

