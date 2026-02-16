from .utils import MovieRecommender, recommender

def main():
    Firede = MovieRecommender()
    Firede.normalize()
    Firede.recommend()
    results = Firede.display()

    with open("results.txt", "a") as file:
        file.write(results)
