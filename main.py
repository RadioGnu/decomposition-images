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
   
    
    liste_images = os.listdir(dossier)
    try:
        id_valeur_moyenne = liste_images.index("valeur_moyenne.csv")
    except ValueError:
        id_valeur_moyenne = -1
    if id_valeur_moyenne == -1:
        images_moyennes = {} #initialisation du dictionnaire
        images_enregistrees = [] #pas d'images enregistrees
    else:
        images_moyennes, images_enregistrees = deserialiser(dossier, liste_images)
        liste_images.pop(id_valeur_moyenne)

    for i in range(len(liste_images)) :
        image = liste_images[i]
        acces = dossier + "/" + image 
        if acces not in images_enregistrees:
            #pour retrouver les images à coup sûr dans les fichiers
            #-> chemin d'accès complet
            #création de l'objet image a partir du chemin d'accès
            imageGal = im.imageGalerie(acces)  
            #utilisation de la méthode couleur moyenne de la classe imageGalerie
            val = imageGal.couleur_moyenne() 
            images_moyennes[i] = imageGal, val 
            
    serialiser(images_moyennes, dossier)
        
    return images_moyennes 
      

def serialiser(images_moyennes, dossier):
    """Stocke le dictionnaire contenant les valeurs moyennes pour chaque image
    dans un fichier texte contenu dans le fichier de la galerie.

    Pour éviter de recalculer une fois que la galerie est mise en place.
    Réécrit le fichier à chaque fois (mais ça ne prend que 3 ms)
    """
    with open(dossier + '/' + 'valeur_moyenne.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter = ',')
        for (image, val) in images_moyennes.values():
            #On met le chemin d'accès complet pour chaque image
            chemin = image.chemin
            nom = chemin.replace(dossier +'/', '')
            #On concatène le tuple des valeurs moyennes avec acces
            writer.writerow((nom,) + val)

def deserialiser(dossier, liste_images):
    """Trouve le dico galerie à partir du fichier texte
    """

    with open(dossier + '/' + 'valeur_moyenne.csv', 'r') as file:
        lecteur = csv.reader(file, delimiter=',')
        i = 0
        images_enregistrees = []
        images_moyennes = {}
        for row in lecteur:
            nom = row[0]
            if nom in liste_images:
                #On lit simplement un chemin d'accès
                chemin = dossier + '/' + nom 
                image = im.imageGalerie(chemin)
                #et on ajoute à liste_images
                images_enregistrees.append(chemin)
                #Convertit chaque élément en flottant
                moyenne = tuple(map(float, row[1:]))
                images_moyennes[i] = image, moyenne
                i += 1

    return images_moyennes, images_enregistrees 
   
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
    ecart_min = [256, 256, 256]
    
    for image, val in dico_galerie.values(): #parcours du dictionnaire
        RGB_proche = [] #initialisation de la liste des écarts
        RGB_min = []

        for couleur in range(3):
            ecart_couleur = int(abs(val_moyenne[couleur]-val[couleur]))
            
            #ecart choisi pour avoir une couleur suffisamment proche
            if ecart_couleur <= 20: 
                RGB_proche.append(ecart_couleur)
           
            if ecart_couleur <= ecart_min[couleur]  : 
                RGB_min.append(ecart_couleur)
                
            
        #il faut que les trois soit très proche
        if len(RGB_proche)==3:
            couleur_proche.append(image)
        
        elif len(RGB_min)==3: 
            image_proche = image
            ecart_min = RGB_min     
        
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
             
    val_moy = (255, 51, 204) 
    liste = liste_image_proche(val_moy, dico)
    for element in liste :
        element.image.show()
