#fonction carreau : place "image" dans le canvas "dessin" (/!\ pas le bon nom) 
#                   aux coordonées NW (x, y)
"""def self.carreau(self, image, x, y):
    im = Image.open(image)
    logo = ImageTk.PhotoImage(im, master=fen)
    dessin.create_image(x, y, anchor = tk.NW, image = logo) #ptet ajouter state = tk.DISABLED, qui devrait rendre l'image inerte au curseur
"""  
    
import tkinter as tk


def test_couleurs(listeRGB):
    """Affiche une série de carré de couleur contenue dans listeRGB 

    Parameters
    ----------
    listeRGB: list of tuple
        Liste de tuples (r,g,b) représentant une couleur.
        r, g et b sont entre 0 et 255.
    Returns
    -------
    None
    """
    coord=[0,0]
    for j in  listeRGB:
        colorhex="#"
        for i in j:
            x=str(hex(i)[2:])
            if len(x)==1:
                x="0"+x
            colorhex+=x
        monCanvas.create_rectangle(coord, coord[0]+50, coord[1]+50 , fill=colorhex)
        if coord[0]==950:
            coord=[0, coord[1]+50]
        else : 
            coord[0]+=50

#listeRGB : liste de triplets RGB sur 8 bits à afficher. tu peux changer son nom plus bas 
listeRGB= [(100, 0, 250), (0,0,0), (250, 250,250)]

fen_princ = tk.Tk()
fen_princ.title("ESSAI AVEC CANVAS")
fen_princ.geometry("3000x1000")
monCanvas = tk.Canvas(fen_princ, width=3000, height=1000, bg='ivory')
test_couleurs(listeRGB)
monCanvas.pack()
fen_princ.mainloop()    
