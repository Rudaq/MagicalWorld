# import libraries
# load the txt files to be used in the models
# create a set (sorted?) of all distinct characters and map to unique identifier
# split the book text up into subsequences with a fixed length of 100 characters, an arbitrary length (example)
# convert characters to integers
# transform the data to be suitable for keras - into the form [samples, time steps, features]
# creating model
# checkpoint?
# fit the model
import requests
import bs4
import pandas as pd

stories = []
# diablo
# forgotten realms
# final fantasy
# lotr
# tyranny
# baldur's gate
# divinity
# mtg
# wow
# goodreads quotes on dwarves, elves, wizards etc.

result = requests.get("https://lotr.fandom.com/wiki/Dwarves")
soup = bs4.BeautifulSoup(result.text, 'html.parser')


# stories.append(soup.select("meta")[8].get("content"))
# output = soup.select("meta")[8].get("content")

string = ""
for i in range(0, 5):
    string += soup.select("p")[i].getText()

output = string

with open('stories2.csv', 'a') as fd:
    fd.write(output)
    fd.write("\n")

