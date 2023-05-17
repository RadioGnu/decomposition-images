# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:31:10 2023

@author: DAMON Coline
"""

import csv
import os
import random

import imageGalerie as im


def dico_galerie(dossier, taille_caneva):
    """Lit le dossier contenant les images de la galerie et crée
    un dictionnaire images_moyennes qui regroupe les objet images

    Parameters
    ----------
    dossier: str
        Chemin d'acces vers le dossier contenant la galerie
        
    taille_caneva : int
        taille maximale que les images de la galerie peuvent avoir

    Returns
    -------
    images_moyennes: dict
        clef   : l'indice de l'image dans le dossier 
        valeur : objet image et tuple valeur moyenne en RGB et lum.
    """
   
    
    liste_images = os.listdir(dossier)
    try:
        id_valeur_moyenne = liste_images.index("valeur_moyenne.csv")
    except ValueError:
        id_valeur_moyenne = -1
    if id_valeur_moyenne == -1:
        images_moyennes = {} #initialisation du dictionnaire
        images_enregistrees = [] #pas d'images enregistrées
    else:
        images_moyennes, images_enregistrees = deserialiser(dossier, liste_images, taille_caneva)
        liste_images.pop(id_valeur_moyenne)

    for i in range(len(liste_images)) :
        image = liste_images[i]
        acces = dossier + "/" + image 
        if acces not in images_enregistrees:
            #pour retrouver les images à coup sûr dans les fichiers
            #-> chemin d'accès complet
            #création de l'objet image a partir du chemin d'accès
            imageGal = im.imageGalerie(acces, taille_caneva)
            
            # utilisation de la méthode couleur moyenne de la classe imageGalerie
            # incrémentation du dictionnaire d'images couleurs + luminosité en dernière valeur
            val = imageGal.couleur_moyenne() 
           
            imageNB = imageGal.image
            imageNB = imageNB.convert("L")
            images_moyennes[i] = imageGal, imageNB, val
            
            
    serialiser(images_moyennes, dossier)
        
    return images_moyennes
      



def serialiser(images_moyennes, dossier):
    """Stocke le dictionnaire contenant les valeurs moyennes pour chaque image
    dans un fichier csv contenu dans le fichier de la galerie.

    Parameters
    ----------
    images_moyennes: dict
        clef   : l'indice de l'image dans le dossier 
        valeur : objet image et tuple valeur moyenne en RGB.    

    dossier: str
        Chemin d'acces vers le dossier contenant la galerie
    
    taille_caneva : int
        taille maximale que les images de la galerie peuvent avoir

    Returns:
    --------
    None

    """
    with open(dossier + '/' + 'valeur_moyenne.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter = ',')
        for (image, imageNB, val) in images_moyennes.values():
            #On met le chemin d'accès complet pour chaque image
            chemin = image.chemin
            nom = chemin.replace(dossier +'/', '')
            #On concatène le tuple des valeurs moyennes avec acces
            writer.writerow((nom,) + val)



def deserialiser(dossier, liste_images, taille_caneva):
    """Stocke le dictionnaire contenant les valeurs moyennes pour chaque image
    dans un fichier csv contenu dans le fichier de la galerie.
    Permet de grandement accelerer la lecture des images après avoir charger 
    la galerie une fois

    Parameters
    ----------
    dossier: str
        Chemin d'acces vers le dossier contenant la galerie

    liste_images: list
        liste des chemins d'accès de toutes les images contenues dans la galerie
    
    taille_caneva : int
        taille maximale que les images de la galerie peuvent avoir

    Returns:
    --------
    images_moyennes: dict
        clef   : l'indice de l'image dans le dossier 
        valeur : objet image et tuple valeur moyenne en RGB + luminosité.

    images_enregistrees: list
        Chemins vers les images qui sont enregistrées dans le csv.


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
                image = im.imageGalerie(chemin, taille_caneva)
                imageNB = image.image
                imageNB = imageNB.convert("L")
                #et on ajoute à liste_images
                images_enregistrees.append(chemin)
                #Convertit chaque élément en flottant
                moyenne = tuple(map(float, row[1:]))
                images_moyennes[i] = image, imageNB, moyenne
                i += 1

    return images_moyennes, images_enregistrees 
   
