"""
Module : gestion_bibliotheque
Description : Gère le chargement, la manipulation et l'affichage des bibliothèques de chansons.
"""

import Chanson
import utils


class BibliothequeManager:
    """
    Classe principale pour gérer les bibliothèques de chansons.
    """

    def __init__(self, chemin_fichier: str):
        """
        Initialise le gestionnaire avec un chemin vers le fichier JSON contenant les bibliothèques.
        """
        self.chemin = chemin_fichier
        self.bibliotheques = []


    def charger_bibliotheques(self) -> dict:
        """
        Charge les bibliothèques à partir du fichier JSON.
        Utilise une fonction utilitaire de utils.py.
        """
        print(f"charger : {self.chemin}")
        self.bibliotheques = utils.lire_json(self.chemin)


    def sauvegarder_bibliotheques(self) -> None:
        """
        Sauvegarde les bibliothèques actuelles dans le fichier JSON.
        """
        pass


    def afficher_bibliotheques(self) -> None:
        """
        Affiche toutes les bibliothèques et leurs chansons dans la console.
        """
        
        liste_bibliotheques = self.bibliotheques["bibliotheques"]
        for b in liste_bibliotheques :
            print()
            print(f"======== {b["bibliotheque_nom"]} ===========")
            print()
            liste_chansons = b["chansons"]
            for c in liste_chansons :
                print(f"{c["chanson_titre"]} -- {c["chanson_chanteur"]}" )



    def ajouter_chanson(self, nom_bibliotheque: str, chanson: Chanson.Chanson) -> None:
        """
        Ajoute une chanson à une bibliothèque donnée.
        Si la bibliothèque n'existe pas, elle peut être créée
        """
        biblio = utils.trouver_bibliotheque(self.bibliotheques,nom_bibliotheque)
        biblio["chansons"].append(chanson.chanson_to_dict())
        
        

    def supprimer_chanson(self, nom_bibliotheque: str, chanson_id: int) -> None:
        """
        Supprime une chanson d'une bibliothèque donnée en fonction de son ID.
        """
        pass

    def rechercher_chanson(self, mot_cle: str) -> list:
        """
        Recherche des chansons contenant le mot clé (dans le titre ou le chanteur).
        Retourne une liste d’objets Chanson correspondants.
        """
        pass

    def filtrer_par_categorie(self, categorie: str) -> list:
        """
        Retourne une liste de chansons appartenant à une catégorie donnée.
        """
        pass

    def trier_par_score(self, ordre: str = "desc") -> list:
        """
        Trie toutes les chansons (toutes bibliothèques confondues) selon leur score.
        ordre : "asc" ou "desc".
        """
        pass


if __name__ == "__main__" :
    bm = BibliothequeManager(utils.PATH_MES_DATAS)
    bm.charger_bibliotheques()
    chanson = Chanson.Chanson(5,"titre1","chanteur1",1,4.2)
    bm.ajouter_chanson("Bibliothèque Pop & Rock", chanson)
    bm.afficher_bibliotheques()


