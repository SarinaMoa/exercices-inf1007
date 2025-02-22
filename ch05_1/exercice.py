#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        return number *-1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    name = []
    for pre in prefixes:
        name.append(pre+suffixe)
    return name


def prime_integer_summation() -> int:

    return 0


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    for i in range(1,11):
        if i==5:
            continue
        print(i)

"""Vérifier si un groupe est acceptable selon l'âge de plusieurs personnes faisant partie de plusieurs groupes. Vous devez retourner une liste booléenne. Les conditions d'acceptation sont les suivantes:
    - Critère de taille: Si le groupe possède plus que 10 membres ou 3 membres et moins, il n'est pas acceptable
    - Critère d'âge: Si au moins un membre du groupe est mineur, le groupe n'est pas acceptable
    - Critère d'âge: Si un membre du groupe est plus vieux que 70 ans et qu'un autre membre du groupe à exactement 50 ans, le groupe n'est pas acceptable
    - Critère d'âge: Si au moins un membre du groupe à exactement 25 ans, alors le groupe est acceptable peut-importe les autres critères d'âges
"""

def verify_ages(groups: List[List[int]]) -> List[bool]:
    taille = 3 <= len(groups) <= 10
  
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
