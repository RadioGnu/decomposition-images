# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:31:10 2023

@author: DAMON Coline
"""

import os
import imageGalerie as im
import random


def dico_galerie(dossier):
    """
    Lit le dossier contenant les images de la gallerie et crée un dictionnaire dico_galerie qui regroupe les objet images 
    

    Parameters
    ----------
    dossier : chemin d'acces
        DESCRIPTION.
        chemin d'acces du dossier ou sont stocké les images à utiliser

    Returns
    -------
    dico_galerie : dict
        DESCRIPTION.
        clé  : l'indice de l'image dans le dossier 
        valeur : objet image et tupple valeur moyenne en RGB.
    """
   
    
    liste_images = os.listdir(dossier) #renvoie la liste des chemin d'acces des image du dossier
    dico_galerie = {} #initialisation du dictionaire
    for i in range(len(liste_images)) :
        if i not in dico_galerie :
            acces = dossier + "/" +liste_images[i] #pour permettre d'etre sur de retrouver les image dans le gestionnaire de fichier -> chemin d'acces complet
            image = im.imageGalerie(acces) #création de l'obket image a partir du chemin d'acces
            
            val = image.couleur_moyenne() #utilisation de la methode couleur moyenne de la classe imageGallerie
            dico_galerie[i] = image, val 
            
            
    return dico_galerie 
      
        
    
   
def liste_image_proche(val_moyenne, dico_galerie):
    """
    ssocie à la valeur moyenne de chaque subdivision de l'image initiale toutes les image dont la valeur moyenne est proche

    Parameters
    ----------
    val_moyenne : tuple 
        DESCRIPTION.
        tuple contenant les 3 valeurs RGB moyenne de la subdivision
    dico_galerie : dict
        DESCRIPTION.
        clé  : l'indice de l'image dans le dossier initial
        valeur : objet image et tupple valeur moyenne en RGB.

    Returns
    -------
    couleur_proche : list
        DESCRIPTION.
        liste des image ayant une couleur moyenne proche de la subdivision
    """
    

    couleur_proche = [] #initialisation
    min_couleur = 3*(255**2) #distance la plus elevé a l'image -> necessairement des images plus proche
    image_proche = None
    for image, val in dico_galerie.values(): #parcours du dictionaire
        liste_pixel_select = [] #initialisation de la liste des ecarts
        somme = 0
        for couleur in range (3):
            ecart_couleur = int(abs(val_moyenne[couleur]-val[couleur]))
            somme += ecart_couleur **2
            if ecart_couleur <= 20: #ecart choisi pour avoir une couleur sufisement proche
                liste_pixel_select.append(ecart_couleur)
                if len(liste_pixel_select)==3: #il faut que les trois soit très proche
                    couleur_proche.append(image)
                
            elif somme < min_couleur : 
                image_proche = image
        if len(couleur_proche) == 0 : #si il n'y a pas d'image proche, choisir celle la plus proche 
            couleur_proche.append(image_proche) 
        
    return couleur_proche

def choix_image(val_moyenne, dico_galerie):
    """
    Choix aléatoire de l'image parmis la liste des image de couleurs moyenne proche de celle de la subdivision

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
    dossier ="C:/Users/solen/OneDrive/Bureau/test_galerie"
    dico = dico_galerie(dossier)
             
    val_moy = (110, 110,110)   
    liste = liste_image_proche(val_moy, dico)
    image_finale = choix_image(liste)
    image_finale.image.show()