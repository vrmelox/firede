from .recommender import MovieRecommender
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Les arguments pour fonctionner")
    parser.add_argument("--movie_title", type=str, required=True, help="The name of a movie that you like")
    parser.add_argument("--n", type=int, default=5, help="Number of recommendation")
    parser.add_argument("--method", type=str, default="cosine", help="Choose between cosine and euclidian")

    args = parser.parse_args()
    Firede = MovieRecommender()
    Firede.normalize()
    filmslit = Firede.recommend(args.movie_title, args.n, args.method)
    results = Firede.display()

    with open("results.txt", "w") as file:
        file.write(results)
    print("Results ok !")

if __name__ == "__main__":
    main()