import math

def normalize_minmax(values):
    """
    Normalise un array de valeurs entre 0 et 1
    
    Paramètres:
    values: numpy array ou liste de nombres
    
    Retour:
    numpy array normalisé entre 0 et 1
    """
    return (values - 0) / (10 - 0)

        # df.action = df.action.apply(normalize_minmax)
        # df.comedy = df.comedy.apply(normalize_minmax)
        # df.romance = df.romance.apply(normalize_minmax)
        # df.scifi = df.scifi.apply(normalize_minmax)
        # df.drama = df.drama.apply(normalize_minmax)

def dot_product(vec1, vec2):
    """
    Calcule le produit scalaire entre deux vecteurs

    Paramètres:
    vec1: numpy array
    vec2: numpy array de même dimension

    Retour:
    float: produit scalaire
    """
    if len(vec1) != len(vec2):
        raise ValueError("Les vecteurs doivent avoir la même dimension")
    if any(math.isnan(x) for x in vec1 + vec2):
        return float('nan')
    return round(math.sqrt(sum([(a * b) for a, b in zip(vec1, vec2)])), 2)

def vector_norm(vec):
    """
    Calcule la norme (longueur) d'un vecteur

    Paramètres:
    vec: numpy array

    Retour:
    float: norme du vecteur
    """
    if any(math.isnan(x) for x in vec):
        return float('nan')
    return math.sqrt(sum([a**2 for a in vec]))

def euclidian_distance(vec1, vec2):
    """
    Calcule la distance euclidienne entre deux vecteurs

    Paramètres:
    vec1: numpy array
    vec2: numpy array de même dimension

    Retour:
    float: distance (0 = identiques, grand = très différents)
    """
    if len(vec1) != len(vec2):
        raise ValueError("Les vecteurs doivent avoir la même dimension")
    if any(math.isnan(x) for x in vec1 + vec2):
        return float('nan')
    return round(math.sqrt(sum([(b - a)**2 for a, b in zip(vec1, vec2)])), 2)