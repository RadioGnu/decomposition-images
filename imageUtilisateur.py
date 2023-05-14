import tkinter as tk
from PIL import Image


class imageUtilisateur():
    def __init__(self, chemin_acces: str):
        """Initialisation de la classe

        Paramaters
        ----------
            chemin_acces: le chemin d'acces relatif ou absolu vers l'image
        """
        self.chemin_acces = chemin_acces
        self.image = Image.open(self.chemin_acces)
        self.auto_rescale()
        self.width = self.image.width
        self.height = self.image.height

    def __str__(self):
        return f"{self.chemin_acces}"
    
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

    def couleur_moyenne(self):
        """
        Renvoie un tuple RGB correspondant a la couleur moyenne de l'image, du 
        blanc ou du noir pour changer la couleur de l'écriture sur l'interface 
        si la couleur moyenne est trop foncée ou trop claire'

        Returns
        self.moyenne_hexa 
        -------
        TYPE : str 
        correspondance hexa de la couleur moyenne en RGB. (en self au cas ou on aurait besoin de la rappeler)
        
        font_color
        -------
        TYPE : str 
        Incation pour utiliser une police noir ou blanche en fonction de la clareté de l'image

        """
        
        font_color = "black"
        #initialisation
        rouge = 0 
        vert = 0
        bleu = 0
        #parcours par pixel
        for i in range (self.width):
            for j in range(self.height):
                #retourne un tuple RGB du pixel de position (i, j)
                RGB = self.image.getpixel((i,j)) 
                rouge += RGB[0]
                vert += RGB[1]
                bleu += RGB[2]
            
        #calcul des moyennes
        taille = self.width * self.height
        mr = rouge/taille
        mv = vert/taille
        mb = bleu/taille
        #si la couleur est trop foncée, on ne vera pas les écritures
        if (mr, mv, mb)<= (127, 127, 127):
            font_color = "white"
        
        self.moyenne_hexa = "#{:02x}{:02x}{:02x}".format(int(mr), int(mv), int(mb))
        
        # La luminance pour convertir l'image couleur en une image noir et blanc est calculée par Gris = 0,299 * Rouge + 0,587 * Vert + 0,114 * Bleu
        lum_main = 0,299 *mr + 0,587 * mv + 0,114 * mb
        return self.moyenne_hexa, lum_main, font_color

    def subdivision(self, facteur):
        """
        Divise l'image en carré répartis tous les largeur/facteur

        Parameters
        ----------
        facteur: nombre de sous-division de la longeur,
            au carré le nombre de carreaux

        Returns coordonnee
        -------
        Type: list 
        element: coordonnes du coin nord-ouest des carreaux
        """
        #On echantillone la longueur
        intervalle = [n* self.width/facteur for n in range(facteur)]

        coordonnee = []
        for j in intervalle:
            for k in intervalle:
                #On ajoute tous les coins nord-ouest
                coordonnee.append((j,k))
        
        return coordonnee

    def couleur_carreaux(self, facteur):
        """Calcule les couleurs moyenne pour chaque carreaux

        Parameters
        ----------
            facteur: cf subdivision plus haut

        Returns coordonnee
        -------
            Type: dict
            clef: coordonnee du coin nord-ouest du carreau
            valeur: couleur moyenne du carreau
            
        """

        coordonnee = self.subdivision(facteur)
        couleur_carreaux = {}

        for coord in coordonnee:
            #Limites du carreau en longeur et largeur
            x = coord[0] + self.width/facteur
            y = coord[1] + self.width/facteur
            
            rouge = 0
            vert = 0
            bleu = 0
            #Pour faire la moyenne, nombre de pixels
            count = 0
            
            for i in range(int(coord[0]), int(x)):
                for j in range(int(coord[1]), int(y)):
                    count += 1
                    RGB = self.image.getpixel((i,j))
                    rouge += RGB[0]
                    vert += RGB[1]
                    bleu += RGB[2]

            #On ajoute le couple coin, valeur moyenne
            couleur_carreaux[coord] = (rouge/count, vert/count, bleu/count)
        return couleur_carreaux


#test
"""
if __name__ == "__main___":
    chemin = "C:/Users/solen/OneDrive/Bureau/test_galerie/2.jpg"
    image = imageUtilisateur(chemin)
    m = image.couleur_moyenne(1)
    print(m)
"""
