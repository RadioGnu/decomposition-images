# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:31:10 2023

@author: DAMON Coline
"""
import os
import csv

import imageGalerie as im

def dico_galerie(dossier):
    
    """
    Lit la liste des chemins des images et crée un dictionnaire images_moyennes 
    qui regroupe les images et ayant pour clé l'indice de l'image et comme valeur son chemin.
    
    """
    
    
    if os.path.isfile(dossier + '/' + "valeur_moyenne.csv"):
        images_moyennes = deserialiser(dossier)

    else:
        liste_images = [f for f in os.listdir(dossier) 
                        if f != "valeur_moyenne.csv"]

        images_moyennes = {}
        for i in range(len(liste_images)) :
            if i not in images_moyennes :
                acces = dossier + "/" +liste_images[i]
                image = im.imageGalerie(acces)
                val = image.couleur_moyenne()
                images_moyennes[i] = image, val

        serialiser(images_moyennes, dossier)
                
    return images_moyennes 
      

def serialiser(images_moyennes, dossier):
    """
    Stocke le dictionnaire contenant les valeurs moyennes pour chaque image
    dans un fichier texte contenu dans le fichier de la galerie.

    Pour éviter de recalculer une fois que la gallerie est mise en place.
    """
    with open(dossier + '/' + 'valeur_moyenne.csv', 'w') as file:
        writer = csv.writer(file, delimiter = ',')
        for (image, val) in images_moyennes.values():
            #On met le chemin d'accès complet pour chaque image
            chemin = image.chemin 
            #On concatène le tuple des valeurs moyennes avec acces
            writer.writerow((chemin,) + val)

def deserialiser(dossier):
    """Trouve le dico gallerie à partir du fichier texte
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
    
   
def couleur_proche(val_moyenne, images_moyennes):
    """Associe à la valeur moyenne de chaque pixel 
    de l'image initiale toutes les image dont 
    la valeur moyenne est proche

    Returns
    dictionnaire (ou liste?) des images choisies
    None.
    """

    couleur_proche = []
    for image, val in images_moyennes.values():
        liste_pixel_select = []
        for couleur in range (3):
            ecart_couleur = int(abs(val_moyenne[couleur]-val[couleur]))
            
            if ecart_couleur <= 20:
                liste_pixel_select.append(ecart_couleur)
                if len(liste_pixel_select)==3:
                    couleur_proche.append(image)
    return couleur_proche

#Tests
if __name__ == "__main__":
    dossier = "gallerie"
    dico = dico_galerie(dossier)
    #val_moy = (12, 9,10)
    #print(couleur_proche(val_moy, dico))
