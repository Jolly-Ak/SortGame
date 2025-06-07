from interface_graphique_bs import * 
from classes_bs import *
from interface_textuelle_bs import *



def __main__():
    """Fonction principale du programme pour lancer le jeu"""
    global jeu_instance
    print('bienvenue dans le jeu des tubes et des balles')
    print("Vous pouvez opter pour l'interface graphique",
           "l'interface textuelle, ou mettre fin au jeu.")
    choix = input(' g / t / f : ')
    if choix == 'g':
        interface_graphique()
        __main__()
    elif choix == 't':  
        interface_textuelle()
        __main__()
    elif choix == 'f':
        print('au revoir')
    else:
        print('erreur')
        __main__()
    
__main__()