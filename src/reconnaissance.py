from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    bin_im = image.binarisation(S)
    loc_im = bin_im.localisation()
    
    #modele_0  = liste_modeles[0]
    #W  = modele_0.W
    #H = modele_0.H
    #res = loc_im.resize(H,W)
    
    prop = 0 
    #i_prop = 0 
    
    for i in range(len(liste_modeles)):
        res=loc_im.resize(liste_modeles[i].H,liste_modeles[i].W)
        if res.similitude(liste_modeles[i]) > prop :
            prop = res.similitude(liste_modeles[i])
            i_prop = i
    return i_prop        
            
            
    

