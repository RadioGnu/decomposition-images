# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:31:10 2023

@author: DAMON Coline
"""

import os
import csv

import imageGalerie as im
import random


def dico_galerie(dossier):
    """ Lit le dossier contenant les images de la galerie et crée
    un dictionnaire images_moyennes qui regroupe les objet images

    Parameters
    ----------
    dossier : chemin d'acces
        chemin d'accès du dossier ou sont stocké les images à utiliser

    Returns
    -------
    images_moyennes: dict
        clé  : l'indice de l'image dans le dossier 
        valeur : objet image et tuple valeur moyenne en RGB.
    """
   
    
    if os.path.isfile(dossier + '/' + "valeur_moyenne.csv"):
        images_moyennes = deserialiser(dossier)

    else:
        liste_images = [f for f in os.listdir(dossier) 
                        if f != "valeur_moyenne.csv"]

        images_moyennes = {} #initialisation du dictionnaire
        for i in range(len(liste_images)) :
            if i not in images_moyennes :
                #pour retrouver les images à coup sûr dans les fichiers
                #-> chemin d'accès complet
                acces = dossier + "/" + liste_images[i] 
                #création de l'objet image a partir du chemin d'accès
                image = im.imageGalerie(acces)  
                #utilisation de la méthode couleur moyenne de la classe imageGalerie
                val = image.couleur_moyenne() 
                images_moyennes[i] = image, val 
                
        serialiser(images_moyennes, dossier)
            
    return images_moyennes 
      

def serialiser(images_moyennes, dossier):
    """Stocke le dictionnaire contenant les valeurs moyennes pour chaque image
    dans un fichier texte contenu dans le fichier de la galerie.

    Pour éviter de recalculer une fois que la galerie est mise en place.
    """
    with open(dossier + '/' + 'valeur_moyenne.csv', 'w') as file:
        writer = csv.writer(file, delimiter = ',')
        for (image, val) in images_moyennes.values():
            #On met le chemin d'accès complet pour chaque image
            chemin = image.chemin 
            #On concatène le tuple des valeurs moyennes avec acces
            writer.writerow((chemin,) + val)

def deserialiser(dossier):
    """Trouve le dico galerie à partir du fichier texte
    """

    with open(dossier + '/' + 'valeur_moyenne.csv', 'r') as file:
        lecteur = csv.reader(file, delimiter=',')
        i = 0
        images_moyennes = {}
        for row in lecteur:
            #On lit simplement un chemin d'accès
            image = im.imageGalerie(row[0])
            #Convertit chaque élément en flottant
            moyenne = tuple(map(float, row[1:]))
            images_moyennes[i] = image, moyenne
            i += 1

    return images_moyennes
    
   
def liste_image_proche(val_moyenne, dico_galerie):
    """Associe à la valeur moyenne de chaque subdivision de l'image initiale 
    toutes les image dont la valeur moyenne est proche.

    Parameters
    ----------
    val_moyenne : tuple 
        tuple contenant les 3 valeurs RGB moyenne de la subdivision
    dico_galerie : dict
        clé  : l'indice de l'image dans le dossier initial
        valeur : objet image et tuple valeur moyenne en RGB.

    Returns
    -------
    couleur_proche : list
        liste des image ayant une couleur moyenne proche de la subdivision
    """
    
    couleur_proche = []
    #distance la plus élevée a l'image -> nécessairement des images plus proche
    min_couleur = 3*(255**2) 
    image_proche = None
    for image, val in dico_galerie.values(): #parcours du dictionnaire
        liste_pixel_select = [] #initialisation de la liste des écarts
        somme = 0
        for couleur in range(3):
            ecart_couleur = int(abs(val_moyenne[couleur]-val[couleur]))
            somme += ecart_couleur**2
            #ecart choisi pour avoir une couleur suffisamment proche
            if ecart_couleur <= 20: 
                liste_pixel_select.append(ecart_couleur)
                #il faut que les trois soit très proche
                if len(liste_pixel_select)==3: 
                    couleur_proche.append(image)
                
            elif somme < min_couleur : 
                image_proche = image

        #si il n'y a pas d'image proche, choisir celle la plus proche
        if len(couleur_proche) == 0: 
            couleur_proche.append(image_proche) 
        
    return couleur_proche

def choix_image(val_moyenne, dico_galerie):
    """Choix aléatoire de l'image parmi la liste des images de couleur moyenne
    proche de celle de la subdivision.

    Parameters
    ----------
    liste_image : list
        DESCRIPTION.

    Returns
    -------
    image_finale : TYPE
        DESCRIPTION.

    """
    liste_image = liste_image_proche(val_moyenne, dico_galerie)
    
    i = random.randint(0, len(liste_image)-1)
    image_finale = liste_image[i]
    
    return image_finale


#Tests
if __name__ == "__main__":
    dossier ="galerie"
    dico = dico_galerie(dossier)
             
    val_moy = (110, 110, 110) 
    liste = liste_image_proche(val_moy, dico)
    image_finale = choix_image(val_moy, dico)
    image_finale.image.show()
