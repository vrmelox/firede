from .recommender import MovieRecommender

def main():
    Firede = MovieRecommender()
    Firede.normalize()
    Firede.recommend()
    results = Firede.display()

    with open("results.txt", "a") as file:
        file.write(results)

if __name__ == "__main__":
    main()