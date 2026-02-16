import pandas as pd
import numpy as np

class MovieRecommender:
    """ Structure de recommendation d'un film"""
    def __init__(self, dataset):
        self.recommandations = {
            "titre": [],
            "score": []
        }
        if not dataset:
            return "Dataset is null"
        if not dataset.endswith(".csv"):
            return "Dataset is in the bad format.\n Should be .csv"
        self.dataset = pd.read_csv(dataset)
        print("Dataset loaded successfully")
