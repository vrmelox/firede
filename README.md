# Firede - Films recommendations system
This is a simple film recommendation system, without an complicated ML system. 

## Installation
You first need to clone the repository

```Bash
git clone <repository hash>
```

To use this project, you first need to have and virtual environment. To do so
```Bash
python3 -m venv myenv
```

You've then have to activate the virtual environment by running
```Bash
source myenv/bin/activate
```

You've then have to install dependency from the requirements.txt

## Use
Go to the project root and 
```Bash
python3 -m src.main
```
A CLI is launch and you just have to follow the instructions. The last recommendations are always stored in the results.txt. So you can come back and check anytime.

## Results and Analysis

Here are the results from cosine and euclidian for the same movie **The Dark Night**

### Cosine
```
Please enter a movie's name: The Dark Knight
Enter the number of recommendations: 5
Choose a method (cosine/euclidian): cosine

Recommendations for The Dark Knight
1. Arrival 1.53
2. Snowpiercer 1.47
3. Edge of Tomorrow 1.46
4. Guardians of the Galaxy 1.46
5. Children of Men 1.45
```

### Euclidian
Please enter a movie's name: The Dark Knight
Enter the number of recommendations: 5
Choose a method (cosine/euclidian): euclidian

```
Recommendations for The Dark Knight
1. Gladiator 0.1
2. Saving Private Ryan 0.17
3. 1917 0.17
4. The Lord of the Rings: The Fellowship of the Ring 0.2
5. Oldboy 0.2
```

As you can see, euclidian seems to prefer films with the same genre are similar to the one the user like. I see that it works on number. 

The cosine, that seems realistic, do not choose films based on their genre. Because Guardians of the Galaxy takes place in other universe and are mostly futurist. So it made the recommentation based on caracteristic, content of the film.

## Limits and amelioration
This film recommendation system is too simple. It might need some ML to make sure the recommendation are trully deep.
 As limits, the systme do not take into account: 
 1. User's preferences history
 2. Critics and/or notes
 3. Actors and producers
 