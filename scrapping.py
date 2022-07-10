import requests
import bs4
import pandas as pd

stories = []

for j in range(1000, 2000):
    result = requests.get("https://www.goodreads.com/book/show/"+str(j)+".{}")
    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    genres = soup.select('a.bookPageGenreLink')
    isFantasy = False
    for i in range(0, len(genres)):
        if 'Fantasy' in genres[i].getText():
            isFantasy = True
            break
    if isFantasy:
        result = requests.get("https://www.goodreads.com/book/show/"+str(j)+".{}")
        soup = bs4.BeautifulSoup(result.text, 'html.parser')
        if soup.select('span')[30]:
            desc = soup.select('span')[30].getText()
            print(desc)
            stories.append(desc)


for i in stories:
    if len(i) < 5:
        stories.remove(i)

stories_csv = pd.DataFrame(stories)
stories_csv.to_csv("stories2.csv", index=False)

