# Decomposition d'images
Projet d'algorithmique 2A INSA Lyon.
Le programme découpe une image en plusieurs carreaux, calcule la couleur
moyenne de chaque carreau, et l'associe à une image choisie dans une galerie.
Puis, il affiche les images choisies à la place des carreaux.

# Installation
Nous vous conseillons d'utiliser venv, comme expliqué sur le site suivant :
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment.

On peut ensuite installer les dépendances avec pip:
```
pip install -r requirements.txt
```

# Utilisation
Pour lancer le programme:
```
python src/interface-graphique.py
```

## Format des images
Le programme reconnait n'importe quelle image que PIL reconnait,
consulter la page suivante pour plus d'informations:
https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html

## Charger une galerie
Une galerie est fournie avec le programme dans le fichier `src`, qui est déjà
chargée. Elle se chargera donc très rapidement.
Il est possible d'y rajouter des images.

Il est également possible d'utiliser une autre galerie. Pour cela, il faut 
s'assurer que le dossier contient **uniquement** des images (voir format). 
Le premier chargement peut prendre un certain temps, les utilisations 
suivantes seront plus rapide.

## Charger une image
Nous vous conseillons de choisir une image de plus de 100*100 pixels,
pour éviter qu'elle apparaisse floue.
Les pixels transparents d'une image PNG seront lus comme des pixels noirs.

## Lancer
Pour lancer, choisissez le nombre d'images sur un côté avec le slider.
Vous pouvez ensuite choisir entre le mode noir et blanc, le mode
couleur ou la démonstration.

La démonstration découpera l'image en puissances de 2 successives.
L'exécution est assez lente, patientez 20 secondes entre chaque
étape.
##Enregistrer
L'image est enregistrée au format postscript (.ps) que vous pouvez
convertir avec des logiciels de conversion, comme par exemple ce
site web: https://convertio.co/ps-jpg/
# Options
## Changer la dimensions du canevas
Si vous souhaitez changer la dimension du canevas pour avoir une image
découpée plus grande, il suffit de changer la valeur de l'attribut 
`self.taille_canevas` dans le fichier `interface_graphique.py`. 

Attention, selon les performances de votre ordinateur, il sera 
peut être nécessaire de diminuer le nombre maximal d'images par côté.
Pour 600 par 600, la limite sur nos ordinateurs est de 70 par exemple.

# Fichiers
## Racine
- `README.md`
    Le fichier que vous lisez ;)
- `requirements.txt`
    Fichier contenant les dépendances du projet.
- `LICENSE`
    License du projet (MIT).
## Dossier `src`
- `interface-graphique.py`
    Application principale du projet, lance une interface graphique
    qui gère l'interface.
- `imageGalerie.py`
    Classe imageGalerie, pour gérer les images de la galerie.
- `imageUtilisateur.py`
    Classe imageUtilisateur, pour faire les calculs sur
    les images de l'utilisateur.
- `fonctions.py`
    Fichier contenant les fonctions d'interaction avec les fichiers.
- `galerie`
    La galerie de base. Le fichier `valeur_moyenne.csv` contient les
    valeurs moyennes des images.
- `testcouleurs.py`
    Fichier utilisé pour constituer la galerie, en testant les couleurs.

# Auteurs
Emile CARRON, Coline DAMON, Paul GEORGES, Solenn MINGAT
