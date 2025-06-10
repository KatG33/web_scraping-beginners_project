
## IMDb's Top 1000 Movies Web Scraper Project

### OVERVIEW:
This project is my first attempt at creating a Python-based web scraper to collect data from websites for analysis.
Its purpose is to scrape data from IMDB's "Top 1,000 movies": <https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv&ref=hackernoon.com>.
The infomation that will be scraped includes: Title, year of release, movie length, IMDB's rating, Metascore's rating, amount of votes, gross earnings in U.S.

### FEATURES:
Data Extraction: Gathers specific information from web pages.
Data Storage: Saves the collected data in formats like CSV or JSON for easy analysis.

### LEARNING RESOURCES:
I followed Angelica Dietzel's tutorial, "How to Build a Web Scraper With Python [Step-by-Step Guide]," to develop this project.
The tutorial can be found at: https://hackernoon.com/how-to-build-a-web-scraper-with-python-step-by-step-guide-jxkp3yum.


### REQUIREMENTS:
Python 3.x

### LIBRARIES:
requests,
beautifulsoup4,
pandas (for data manipulation)

## Installation
```python
CLONE THE REPOSITORY:
git clone https://github.com/katg33/web_scraping-beginners_project.git
cd web_scraping-beginners_project

CREATE VIRTUAL ENVIRONMENT:
python -m venv venv
source venv/bin/activate  
Windows command is: venv\Scripts\activate

INSTALL DEPENDENCIES:
pip install -r requirements.txt
```

### SET THE TARGET URL:
Update the config.py file with the URL of the website you want to scrape.

### RUN THE SCRAPER:
python scraper.py

### VIEW THE OUTPUT:
The data will be saved in the output directory in your chosen format.

## Legal and Ethical Considerations
Ensure your web scraping activities comply with the target website's terms of service. Check the site's robots.txt file for any restrictions. 
REMEMBER! Unauthorized data extraction can have legal consequences.

## Acknowledgments
Thank you to Angelica Dietzel for her detailed tutorial, which was instrumental in the development of this project.
