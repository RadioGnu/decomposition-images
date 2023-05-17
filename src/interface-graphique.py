#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:29:33 2023

@author: ecarrondel
"""
from random import randint
import time 

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog as fd

import fonctions as f
import imageUtilisateur as iu



class interface:
    """Interface graphique de l'application
    """

    #initialisation de la fenêtre
    def __init__(self):
        """Création des boutons de l'application, ainsi que des
        informations principales.
        """
        self.racine = tk.Tk()
        self.racine.geometry("800x600")
        self.racine.title("DECOUPIMAGE 2000")
        self.liste_logo = []
        self.parcours_multiple = 0
        self.image_originale = None
        self.galerie = None
       
        #ATTENTION : le slider est adapté à la taille du caneva. 
        #Il est possible de la modifier mais il faudra recalibrer le slider en conséquence
        self.taille_caneva = 600
        
        
        
        self.division = tk.IntVar()
        #Le slider va de 20 a 70 parce que en-dessous de 20*20,
        #l'image n'a pas trop de sens,
        #et au-delà de 70, le programme peut planter (sur spyder)
        self.slider=tk.Scale(self.racine, orient='horizontal', from_=20, to=70,
                             resolution=1, length=200, variable = self.division,
                             font=("Calibri", 8))
        
        self.boutonlancer=tk.Button(self.racine, text="lancer")
        self.boutonlancer.bind('<Button-1>', self.attribution)
        
        self.boutoncharger=tk.Button(self.racine, text="charger l'image")
        self.boutoncharger.bind('<Button-1>', self.charger)
        
        self.boutongalerie=tk.Button(self.racine, text="charger la galerie")
        self.boutongalerie.bind('<Button-1>', self.changer_galerie)
        
        self.boutonenregistrer =tk.Button(self.racine, text="Enregistrer l'image")
        self.boutonenregistrer.bind('<Button-1>', self.enregistrer)

        self.labelchoixmodes = tk.Label(self.racine, text = "Choix des modes")
        
        self.noir_blanc = tk.IntVar()
        self.bouton_noir_et_blanc = tk.Checkbutton(self.racine, 
                                                 text = "noir et blanc",onvalue = True, offvalue = False,
                                                 variable = self.noir_blanc)
        
        
        self.DemoVar = tk.IntVar()
        self.boutondemo = tk.Checkbutton(self.racine, 
                                                 text="version demo", onvalue = True, offvalue = False,
                                                 variable = self.DemoVar)

        self.creer_mosaique()
        self.creer_miniature()
        self.positionner()

    def creer_miniature(self):
        """Crée une miniature pour la photo choisie par l'utlisateur
        """
        self.miniature=tk.Canvas(self.racine, background="white", height=200, width=200)
        #self.miniature.create_image(0,0, anchor = tk.NW, image=self.photo)
         
    def creer_mosaique(self):
        """Crée le canevas où l'on va placer la mosaïque des images
        de la galerie.
        """
        self.mosaique=tk.Canvas(self.racine, background="white", 
                                height=self.taille_caneva, width=self.taille_caneva, 
                                highlightthickness = 0,
                                borderwidth = 0)
        
    def positionner(self):
        """Positionne tous les widgets de la fenêtre
        """
        self.mosaique.pack(side="left")
        self.miniature.pack(side="top")
        self.slider.pack(side="top")
        self.boutonlancer.pack(side="top")
        self.labelchoixmodes.pack(side = "top")
        self.bouton_noir_et_blanc.pack(side="top")
        self.boutondemo.pack(side = "top")
        self.boutonenregistrer.pack(side="top")
        self.boutoncharger.pack(side="bottom")
        self.boutongalerie.pack(side="bottom")
        

    #Chargements de la galerie et de l'image de l'utilisateur
    def changer_galerie(self, event):
        """Charge une galerie stocké dans le dossier demandé 
        par l'utilisateur.
        """
        etiquette = tk.Label(self.racine, text="chargement...", bg = 'red')
        etiquette.place(x = 250, y = 250, height=100, width=100)
        
        self.chemin_galerie = fd.askdirectory()
        #Si l'utilisateur annule, le chemin renvoyé fait partie
        #de la liste dans le test
        if self.chemin_galerie in ['', ()]:
            self.prevenir_annuler()
            etiquette.destroy()

        else:
            self.galerie = f.dico_galerie(self.chemin_galerie, self.taille_caneva)
        
        etiquette.destroy()
        
        
    def charger(self,event):
        """Charge l'image demandée par l'utilisateur, la place dans
        la miniature, et change la couleur de l'interface.
        """
        chemin = fd.askopenfilename()
        #Si l'utilisateur annule, le chemin renvoyé fait partie
        #de la liste dans le test
        if chemin in ['', ()]:
            self.prevenir_annuler()
        else:
            self.miniature.delete("all")
            self.image_originale = iu.imageUtilisateur(chemin, self.taille_caneva)
            self.image_mini = iu.imageUtilisateur(chemin, self.taille_caneva)
            self.image_mini.image = self.image_originale.image.resize((200, 200))
            
            self.IM = ImageTk.PhotoImage(self.image_mini.image)
            self.miniature.create_image(0, 0, anchor = tk.NW, image = self.IM)
            self.adapter_couleurs()
            
    def adapter_couleurs(self):
        """Change les couleurs de l'interface en la couleur moyenne
        de l'image choisie.
        """
        couleur, lumiere, font_color = self.image_originale.couleur_moyenne()
        self.boutonlancer.config(bg = couleur, fg=font_color)
        self.boutonlancer.pack()
        
        self.boutoncharger.config(bg = couleur, fg = font_color)
        self.boutoncharger.pack()
        
        self.boutongalerie.config(bg = couleur, fg = font_color)
        self.boutongalerie.pack()
        
        self.boutonenregistrer.config(bg = couleur, fg = font_color)
        self.boutongalerie.pack()
        
        self.slider.config(troughcolor = couleur)
        self.slider.pack()
        

    def prevenir_annuler(self):
        """Prévient l'utlisateur qu'il a annulé la sélection
        d'une image
        """
        
        self.message = tk.messagebox.showwarning(title="Annulation",
                                message="Vous avez annulé votre sélection,"
                                        +"pas de nouvelle image ou galerie chargée."
                                                 )

    
    def attribution(self, event):
        """ Renvoie vers le bon découpage en fonction du bouton appuyé"""
        
        if self.image_originale == None or self.galerie == None:
            self.message = tk.messagebox.showwarning(title="Erreur",
                                    message="Vous n'avez pas choisie d'image et/ou de galerie. \n"
                                            +"Veuillez charger votre image et votre galerie pour lancer le programe")
        
        else:
            if self.DemoVar.get() == 0:
                facteur = self.division.get()
                self.lancer(facteur)
            else :
                #reinitialise le parcours si l'animation est relancée
                self.parcours_multiple = 0
                self.animation()
            
    def animation(self):
         """ Permet d'animer le caneva comme un diaporama en découpage l'image en multiple de 2 
         de plus en plus grand, puis en recommencant à 2 début """
         start = time.time()
         liste_multiple = [2, 4, 8, 16, 32, 64]
         facteur = liste_multiple[self.parcours_multiple]
         self.parcours_multiple += 1
         if self.parcours_multiple == len(liste_multiple):
             self.parcours_multiple = 0
         
         self.lancer(facteur)
         delai = time.time() - start
         if self.DemoVar.get() == 1:
             self.racine.after(int(20-delai)*1000 , self.animation)
        
         
        
    #Découpage de l'image en la mosaïque
    def lancer(self, facteur):
        """Lance le programme de création de la mosaïque à partir
        de l'image de l'utilisateur.
        """
        
        liste_carreaux = self.image_originale.couleur_carreaux(facteur)

        self.liste_logo = []
        
        #mettre le if ... else... avant les boucles permet de ne faire qu'une fois le test
        if self.noir_blanc.get() == 1:
            for coord, couleurs in liste_carreaux.items():
                R, V, B = couleurs
                lum = 0.299 *R + 0.587 * V + 0.114 * B
                
                image = f.image_proche_noir_et_blanc(lum, self.galerie)
                
                image_mosaique = f.rescale(image, facteur, self.taille_caneva)
                
                x, y = coord
                self.carreau(image_mosaique, x, y)
        
        else: 
            for coord, couleurs in liste_carreaux.items():
                image = f.choix_image(couleurs, self.galerie)
    
                image_mosaique = f.rescale(image.image, facteur, self.taille_caneva)
                
                x, y = coord
                self.carreau(image_mosaique, x, y)
            
            

    def carreau(self, im, x, y):
        """Place la photo "im" en (x,y)

        Parameters:
        -----------
        im: Image PIL qui a été choisie dans la galerie

        x, y: Coordonnées où on veut placer l'image
            Coin nord-ouest

        Returns:
        --------
        None
        """
        
        self.logo = ImageTk.PhotoImage(image= im , master=self.racine)
        self.liste_logo.append(self.logo)
        #ptet ajouter state = tk.DISABLED, qui devrait rendre l'image inerte au curseur
        self.mosaique.create_image(x, y, anchor = tk.NW, image = self.logo) 
    
    #Enregistrement optionnel
    def enregistrer(self, event) :
        """Enregistre le canvas en un fichier postcript de nom aléatoire.
        """
        nb = randint(0, 10000)
        self.mosaique.postscript(file = "../" + f"image{nb}.ps")

# Lancement de l'interface
app=interface()
app.racine.mainloop()
