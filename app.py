import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" for movies in data:
    print(movies["title"]) """
    
""" pick0=int(input("What Year do you want your movies to go after?"))
for movies in data:
    if movies["year"] > int(pick0):
        print(movies['title']) """

""" pick1=int(input("What Year do you want your movies to go after?"))
pick2=int(input("What Year do you want your movies to go before"))
for movies in data:
    if movies["year"] > int(pick1) and movies["year"]< int(pick2):
        print(movies["title"]) """

""" pick3=int(input("What Year do you want your movies to be in?"))
for movies in data:
    if movies["year"] == int(pick3):
        print(movies["title"]) """

type=input("Search for the movie you want")
def search(x):
    for movies in data:
        if type.lower() == movies["title"].lower():
            print(movies["title"])
search(type)
