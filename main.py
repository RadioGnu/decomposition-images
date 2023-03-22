# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:31:10 2023

@author: DAMON Coline
"""
import os
import imageGalerie as im

def dico_galerie(dossier):
    
    """
    Description:
    Lit la liste des chemins des images et crée un dictionnaire dico_galerie qui regroupe les images et ayant pour clé l'indice de l'image et comme valeur son chemin.
    
    """
    
    liste_images = os.listdir(dossier)
    dico_galerie = {}
    for i in range(len(liste_images)) :
        if i not in dico_galerie :
            acces = dossier + "/" +liste_images[i]
            image = im.imageGalerie(acces)
            val = image.couleur_moyenne()
            dico_galerie[i] = image, val
            
    return dico_galerie 
      
        
    
   
def couleur_proche(val_moyenne, dico_galerie):
    """
    Associe à la valeur moyenne de chaque pixel de l'image initiale toutes les image dont la valeur moyenne est proche

    Returns
    dictionnaire (ou liste?) des images choisies
    None.

    """
    couleur_proche = []
    for image, val in dico_galerie.values():
        liste_pixel_select = []
        for couleur in range (3):
            ecart_couleur = int(abs(val_moyenne[couleur]-val[couleur]))
            
            if ecart_couleur <= 20:
                liste_pixel_select.append(ecart_couleur)
                if len(liste_pixel_select)==3:
                    couleur_proche.append(image)
    return couleur_proche
                    
dossier = "C:/Users/DAMON Coline/Documents/GitHub/decomposition-images/gallerie"
dico = dico_galerie(dossier)         
val_moy = (12, 9,10)   
print( couleur_proche(val_moy, dico) )        
            
        
