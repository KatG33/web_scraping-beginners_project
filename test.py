"""Unfortunately this website has been updated to disallow  scraping.
You can confirm this by visiting https://www.imdb.com/robots.txt 
Hence I will have to stop with this project and scrape this project 
once I have completed another example of a web scraper"""

import requests
from requests import get 
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np 

headers = {"Accept-Language": "en-US, en;q=0.5"}
#url = "https://www.imbd.com/search/title/?groups=top_1000&ref_=adv_prv"
url = "https://www.imdb.com/search/title/?groups=top_1000"
results=requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

print(soup)

titles = []
years = []
run_time = []
imbd_rating = []
metascores = []
votes = []


movie_div = soup.find_all('div', class_='sc-300a8231-0 gTnHyA')
print(movie_div)
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
    
    
    
    """
    # I ma not sure if it is gonna go through the same element twice,
    # or if it will save the following element, will have to check the output
    year=container.find('span', class_="sc-300a8231-7 eaXxft dli-title-metadata-item").text
    runtime=container.find('span', class_="sc-300a8231-7 eaXxft dli-title-metadata-item").text
#   age_restr=container.find('span', class_="sc-300a8231-7 eaXxft dli-title-metadata-item").text
    years.append(year)
    time.append(runtime)
    """
    
    ibmd = container.find('span', class_="ipc-rating-star--rating").text if container.find('span', class_="ipc-rating-star--rating") else '-'
    ibmd = float(ibmd)
    imbd_rating.append(ibmd)
    
    m_score = container.find('span', class_='sc-b0901df4-0 bXIOoL metacritic-score-box').text if container.find('span', class_='sc-b0901df4-0 bXIOoL metacritic-score-box') else '-'
    metascores.append(m_score)
    
    vote_num = container.find('span', class_='ipc-rating-star--voteCount').text if container.find('span', class_='ipc-rating-star--voteCount') else '-'
    votes.append(vote_num)


    