#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 14:29:33 2023

@author: ecarrondel
"""
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog as fd
import time 

import main as f
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
        
        self.division = tk.IntVar()
        # de 20 a 70 parce que spider plante après 70*70 carreau, et que l'image ne ressemble a rien avant 20*20
        self.slider=tk.Scale(self.racine, orient='horizontal', from_=20, to=70,
                             resolution=1, length=200, variable = self.division,
                             font=("Calibri", 8))
        
        self.boutonlancer=tk.Button(self.racine, text="lancer")
        self.boutonlancer.bind('<Button-1>', self.atribution)
        
        self.boutoncharger=tk.Button(self.racine, text="charger l'image")
        self.boutoncharger.bind('<Button-1>', self.charger)
        
        self.boutongalerie=tk.Button(self.racine, text="charger la galerie")
        self.boutongalerie.bind('<Button-1>', self.changer_galerie)

        self.boutonchoixcouleur = tk.Label(self.racine, text = "Choix de couleur")
        
        self.checkVar = tk.IntVar()
        self.bouton_noir_et_blanc = tk.Checkbutton(self.racine, 
                                                 text = "noir et blanc",onvalue = True, offvalue = False,
                                                 variable = self.checkVar)
        
        self.bouton_noir_et_blanc.bind('<Button-1>', self.choix_couleur)
        self.boutondemo = tk.Button(self.racine, text="lancer version demo")
        self.boutondemo.bind('<Button-1>', self.atribution)

        self.creer_mosaique()
        self.creer_miniature()
        self.positionner()

    def creer_miniature(self):
        """Crée une miniature pour la photo choisie par l'utlisateur
        """
        self.miniature=tk.Canvas(self.racine, background="white", height=200, width=200)
        #self.miniature.create_image(0,0, anchor = tk.NW, image=self.photo)
         
    def creer_mosaique(self):
        """Crée le canevas où on va placer la mosaïque des images
        de la galerie.
        """
        self.mosaique=tk.Canvas(self.racine, background="white", 
                                height=600, width=600, 
                                highlightthickness = 0,
                                borderwidth = 0)
        
    def positionner(self):
        """Positionne tous les widgets de la fenêtre
        """
        self.mosaique.pack(side="left")
        self.miniature.pack(side="top")
        self.slider.pack(side="top")
        self.boutonlancer.pack(side="top")
        self.boutonchoixcouleur.pack(side = "top")
        self.bouton_noir_et_blanc.pack(side="top")
        self.boutondemo.pack(side = "top")
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
        if self.chemin_galerie in [(), '']:
            self.prevenir_annuler()
        else:
            self.galerie = f.dico_galerie(self.chemin_galerie)
        
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
            self.image_originale = iu.imageUtilisateur(chemin)
            self.image_mini = iu.imageUtilisateur(chemin)
            self.image_mini.image=self.image_originale.image.resize((200, 200))
            
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
        
        self.slider.config(troughcolor = couleur)
        self.slider.pack()
        
        self.boutondemo.config(bg = couleur, fg = font_color)
        self.boutongalerie.pack()

    def prevenir_annuler(self):
        """Prévient l'utlisateur qu'il a annulé la sélection
        d'une image
        """
        
        self.message = tk.messagebox.showwarning(title="Annulation",
                                message="Vous avez annulé votre sélection,"
                                        +"pas de nouvelle image chargée."
                                                 )

    
    def atribution(self, event):
        """ Renvoie vers le bon découpage en fonction du bouton appuyé"""
        widget = event.widget
        if widget == self.boutonlancer :
            facteur = self.division.get()
            self.lancer(facteur)
        else :
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
         self.racine.after(int(20-delai)*1000 , self.animation)
         
        
    #Découpage de l'image en la mosaïque
    def lancer(self, facteur):
        """Lance le programme de création de la mosaïque à partir
        de l'image de l'utilisateur.
        """
        
        
        carreauline = self.image_originale.couleur_carreaux(facteur)
        self.liste_logo = []
        
        """ if self.noir_blanc.get() == True : 
            for coord, couleurs in carreauline.items() :
                image = f.choix_image(couleurs, self.galerie)
                
                image_mosaique = image.rescale(600/facteur)
                
                #ATENTION : c'est hyper long comme ca ... faudrait mieux convertir toute la 
                #galerie parce que la il fait plein d'opération plusieur fois pour rien
                image_mosaique = image_mosaique.convert("L")
                x, y = coord
                self.carreau(image_mosaique, x, y)
        
        else : """
        
        for coord, couleurs in carreauline.items() :
            image = f.choix_image(couleurs, self.galerie)

            image_mosaique = image.rescale(600/facteur)
            
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
        
        
    def choix_couleur(self, event):
        if self.checkVar.get() == 1:
            couleur, val_moy = self.image_originale.couleur_moyenne()
            lumiere = val_moy[3]
            f.image_proche_noir_et_blanc(lumiere, self.galerie)

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
