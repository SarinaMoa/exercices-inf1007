#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

"""Soit un prénom composé (avec un trait d’union) passé en paramètre (exemple « jean-luc »). Il faut extraire le premier prénom (exemple « jean » pour « jean-luc ») puis le mettre dans la phrase « Bonjour *PremierPrénom* » (exemple « Bonjour Jean »). La première lettre du prénom doit être en majuscule (même si le paramètre est en minuscule). Indice : Les chaînes de caractères possèdent des fonctions de recherche et de séparation."""
def get_first_part_of_name(name):
	prenom = name.split('-')[0]
	cap = prenom[0].upper() + prenom[1:].lower()

	return "Bonjour," + prenom

def get_random_sentence(animals, adjectives, fruits):
	return ""

def format_date(year, month, day, hours, minutes, seconds):
	return ""

def encrypt(text, shift):
	return ""

def decrypt(encrypted_text, shift):
	return ""


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))

	print(format_date(1970, 1, 12, 12, 3, 45.6789))

	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
