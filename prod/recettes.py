from .models import Data
from abc import ABC, abstractmethod
from decimal import Decimal


class Ingredients():
    """Ingredients Classe qui regroupe tous les ingrédients nécessaires pour
    les recettes. Elle permet des opérations basiques comme l'addition.
    """
    
    def __init__(self,
                 FT80:float=0, ST170:float=0, PET80:float=0, RT80:float=0, FPDT:float=0, SarT80:float=0,
                 eau:float=0, sel:float=0, oeufs:float=0, sucre:float=0, beurre:float=0, levain:float=0,
                 raisin:float=0, noisette:float=0, noix:float=0, graines:float=0,
                 levure:float=0,
                 ):
        
        # Farines
        self.FT80 = FT80
        self.ST170 = ST170
        self.PET80 = PET80
        self.RT80 = RT80
        self.SarT80 = SarT80
        self.FPDT = FPDT
        
        # Basiques
        self.eau = eau
        self.sel = sel
        self.oeufs = oeufs
        self.sucre = sucre
        self.beurre = beurre
        self.levain = levain
        
        # Graines et fruits
        self.raisin = raisin
        self.noisettes = noisette
        self.noix = noix
        self.graines = graines
        
        # divers
        self.levure = levure
        
    def __add__(self, other):
        new = {}
        for attr, value in self.__dict__.items():
            new[attr] = value + other.__dict__[attr]
        return Ingredients(**new)
    
    def __repr__(self):
        string_init = "Ingrédients("
        counter = 0
        for ingr, qtt in self.__dict__.items():
            str_add = ""
            if counter > 0 and qtt != 0:
                str_add += ";"

            if qtt != 0:
                str_add += f"{ingr}:{qtt}"
                    
            string_init += str_add
            counter += 1
        string_init +=")"    
        return string_init


def recettes(nom_recette, kg):
    if nom_recette == "T80":
        return Ingredients(
        FT80=0.6*kg,
        sel=0.05*kg,
        eau=0.4*kg,
        levain=0.2*kg,
    )
        
    elif nom_recette == "BuchNat":
        return Ingredients(
        FT80=0.45*kg,
        ST170=0.15*kg,
        sel=0.05*kg,
        eau=0.4*kg,
        levain=0.2*kg,
    )
    
    elif nom_recette == "BuchMG":
        return Ingredients(
        FT80=0.45*kg,
        ST170=0.15*kg,
        sel=0.05*kg,
        eau=0.4*kg,
        levain=0.2*kg,
        graines=0.1*kg,
    )
        
    elif nom_recette == "BuchRN":
        return Ingredients(
        FT80=0.45*kg,
        ST170=0.15*kg,
        sel=0.05*kg,
        eau=0.4*kg,
        levain=0.2*kg,
        raisin=0.1*kg,
        noisette=0.1*kg,
    )
        
    elif nom_recette == "BuchNoix":
        return Ingredients(
        FT80=0.45*kg,
        ST170=0.15*kg,
        sel=0.05*kg,
        eau=0.4*kg,
        levain=0.2*kg,
        noix=0.1*kg,
    )
        
    elif nom_recette == "RizSar":
        return Ingredients(
        FT80=0.6*kg,
        SarT80=0.6*kg,
        sel=0.05*kg,
        eau=0.4*kg,
        levain=0.2*kg,
    )
        
    elif nom_recette == "PetEp":
        return Ingredients(
        PET80=0.6*kg,
        sel=0.05*kg,
        eau=0.4*kg,
        levain=0.2*kg,
    )
        
    elif nom_recette == "Brioche":
        return Ingredients(
        FT80=0.6*kg,
        sel=0.05*kg,
        eau=0.4*kg,
        levain=0.2*kg,
        beurre=0.5*kg,
        sucre=0.2*kg,
        oeufs=0.3*kg,
    )
    
    elif nom_recette == "Cookies":
        return Ingredients(
            FT80=0.6*kg,
            sel=0.05*kg,
            beurre=0.5*kg,
            sucre=0.2*kg,
            oeufs=0.3*kg,
        )
        
    else:
        raise ValueError(f"{nom_recette} n'est pas une recette valide !")
        
        
        



def formatteur_de_recettes(data):
    """formatteur_de_recettes Prend en entrée un objet data qui contient toutes
    les infos sur un four. Rend en sortie une liste de dictionnaires avec tous
    les ingrédients non nuls du four en question.

    Parameters
    ----------
    data : _type_
        _description_

    Returns
    -------
    _type_
        _description_
    """
    # Rend une liste de tout les types de pains dans Data
    liste_de_pains = data._meta.get_fields()[2:]
    
    # Pour chaque pain de quantitté non nulle, fournir une recette
    liste_recettes = {}
    for field in liste_de_pains:
        pain = field.name
        if getattr(data, pain) > 0:
            liste_recettes[pain] = recettes(pain, getattr(data, pain))
            
    # Faire une liste de tous les ingredients non nuls dans le four en question
    liste_ingredient = []
    for type_de_pain in liste_recettes:
        obj = liste_recettes[type_de_pain]
        ingr_supp  = [ingr for ingr, qtt in vars(obj).items() if qtt != 0]
        liste_ingredient.extend(ingr_supp)
        
    # On enlève les ingrédients en double
    liste_ingredient = list(set(liste_ingredient))
    
    # On prépare le tableau de sortie final
    result = {}
    result["headers"] = list(liste_recettes.keys())
    result["headers"].insert(0,"Ingrédients")
    result["rows"] = {}
    for ingr in liste_ingredient:
        qtt = []
        for type_de_pain in liste_recettes:
            ingr_obj = liste_recettes[type_de_pain]
            qtt_ingr = round(getattr(ingr_obj, ingr),2)
            qtt.append(qtt_ingr)
        result["rows"][ingr] = qtt
    
    return result
    