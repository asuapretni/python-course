import requests
from bs4 import BeautifulSoup
import datetime
import pandas as pd
# def title_generator(balls):
#     list_balls = []
#
#     def post_formatter(url):
#             url = url.string
#             list_balls.append(url)
#
#     for ball in balls:
#         post_formatter(ball.get("href"))
#
#     return list_balls
today = datetime.datetime.now()
year = today.year
years = []
for i in range(2004, year):
    years.append(i)
print(years)

r = requests.get(f'https://www.euro-millions.com/results-history-{years[0]}')
soup = BeautifulSoup(r.text, 'html.parser')
balls = soup.find_all('li', class_='ball')
list_balls = []

for ball in balls:
    list_balls.append(ball.text)

chunk_size = 5
output_list_balls = [list_balls[i:i + chunk_size] for i in range(0, len(list_balls), chunk_size)]
# print(output_list_balls)
prpr = pd.Series(list_balls).value_counts()
print(prpr[:6])
#print(balls)
# title_generator(balls)

# for fecha in list_dates:
#     print(fecha)