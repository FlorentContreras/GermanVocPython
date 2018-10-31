# Fichier de fonctions

import random

def demandeDeMots(mots):
    """ Propose un mot et attend son équivalent traduit """
    
    random.shuffle(mots)            # Permet de mélanger la liste des mots
    motsAjouer = ChoixMode(mots)    # Permet de ne pas jouer les noms si demandé

    print("""
    Raccourcis : 
        q : quitter
        ? : solution
""")

    print("Que voulez-vous faire ? ")

    choixMenu = ""
    choixMenuValide = 0

    while choixMenuValide == 0:
        """ Permet de choisir le sens de traduction choisi """
        choixMenu = input("""
        A : traduire des mots Francais vers l'Allemand. 
        F : traduire des mots Allemand vers le Francais. 
        """)
        print("""
*************************************************************************

""")

        if choixMenu.lower() == "a":
            DemandeMotFrAll(motsAjouer)
            choixMenuValide = 1
        elif choixMenu.lower() == "f":
            DemandeMotAllFr(motsAjouer)
            choixMenuValide = 1
        else:
            print("Choix invalide !")


def ChoixMode(mots):
    """ Cette fonction permet de ne pas prendre en compte les noms """

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


def DemandeMotFrAll(mots):
    """ Cette fonction propose un mot "motFr1" et attend la traduction "motAll1"
        Les commande s et q permettent d'afficher la solution ou de quitter 
        Un compteur de mot s'affiche en début de proposition """
    
    fin = False
    i = 0
    doubleTraduction = [0, 0]

    print("Entrer la traduction du mot : ")

    while not fin and i < len(mots) :

        # On va regarder s'il existe un deuxième mot francaise. 
        # Si c'est le cas, on va choisir l'un des deux. 
        try:
            a = mots[i]["motFr2"]
            motFr = random.choice(["motFr1", "motFr2"])
        except :
            motFr = "motFr1"

        # Demande de la traduction 
        trad = input(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motFr] + " : ")

        # Quitter
        if trad.lower() == "q":
            print(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motFr] + " : " + mots[i]["motAll1"])

            try:
                print(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motFr] + " : " + mots[i]["motAll2"])
            except :
                pass

            fin = True

        # Demander la traduction
        elif trad.lower() == "?":
            print(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motFr] + " : " + mots[i]["motAll1"])

            try:
                print(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motFr] + " : " + mots[i]["motAll2"])
            except :
                pass

            i += 1
            doubleTraduction = [0, 0]

        # Traduction correcte
        elif trad == mots[i]["motAll1"]: 

            try: 
                mots[i]["motAll2"]                  # recherche si une autre traduction existe
                doubleTraduction[0] = 1
            except:
                i += 1

            if doubleTraduction == [1, 1]:
                i +=1
                doubleTraduction = [0, 0]

        # Mauvaise traduction
        else:
            try:
                if trad == mots[i]["motAll2"]:      # recherche si une autre traduction existe
                    doubleTraduction[1] = 1
                else:
                    print("Réessayer !!")

                if doubleTraduction == [1, 1]:
                    i +=1
                    doubleTraduction = [0, 0]

            except:
                print("Réessayer !!")



def DemandeMotAllFr(mots):
    """ Cette fonction propose un mot "motAll1" et attend la traduction "motFr1"
        Les commande s et q permettent d'afficher la solution ou de quitter 
        Un compteur de mot s'affiche en début de proposition """
    
    fin = False
    i = 0

    print("Entrer la traduction du mot : ")

    while not fin and i < len(mots) :

        # On va regarder s'il existe un deuxième mot allemand. 
        # Si c'est le cas, on va choisir l'un des deux. 
        try:
            a = mots[i]["motAll2"]
            motAll = random.choice(["motAll1", "motAll2"])
        except :
            motAll = "motAll1"

        # Demande de la traduction 
        trad = input(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motAll] + " : ")
        
        # Quitter
        if trad.lower() == "q":
            print(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motAll] + " : " + mots[i]["motFr1"])

            try:
                print(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motAll] + " : " + mots[i]["motFr2"])
            except :
                pass

            fin = True

        # Demander la traduction
        elif trad.lower() == "?":
            print(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motAll] + " : " + mots[i]["motFr1"])

            try:
                print(str(i+1) + "/" + str(len(mots)) + "    " + mots[i][motAll] + " : " + mots[i]["motFr2"])
            except :
                pass
                
            i += 1

        # Traduction correcte
        elif trad == mots[i]["motFr1"]: 
            i += 1

        # Mauvaise traduction
        else:
            try:
                if trad == mots[i]["motFr2"]:           # recherche si une autre traduction existe
                    i +=1
                else:
                    print("Réessayer !!")
                    
            except:
                print("Réessayer !!")

