# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:31:10 2023

@author: DAMON Coline
"""
import os

def dico_galerie(self):
    
    """
    Description:
    Lit la liste des chemins des images et crée un dictionnaire dico_galerie qui regroupe les images et ayant pour clé l'indice de l'image et comme valeur son chemin.
    
    """
    
    liste_images = list(self.galerie)
    dico_galerie = {}
    for i in range(len(liste_images)) :
        if i not in dico_galerie :
            image = image_galerie(liste_image[i])
            dico_galerie[i] = image
    self.dico_galerie = dico_galerie  
      
        
    
   
def couleur_proche(self):
    """
    Associe à la valeur moyenne des pixels de l'image initiale toutes les image dont la valeur moyenne est proche

    Returns
    dictionnaire (ou liste?) des images choisies
    None.

    """
    val_moy_init = self.valeur_moyenne
    couleur_proche = []
    for image in self.dico_galerie.keys:
        val_moy_image= image.self.couleur_moyenne() #renvoie le tuple moyen
        for i in range (2):
            ecart_couleur = int(abs(val_moy_init[i]-val_moy_image[i]))
            liste_pixel_select = []
            if ecart_couleur <= 20:
                liste_pixel_select.append(ecart_couleur)
                if len(liste_pixel_select)==3:
                    couleur_proche.append(image)
                
            
            
        
