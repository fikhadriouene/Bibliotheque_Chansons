"""
Module : utils
Description : Fonctions utilitaires pour la gestion de fichiers, JSON, et opérations diverses.
"""

import json


def lire_json(chemin_fichier: str) -> dict:
    """
    Lit un fichier JSON et retourne son contenu sous forme de dictionnaire.
    """
    pass


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
    pass


def generer_nouvel_id(bibliotheques: list) -> int:
    """
    Génère un nouvel identifiant unique pour une chanson.
    Parcourt toutes les bibliothèques pour trouver le plus grand ID existant.
    """
    pass


def formater_affichage_chanson(chanson_obj) -> str:
    """
    Retourne une chaîne de caractères formatée pour afficher une chanson joliment dans la console.
    """
    pass
