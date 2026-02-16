from .utils import dot_product, vector_norm

def cosine_similarity(vec1, vec2):
    """
    Calcule la similarité cosinus entre deux vecteurs

    Paramètres:
    vec1: numpy array
    vec2: numpy array de même dimension

    Retour:
    """
    docti = dot_product(vec1, vec2)
    norm_vec1 = vector_norm(vec1)
    norm_vec2 = vector_norm(vec2)
    return round(docti / norm_vec1 * norm_vec2, 2)
