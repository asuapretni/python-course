"""
"How to implement FizzBuzz in Python"

Libraries:
_ requests
_ inflection
_ beautifulsoup
"""

import requests
from bs4 import BeautifulSoup
from inflection import titleize

def title_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get("href"))

    return print(titles)

r = requests.get('https://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll('a')
titles = title_generator(links)

