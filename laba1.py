import os
from bs4 import BeautifulSoup
import requests

def main():
 print("heum")
if not os.path.isdir("Dataset"):
 os.mkdir("Dataset")
 os.chdir("Dataset")
for i in range(1, 6):
 if not os.path.isdir(str(i)):
  os.mkdir(str(i))


url = 'https://www.livelib.ru/reviews/~{p}#reviews'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

reviers = soup.find_all("div", class_ = "lenta-card")
for revier in reviers:
    tutle = revier.find("a", class_="lenta-card__book-title").text
    author = revier.find("a", class_="lenta-card__author").text
    rate = soup.find("div", class_= "lenta-card__details").find("span", class_="lenta-card__mymark").text
    comment = soup.find("div", class_="lenta-card__text-review-full").text
    