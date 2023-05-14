"""Fichier contenant la definition de la classe permettant de creer les objets
image a partir des photos de la galerie d'images"""


import PIL.Image as PIL

class imageGalerie :
    def __init__(self, chemin, taille_caneva):
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
        self.dimension = taille_caneva
        
        self.auto_rescale()
        
        
        
        
        
    def __str__(self):
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
        
        #calcul des moyennes des couleur des sous pixels
        mr = rouge/len(self.couleur) 
        mv = vert/len(self.couleur)
        mb = bleu/len(self.couleur)
        
        
        
        # La luminance pour convertir l'image couleur en une image noir et blanc est calculée par Gris = 0,299 * Rouge + 0,587 * Vert + 0,114 * Bleu
        lum = 0.299 *mr + 0.587 * mv + 0.114 * mb
        moyenne = (mr, mv, mb, lum)
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

