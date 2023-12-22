import requests

from bs4 import BeautifulSoup
import pandas as pd

# URL of the website to scrape
url = "https://stackoverflow.com/questions/tagged/python"

# Send an HTTP GET request to the website
response = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the relevant information from the HTML code
questions = []
for row in soup.select('div.s-post-summary--content'):
    questions = row.find('h3', class_='.s-post-summary--content-title').find('a').get_text()
    questions.append([questions])

# Store the information in a pandas dataframe
    df = pd.DataFrame(questions, columns=['questions'])

# Add a delay between requests to avoid overwhelming the website with requests
    df.to_csv('main.csv', index=False)
