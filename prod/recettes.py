from .models import Data
from abc import ABC, abstractmethod

        
def formatteur_de_recettes(data):    
    # On récupère toutes les recettes du four
    all_recipes = data.recipe_set.all()
    
    # On ne garde que les ingrédients non nuls dans au moins une des recettes du four
    non_zero_ingr = []
    recipes_names = []
    totals = []
    for recipe in all_recipes:
        recipes_names.append(recipe.four_pain) # au passage, les noms de recettes
        totals.append(recipe.total_ingr()) # au passage, les poids totaux
        non_zero_ingr += list(recipe.non_zero())
    non_zero_ingr = set(non_zero_ingr) #remove duplicates
    print(non_zero_ingr)
    print(recipes_names)
    
    # On prépare le tableau de sortie final
    result = {}
    ## Les titres et totaux
    result["headers"] = recipes_names
    result["headers"].insert(0,"Ingrédients")
    result["totals"] = totals
    ## Les lignes 
    result["rows"] = {}   
    for ingr in non_zero_ingr:
        qtt = []
        for recipe in all_recipes:
            qtt.append(round(getattr(recipe,ingr),2))
        result["rows"][ingr] = qtt
                 

    return result