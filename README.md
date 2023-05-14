# Decomposition d'images
Projet d'algorithmique 2A INSA Lyon.
Le programme découpe une image en plusieurs carreaux, calcule la couleur
moyenne de chaque carreau, et l'associe à une image choisie dans une galerie.
Puis, il affiche les images choisies à la place des carreaux.

# Lancer le programme
Nous vous conseillons d'utiliser venv, comme expliqué sur le site suivant :
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment.

On peut ensuite installer les dépendances avec pip:
```
pip install -r requirements.txt
```

Pour lancer le programme:
```
python src/interface-graphique.py
```

Une fois le programme lancé, il faut choisir une image avec le bouton
`charger image`. Ensuite, il faut charger une galerie d'images
avec le bouton `charger galerie`. Vous pouvez utiliser votre
propre galerie - auquel cas vous devrez attendre quelques
minutes - ou vous pouvez utiliser la galerie par défaut,
stockée dans `src/galerie`.

# Auteurs
Emile CARRON, Coline DAMON, Paul GEORGES, Solenn MINGAT
