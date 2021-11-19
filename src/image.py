from skimage import io
from skimage.transform import resize
import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self):
        """Initialisation d'une image composee d'un tableau numpy 2D vide
        (pixels) et de 2 dimensions (H = height et W = width) mises a 0
        """
        self.pixels = None
        self.H = 0
        self.W = 0
    

    def set_pixels(self, tab_pixels):
        """ Remplissage du tableau pixels de l'image self avec un tableau 2D (tab_pixels)
        et affectation des dimensions de l'image self avec les dimensions 
        du tableau 2D (tab_pixels) 
        """
        self.pixels = tab_pixels
        self.H, self.W = self.pixels.shape


    def load(self, file_name):
        """ Lecture d'un image a partir d'un fichier de nom "file_name"""
        self.pixels = io.imread(file_name)
        self.H,self.W = self.pixels.shape 
        print("lecture image : " + file_name + " (" + str(self.H) + "x" + str(self.W) + ")")


    def display(self, window_name):
        """Affichage a l'ecran d'une image"""
        fig = plt.figure(window_name)
        if (not (self.pixels is None)):
            io.imshow(self.pixels)
            io.show()
        else:
            print("L'image est vide. Rien à afficher")


    #==============================================================================
    # Methode de binarisation
    # 2 parametres :
    #   self : l'image a binariser
    #   S : le seuil de binarisation
    #   on retourne une nouvelle image binarisee
    #==============================================================================
    def binarisation(self, S):
         
        """
        Calcule et retourne l'image binarisee avec un seuil S de l'image self
        return: self
        """
        # preparaton du resultat : creation d'une image vide 
        im_modif = Image()
        # affectation de l'image resultat par un tableau de 0, de meme taille
        # que le tableau de pixels de l'image self
        # les valeurs sont de type uint8 (8bits non signes)
        im_modif.set_pixels(np.zeros((self.H,self.W), dtype=np.uint8))
                                                
        # boucle imbriquees pour parcourir tous les pixels de l'image
        for l in range(self.H):
            for c in range(self.W):
                # modif des pixels d'intensite >= a S
                if self.pixels[l][c] >= S:
                    im_modif.pixels[l][c] = 255
                else :
                    im_modif.pixels[l][c] = 0
        return im_modif


    #==============================================================================
    # Dans une image binaire contenant une forme noire sur un fond blanc
    # la methode 'localisation' permet de limiter l'image au rectangle englobant
    # la forme noire
    # 1 parametre :
    #   self : l'image binaire que l'on veut recadrer
    #   on retourne une nouvelle image recadree
    #==============================================================================
    def localisation(self):
        """
        Calcule et retourne l'image recadree sur le chiffre à identifier
        """
        l_min = self.H-1
        c_min = self.W-1
        l_max = 0
        c_max = 0
        for l in range(self.H):
            for c in range(self.W):
                if self.pixels[l][c] == 0:
                    if l < l_min:
                        l_min = l
                    if l > l_max :
                        l_max = l
                    if c < c_min:
                        c_min = c
                    if c > c_max:
                        c_max = c
        im_bin = Image()
        im_bin.set_pixels(self.pixels[l_min:l_max+1,c_min:c_max+1])
        return im_bin

    #==============================================================================
    # Methode de redimensionnement d'image
    #==============================================================================
    def resize(self, new_H, new_W):
        res_im = Image()
        n = resize(self.pixels,(new_H,new_W),0)
        res_im.set_pixels(np.uint8(n*255))
       
        return res_im
   

    #==============================================================================
    # Methode de mesure de similitude entre l'image self et un modele im
    #==============================================================================
    def similitude(self, im):
        nombre_similitude = 0 
        for x in range(self.H):
            for y in range(self.W):
                if self.pixels[x][y] == im.pixels[x][y]:
                    nombre_similitude += 1
        taux = nombre_similitude/(self.H * self.W)
        return taux            

