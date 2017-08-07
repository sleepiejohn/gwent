# Gwent: An analysis of the game

### Goals

At analysis level we want to compare amounts of cards, types, strength,
and rarity across all factions.

Finally we want to provide a clustering model to group cards and a classification
model that will answer, given a set of details of the card, which rarity it
should be ?

This will give us the whole pipeline of a machine learning problem, from data
acquisition to model preparation and test.

The data will be scrapped from the [Gwent API](gwentapi.com) and saved as a CSV file, from there
we will clean up the data and search for relations of the cards. The final dataset
will be saved and used to train and/or test our models.


### Requirements to Run

 - Python 3.5
 - pip

or
 - Anaconda

 Create an virtual env and install the dependencies using `pip install -r requirements.txt`

### Notebooks

Notebooks for exploratory data can be found at:  [./notebooks](/notebooks) on this project

----------------

License MIT
