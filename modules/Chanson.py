
class Chanson :
    def __init__(self, chanson_id : int, chanson_titre : str, chanson_chanteur : str, chanson_categorie : int, chanson_score : float) :
            self.chanson_id = chanson_id
            self.chanson_titre = chanson_titre
            self.chanson_chanteur = chanson_chanteur
            self.chanson_categorie = chanson_categorie
            self.chanson_score = chanson_score
    
    def chanson_to_dict(self) -> dict :
          d = {}
          d["chanson_id"] = self.chanson_id
          d["chanson_titre"] = self.chanson_titre
          d["chanson_chanteur"] = self.chanson_chanteur
          d["chanson_categorie"] = self.chanson_categorie
          d["chanson_score"] = self.chanson_score

          return d