def liste_image_proche(val_moyenne, dico_galerie):
    """Associe à la valeur moyenne de chaque subdivision de l'image initiale 
    toutes les image dont la valeur moyenne est proche.

    Parameters
    ----------
    val_moyenne : tuple 
        tuple contenant les 3 valeurs RGB moyenne de la subdivision et la valeur moyenne de la luminosité.
    dico_galerie : dict
        clé  : l'indice de l'image dans le dossier initial
        valeur : objet image et tuple valeur moyenne en RGB.

    Returns
    -------
    couleur_proche : list
        liste des images ayant une couleur moyenne proche de la subdivision
    """
    
    couleur_proche = []
    #distance la plus élevée a l'image -> nécessairement des images plus proche
    ecart_min = [256, 256, 256]
    
    for image, imageNB, val in dico_galerie.values(): #parcours du dictionnaire
        RGB_proche = [] #initialisation de la liste des écarts
        RGB_min = []

        for couleur in range(3):
            ecart_couleur = int(abs(val_moyenne[couleur]-val[couleur]))
            
            #ecart choisi pour avoir une couleur suffisamment proche
            if ecart_couleur <= 30: 
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
    val_moyenne : tuple 
        tuple contenant les 3 valeurs RGB moyenne de la subdivision
    dico_galerie : dict
        clé  : l'indice de l'image dans le dossier initial
        valeur : objet image et tuple valeur moyenne en RGB +luminosité.

    Returns
    -------
    image_finale : objet imageGalerie 
        L'image choisie aléatoirement pour aller sur le canevas.

    """
    
    liste_image = liste_image_proche(val_moyenne, dico_galerie)
    i = random.randint(0, len(liste_image)-1)
    image_finale = liste_image[i]
    
    return image_finale

def image_proche_noir_et_blanc(lum_image_ref, dico_galerie):
    """
    Même fonctionnement que liste_image_proche sans le côté aléatoire, permettant de choisir 
    l'image la plus proche en terme de luminosité moyenne

    Parameters
    ----------
    lum_image_ref : int
        luminosité moyenne de la subdivision
        
    dico_galerie : dict
        clé  : l'indice de l'image dans le dossier initial
        valeur : objet image et tuple valeur moyenne en RGB + luminosité.

    Returns
    -------
    image_proche : objet PIL.Image 
        L'image choisie aléatoirement pour aller sur le canevas.

    """
    
    liste_lum = []
    ecart_min = 256
    
    #parcours du dictionnaire
    for image, imageNB, val_moy in dico_galerie.values():
        lum_moy = val_moy[3]
        liste_lum.append(lum_moy)
        #calcul de l'écart de luminance entre la subdivision et l'image
        ecart = abs(lum_moy-lum_image_ref)

        if ecart <= ecart_min :
            ecart_min = ecart
            image_proche = imageNB
    
    return image_proche


def rescale(image, facteur, taille_canevas):
    """Permet de mettre l'image a la taille voulue pour le canevas
    
    Parameters
    ----------
    image : objet PIL
        Image dont on veut modifier la taille
    
    facteur : int
        facteur de division de la taille de l'image
    
    taille_canevas : int
        taille maximale que les images de la galerie peuvent avoir sur le caneva

    Returns
    -------
    rescaled_image : image (jpeg, png ... en fonction de l'image d'origine)
    """
    
    # +1 pour éviter d'avoir des trous dans la grille 
    # => arrondi au dessus plutot que au dessous
    taille = int(taille_canevas/facteur) +1
    
    rescaled_image = image.resize((taille, taille))
    return rescaled_image
    


#Tests
"""
if __name__ == "__main__":
    dossier ="C:/Users/solen/OneDrive/Bureau/test_galerie"
    dico = dico_galerie(dossier)
    
    image_proche = image_proche_noir_et_blanc(250, dico)
    image_proche.show()
#def rgb_to_hex(r, g, b):
    #return '#{:02x}{:02x}{:02x}'.format(r, g, b)
"""
