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
1. The Dark Knight 1.0
2. Gladiator 0.9971
3. 1917 0.9932
4. Saving Private Ryan 0.9922
5. Dunkirk 0.9913
```

The scores are very close to 1.0 (0.99+), which indicates that these movies 
have **almost identical genre proportions** to The Dark Knight.

All are action/war films with little comedy and romance, 
and a lot of drama.

### Euclidian
Please enter a movie's name: The Dark Knight
Enter the number of recommendations: 5
Choose a method (cosine/euclidian): euclidian

```
Recommendations for The Dark Knight
1. Gladiator 0.1
2. Saving Private Ryan 0.1732
3. 1917 0.1732
4. The Lord of the Rings: The Fellowship of the Ring 0.2
5. Oldboy 0.2

```

The distances are very small (0.1 to 0.2), which confirms that these 
movies are **numerically very close** in the normalized vector space.

After normalization, both methods converge towards similar recommendations 
because movies that are close in distance also have similar angles.

**Cosine similarity** is preferable when you want to ignore absolute intensity 
(e.g., an "intense" vs "moderate" action movie but with the same proportions).

**Euclidean distance** is preferable when absolute values 
matter (e.g., movies with exactly the same IMDB rating).

## Limits and amelioration
This film recommendation system is too simple. It might need some ML to make sure the recommendation are trully deep.
 As limits, the systme do not take into account: 
 1. User's preferences history
 2. Critics and/or notes
 3. Actors and producers
 