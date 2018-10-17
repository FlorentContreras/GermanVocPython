# Fichier de fonctions

import random


def melangeLaListe(liste):
	""" Prend une liste et la mélange """
	random.shuffle(liste)


def demandeDeMots(mots):
	""" Propose un mot francais et attend son équivalent allemand"""
	
	melangeLaListe(mots)		# Permet de mélanger la liste des mots

	print("""
Raccourcis : 
	q : quitter
	s : solution
""")

	fin = False
	i = 0

	while not fin and i < len(mots) :
		trad = input("Entrer la traduction du mot " + mots[i]["motFr1"] + " : ")
		if trad == "q": 
			fin = True

		elif trad == "s":
			print(mots[i]["motAll1"])
			i += 1

		elif trad == mots[i]["motAll1"]: 
			print("Bravo !!")
			i += 1

		else:
			print("Réssayer !!")

		

