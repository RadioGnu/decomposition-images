import tkinter as tk
from PIL import Image

class imageUtilisateur():
    def __init__(self, chemin_acces: str):
        """Initialisation de la classe
        Input:
            chemin_acces: le chemin d'acces relatif ou absolu vers l'image
        """
        self.image = Image.open(chemin_acces)
        self.width = self.image.width
        self.height = self.image.height
        self.square_crop()

    def __str__(self):
        pass
    
    def __pass__(self):
        pass

    def square_crop(self):
        """Rogne l'image self.image selon sa dimension la plus faible en carré

        On obtient donc une image carree (facilement decoupable)
        """
        #Recherche de la dimension la plus faible length
        if self.width > self.height:
            length = self.height
        else:
            length = self.width

        #Boite de rognage
        boite = (0,0, length, length)
        self.image = self.image.crop(boite)


    def subdivision(self, facteur:int):
        """Divise l'image en carré répartis tous les largeur/facteur

        Input:
            facteur: nombre de sous-division de la longeur,
            au carré le nombre de carreaux
        Output:
            liste coordonnee
            element = coin nord-ouest des carreaux
        """
        #On echantillone la longueur
        intervalle = [n* self.width/facteur for n in range(facteur)]

        coordonnee = []
        for j in intervalle:
            for k in intervalle:
                #On ajoute tous les coins nord-ouest
                coordonnee.append((j,k))
        
        return coordonnee

    def couleur_moyenne(self, facteur):
        """Calclule les couleurs moyenne pour chaque carreaux

        Input:
            facteur: cf subdivision plus haut
        Output:
            dictionnaire coordonnee
            clef: coin nord-ouest du carreau
            valeurs: couleur moyenne du carreau
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


