# Fichier de fonctions

import random


def demandeDeMots(mots):
    """ Propose un mot francais et attend son équivalent allemand"""
    
    melangeLaListe(mots)        # Permet de mélanger la liste des mots
    motsAjouer = ChoixMode(mots)

    print("""
    Raccourcis : 
        q : quitter
        ? : solution
""")

    print("Que voulez-vous faire ? ")
    choixMenu = input("""
 A : traduire des mots Francais vers l'Allemand. 
 F : traduire des mots Allemand vers l'Francais. 
""")
    if choixMenu.lower() == "a":
        DemandeMot(motsAjouer, "motFr1", "motAll1")
    elif choixMenu.lower() == "f":
        DemandeMot(motsAjouer, "motAll1", "motFr1")
    else:
        print("Choix invalide !")


def melangeLaListe(liste):
    """ Prend une liste et la mélange """
    random.shuffle(liste)


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


def DemandeMot(mots, motMontre, motCache):
    """ Cette fonction propose un mot "motMontre" et attend la traduction "motCache"
        Les commande s et q permettent d'afficher la solution ou de quitter 
        Cette fonction est valable pour les traduction dans les deux sens """
    
    fin = False
    i = 0

    print("Entrer la traduction du mot : ")

    while not fin and i < len(mots) :

        trad = input("    " + mots[i][motMontre] + " : ")

        if trad.lower() == "q":     # permet de quitter
            print("    " + mots[i][motMontre] + " : " + mots[i][motCache])
            fin = True

        elif trad.lower() == "?":   # permet d'afficher la solution
            print("    " + mots[i][motMontre] + " : " + mots[i][motCache])
            i += 1

        elif trad == mots[i][motCache]: 
            i += 1

        else:
            print("Réessayer !!")