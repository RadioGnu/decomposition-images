# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:31:10 2023

@author: DAMON Coline
"""
import os
import imageGalerie as im

def dico_galerie(dossier):
    
    """
    Lit la liste des chemins des images et crée un dictionnaire dico_galerie 
    qui regroupe les images et ayant pour clé l'indice de l'image et comme valeur son chemin.
    
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
      

def serialiser(dico_galerie):
    """
    Stocke le dictionnaire contenant les valeurs moyennes pour chaque image
    dans un fichier texte contenu dans le fichier de la galerie.

    Pour éviter de recalculer une fois que la gallerie est mise en place.
    """
    with open('galerie/valeur_moyenne.csv', 'w') as file:
        for (k,v) in dico_galerie.items():
            chemin = k.chemin
            file.write(f'{chemin},{v}')


def deserialiser(dossier):
    """
    Trouve le dico gallerie à partir du fichier texte
    """
    #ajouter import csv avant
    with open('galerie/valeur_moyenne.csv', 'r') as file:
        lecteur = csv.reader(file, delimiter=',')
        for line in lecteur:
            acces = dossier + '/' + row[0]
            image = im.ImageGalerie(acces)
            dico_galerie[image] = row[1]
    
   
def couleur_proche(val_moyenne, dico_galerie):
    """
    Associe à la valeur moyenne de chaque pixel de l'image initiale toutes les
    image dont la valeur moyenne est proche

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

#Tests
if __name__ == "__main__":
    dossier = "C:/Users/DAMON Coline/Documents/GitHub/decomposition-images/gallerie"
    dico = dico_galerie(dossier)         
    val_moy = (12, 9,10)   
    print( couleur_proche(val_moy, dico) )
