"""Fichier contenant la definition de la classe permettant de creer les objets
image a partir des photos de la galerie d'images"""

import PIL.Image as PIL


class imageGalerie :
    def __init__(self, chemin):
        """initialisation de l'objet

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

        Returns self.moyenn
        -------
        TYPE : tuple 
        tuple des trois moyenne de couleurs .

        """
        
        self.liste_RGB()
        rouge = 0 #initialisation
        vert = 0
        bleu = 0
        for RGB in self.couleur: #parcour de la liste de pixel (pas fait de tableau car plus simple a parcourir)
            rouge += RGB[0]
            vert += RGB[1]
            bleu += RGB[2]
        
        mr = rouge/len(self.couleur) #calcul des moyennes
        mv = vert/len(self.couleur)
        mb = bleu/len(self.couleur)
        
        self.moyenne = (mr, mv, mb)
        return self.moyenne #permet d'acceder a la valeur lorsque la fonction est appelée
    
    
    def auto_rescale(self):
        """
        distord et retrecie l'image pour en faire un carré de 500*500, taille maximale ou elles seront affiché sur le canevas
        
        Returns
        -------
        None.

        """
        width = 500 #dimensions voulue pour les images
        height = 500
        self.image = self.image.resize((width, height))
        
    
    
    def rescale(self, x):
        """
        permet de mettre l'image a la taille voulue pour le canevas
        
        Parameters
        ----------
        coef : float
            coefficient de reduction de l'image.

        Returns
        -------
        rescaled_image : image (jpeg, png ... en fonction de l'image d'origine)

        """
        
        width = int(x)
        height = int(x)
        rescaled_image = self.image.resize((width, height))
        return rescaled_image