import requests
from bs4 import BeautifulSoup


def title_generator(dates):
    list_dates = []

    def post_formatter(url):
        if 'results' in url:
            url = url.split('/')[-1]
            list_dates.append(url)

    for date in dates:
        if date.get('href') == None:
            continue
        else:
            post_formatter(date.get("href"))

    return list_dates

r = requests.get('https://www.euro-millions.com/results-history-2019')
soup = BeautifulSoup(r.text, 'html.parser')
dates = soup.findAll('a')
list_dates = title_generator(dates)
new_list = list_dates[28:]
print(len(new_list))
# for fecha in list_dates:
#     print(fecha)