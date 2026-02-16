from .recommender import MovieRecommender
import argparse
import os
from .utils import cliManager

def main():
    # parser = argparse.ArgumentParser(description="Les arguments pour fonctionner")
    # parser.add_argument("--movie_title", type=str, required=True, help="The name of a movie that you like")
    # parser.add_argument("--n", type=int, default=5, help="Number of recommendation")
    # parser.add_argument("--method", type=str, default="cosine", help="Choose between cosine and euclidian")

    # args = parser.parse_args()
    cliargs = cliManager()
    Firede = MovieRecommender()
    Firede.normalize()
    Firede.recommend(cliargs[0], cliargs[1], cliargs[2])
    results = Firede.display()

    with open("results.txt", "w") as file:
        file.write(results)

if __name__ == "__main__":
    main()