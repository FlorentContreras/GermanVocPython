# Fichier de fonctions

import random


def melangeLaListe(liste):
    """ Prend une liste et la mélange """
    random.shuffle(liste)


def demandeDeMots(mots):
    """ Propose un mot francais et attend son équivalent allemand"""
    
    melangeLaListe(mots)        # Permet de mélanger la liste des mots
    motsAjouer = ChoixMode(mots)
    DemandeMot(motsAjouer)



def ChoixMode(mots):
    """ Cette fonction permet de ne pas prendre en compte les noms"""

    choix = input("Jouer aussi les noms (oui/non) ? ")

    if choix.lower() == "oui":
        listeSelectionnee = mots
        
    else:
        listeSelectionnee = []

        for monDictionnaire in mots :

            monDictionnaire = dict(monDictionnaire)

            try:
                if monDictionnaire["typ"] != "nom":
                    listeSelectionnee.append(monDictionnaire)

            except KeyError:
                listeSelectionnee.append(monDictionnaire)

    return listeSelectionnee


def DemandeMot(mots):
    """ Cette fonction propose un mot francais et attend la traduction allemande
        Les commande s et q permettent d'afficher la solution ou de quitter"""
    
    print("""
Raccourcis : 
    q : quitter
    s : solution
""")

    fin = False
    i = 0

    while not fin and i < len(mots) :
        trad = input("Entrer la traduction du mot " + mots[i]["motFr1"] + " : ")

        if trad.lower() == "q":     # permet de quitter
            print(mots[i]["motAll1"])
            fin = True

        elif trad.lower() == "s":   # permet d'afficher la solution
            print(mots[i]["motAll1"])
            i += 1

        elif trad == mots[i]["motAll1"]: 
            print("Bravo !!")
            i += 1

        else:
            print("Réssayer !!")

        

