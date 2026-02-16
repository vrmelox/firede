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

def cliManager():
    cliargs = []
    print("=== Film recommendation system ===\nYou can stop anytime with Crtl + C")
    movie_title = input("Please enter a movie's name: ")
    if len(movie_title) <= 0 or not isinstance(movie_title, str):
        raise TypeError("Provide a real name")
    cliargs.append(movie_title)
    n = int(input("Enter the number of recommendations: "))
    if not isinstance(n, int):
        raise TypeError("Provide a number")
    cliargs.append(n)
    method = input("Choose a method (cosine/euclidian): ")
    if len(method) <= 0 or not isinstance(movie_title, str):
        raise TypeError("Choose a method")
    if method not in ["cosine", "euclidian"]:
        raise TypeError("Choose a real method between cosine and euclidian")
    cliargs.append(method)
    return cliargs