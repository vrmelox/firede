import pandas as pd
import numpy as np
from .utils import cosine_similarity, euclidian_distance

class MovieRecommender:
    """ Structure de recommendation d'un film"""
    def __init__(self):
        self.recommandations = {
            "titre": [],
            "score": []
        }
        self.dataset = pd.read_csv("../data.csv")
        print("Dataset loaded successfully")
        
    def film_vectors(row):
        return row.iloc[[1, 2, 3, 4, 5]].to_numpy()

    def recommend(self, movie_title, n=5, method='cosine'):
        if method not in ['cosine', 'euclidian']:
            return "Choose between cosine, euclidian"
        """
        Recommande les N films les plus similaires à un film donné

        Paramètres:
        movie_title: str - titre du film de référence
        df: DataFrame - dataset des films
        n: int - nombre de recommandations
        method: str - 'cosine' ou 'euclidean'

        Retour:
        DataFrame avec les N films recommandés et leur score de similarité
        """
        findfilm = self.dataset[self.dataset.title == movie_title]
        if len(findfilm) == 0 :
            return "Film inexistant"
        ed = findfilm.iloc[:, [1, 2,3,4,5]].iloc[0].to_numpy()
        if method == 'cosine':
            scores = self.dataset.apply(lambda row: cosine_similarity(ed, self.film_vectors(row)), axis=1)
            self.recommandations['title'] = self.dataset['title']
            self.recommandations['score'] = scores
            reco_df = pd.DataFrame(self.recommandations)
            reco_df = reco_df.sort_values(by='score', ascending=False)
            return reco_df.head(n)
        if method == 'euclidian':
            scores = self.dataset.apply(lambda row: euclidian_distance(ed, self.film_vectors(row)), axis=1)
            self.recommandations['title'] = self.dataset['title']
            self.recommandations['score'] = scores
            reco_df = pd.DataFrame(self.recommandations)
            reco_df = reco_df.sort_values(by='score')
            return reco_df.head(n)