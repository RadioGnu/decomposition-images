#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:29:33 2023

@author: ecarrondel
"""
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog as fd
import imageUtilisateur as iu
import main as f

class interface:

    #iniit : les trucs qui seront forcément là, et auxquelles on touche pas : Boutons, slider( variable self.division).
    def __init__(self):
        self.racine = tk.Tk()
        self.racine.geometry("800x600")
        self.racine.title("DECOUPIMAGE 20000")
        self.division = tk.IntVar()
        self.slider=tk.Scale(self.racine, orient='horizontal', from_=1, to=100 ,resolution=1, length=200, variable = self.division, font=("Calibri", 8))
        
        self.boutonlancer=tk.Button(self.racine, text="lancer")
        self.boutonlancer.bind('<Button-1>', self.lancer)
        
        self.boutoncharger=tk.Button(self.racine, text="charger l'image")
        self.boutoncharger.bind('<Button-1>', self.charger)
        
        self.boutongalerie=tk.Button(self.racine, text="changer de galerie")
        self.boutongalerie.bind('<Button-1>', self.changer_galerie)

        self.boutoncouleur = tk.Checkbutton(self.racine, text="couleur")
        self.bouton_black_white = tk.Checkbutton(self.racine, text = "noir et blanc")

        self.creer_mosaique()
        self.creer_mignature()
        self.positionner()
        self.choix_couleur()


    #peitte photo : canvas pour afficher l'image d'origine
    def creer_mignature(self):
        self.mignature=tk.Canvas(self.racine, background="white", height=200, width=200)
        #self.mignature.create_image(0,0, anchor = tk.NW, image=self.photo)
        
        
    #Grande photo composée : canvas pour la grand photo,
    #qui se clear et se reforme pour la nouvelle photo quand on l'appelle.
    def creer_mosaique(self):
        self.mosaique=tk.Canvas(self.racine, background="white",  height=600, width=600)

    
        
    def positionner(self):
        self.mosaique.pack(side="left")
        self.mignature.pack(side="top")
        self.slider.pack(side="top")
        self.boutonlancer.pack(side="top")
        self.boutoncharger.pack(side="bottom")
        self.boutongalerie.pack(side="bottom")

    def changer_galerie(self, event):
        etiquette = tk.Label(self.racine, text="chargement...", bg = 'red')
        etiquette.place(x = 250, y = 250, height=100, width=100)
        
        chemin = fd.askdirectory()
        self.galerie = f.dico_galerie(chemin)
        
        etiquette.destroy()
        
        
    def lancer(self, event):
        facteur = self.division.get()
        carreauline = self.image_originale.couleur_moyenne(facteur)
        
        for coord, couleurs in carreauline.items() :
            image = f.choix_image(couleurs, self.galerie)
            image.rescale(600/facteur)
            x, y = coord
            self.carreau(image, x, y)
        
        
    def charger(self,event):
        self.mignature.delete("all")
        chemin = fd.askopenfilename()
        self.image_originale = iu.imageUtilisateur(chemin)
        self.image_mini = iu.imageUtilisateur(chemin)
        self.image_mini.image=self.image_originale.image.resize((200, 200))
        
        self.IM = ImageTk.PhotoImage(self.image_mini.image)
        self.mignature.create_image(0, 0, anchor = tk.NW, image = self.IM)

# carreau : place la photo "image" en (x,y) 
    def carreau(self, image, x, y):
        im = Image.open(image)
        logo = ImageTk.PhotoImage(im, master=self.racine)
        self.mosaique.create_image(x, y, anchor = tk.NW, image = logo) #ptet ajouter state = tk.DISABLED, qui devrait rendre l'image inerte au curseur

        
    def choix_couleur(self):
        pass

app=interface()
app.racine.mainloop()

"""     
image = Image.open("gallerie/1.jpg") 
photo = ImageTk.PhotoImage(image) 

canvas = tk.Canvas(root, width = image.size[0], height = image.size[1]) 
canvas.create_image(0,0, anchor = tk.NW, image=photo)
canvas.pack() 
root.mainloop()
"""