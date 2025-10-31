"""
Module : utils
Description : Fonctions utilitaires pour la gestion de fichiers, JSON, et opérations diverses.
"""

import os, json

PATH_MES_DATAS = "data/bibliotheques_chansons.json" 


def lire_json(chemin_fichier: str) -> dict:
    """
    Lit un fichier JSON et retourne son contenu sous forme de dictionnaire.
    """
    if os.path.exists(chemin_fichier):
        with open(chemin_fichier, 'r', encoding="UTF-8") as file :
            mes_data = json.load(file)
        return mes_data
    else :
        print(chemin_fichier)
        return {"Fichier inexistant"}    


def ecrire_json(chemin_fichier: str, donnees: dict) -> None:
    """
    Écrit des données dans un fichier JSON, avec indentation et encodage UTF-8.
    """
    pass
               

def trouver_bibliotheque(bibliotheques: list, nom: str) -> dict:
    """
    Retourne la bibliothèque correspondant au nom fourni.
    Si aucune bibliothèque ne correspond, retourne None.
    """
    for b in bibliotheques :
        if b["bibliotheque_nom"] == nom :
            return b
        else :
            print("bibiothèque inexistante")


def generer_nouvel_id(bibliotheques: list) -> int:
    """
    Génère un nouvel identifiant unique pour une chanson.
    Parcourt toutes les bibliothèques pour trouver le plus grand ID existant.
    """
    liste_chanson = bibliotheques["chansons"] 
    liste_id =[]
    for c in liste_chanson :
        liste_id.append(c["chanson_id"])
    return max(liste_id) + 1



def formater_affichage_chanson(chanson_obj) -> str:
    """
    Retourne une chaîne de caractères formatée pour afficher une chanson joliment dans la console.
    """
    pass

if __name__ == "__main__" :

    bibiotheques  = lire_json(PATH_MES_DATAS)
    b = bibiotheques["bibliotheques"][0]
    #print(b["chansons"])
    print(generer_nouvel_id(b))
    


    
