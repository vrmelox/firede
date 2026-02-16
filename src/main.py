from .recommender import MovieRecommender

def main():
    Firede = MovieRecommender()
    Firede.normalize()
    filmslit = Firede.recommend("The Dark Knight", 5, "euclidian")
    results = Firede.display()

    with open("results.txt", "w") as file:
        file.write(results)
    print("Results ok !")

if __name__ == "__main__":
    main()