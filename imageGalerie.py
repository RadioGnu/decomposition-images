"""Fichier contenant la definition de la classe permettant de créer les objet image a partir des photos de la galeries d'image"""

import PIL.Image as PIL

class imageGalerie :
    def __init__(self, image):
        """ image est un chemin d'accès"""
        self.image = PIL.open(image)
        self.width = self.image.width
        self.height = self.image.height
        
        
    def liste_RGB(self):
        """liste contenant les tuples des valeurs en rouge, vert et bleu pour chaque pixel de l'image
        a voir lecture un pixel sur 5 ?"""
        self.couleur = []
        for i in range (self.width):
            for j in range(self.height):
                RGB = self.image.getpixel((i,j))
                self.couleur.append(RGB)
                
    def couleur_moyenne(self):
        """calcul la valeur moyenne pour chaque couleur en renvoie un tuple RGB"""
        
        self.liste_RGB()
        rouge = 0
        vert = 0
        bleu = 0
        for i in range (len(self.couleur)):
            rouge += int(self.couleur[i][0])
            vert += int(self.couleur[i][1])
            bleu += int(self.couleur[i][2])
        
        mr = rouge/len(self.couleur)
        mv = vert/len(self.couleur)
        mb = bleu/len(self.couleur)
        self.moyenne = (mr, mv, mb)
        return self.moyenne
    
    def rescale(self, coef):
        """permet de mettre l'image a la taille voulu pour le caneva"""
        width = int(self.width * coef)
        height = int(self.height * coef)
        rescaled_image = self.image.resize((width, height))
        return rescaled_image

