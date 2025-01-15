"""Unfortunately this website has been updated to disallow  scraping.
You can confirm this by visiting https://www.imdb.com/robots.txt 
Hence I will have to stop with this project and scrape this project 
once I have completed another example of a web scraper"""

import requests
from requests import get 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 

headers = {"Accept-Language": "en-US,en;q=0.5",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

url = "https://www.imdb.com/search/title/?groups=top_1000"
results=requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

titles = []
years = []
run_time = []
imbd_rating = []
metascores = []
votes = []


movie_div = soup.find_all('div', class_='sc-300a8231-0 gTnHyA')
#print(movie_div)
# intiating a for loop to go through each div containing info about 
# a movie, which has been stored in movie_div
for container in movie_div: 
    name=container.a.h3.text
    titles.append(name)
    
    nv = container.find_all('span', attrs={'class': 'sc-300a8231-7 eaXxft dli-title-metadata-item'})
    year=nv[0].text
    years.append(year)
    time=nv[1].text
    run_time.append(time)
    
    ibmd = container.find('span', class_="ipc-rating-star--rating").text if container.find('span', class_="ipc-rating-star--rating") else '-'
    ibmd = float(ibmd)
    imbd_rating.append(ibmd)
    
    m_score = container.find('span', class_='sc-b0901df4-0 bXIOoL metacritic-score-box').text if container.find('span', class_='sc-b0901df4-0 bXIOoL metacritic-score-box') else '-'
    metascores.append(m_score)
    
    vote_strings = container.find('span', class_='ipc-rating-star--voteCount').text if container.find('span', class_='ipc-rating-star--voteCount') else '-'
    vote_num = vote_strings.replace("\xa0(","").replace(")","")
    votes.append(vote_num)

print(titles)
print(years)
print(run_time)
print(imbd_rating)
print(metascores)
print(votes)
    