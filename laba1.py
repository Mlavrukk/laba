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

date = []
rates = []
quotes_1 = 0
quotes_2 = 0
quotes_3 = 0
quotes_4 = 0
quotes_5 = 0
for p in range (1,2):
 url = 'https://www.livelib.ru/reviews/~{p}#reviews'
 html_text = requests.get(url).text
 soup = BeautifulSoup(html_text, 'lxml')

 reviers = soup.find_all("div", class_ = "lenta-card")
 for revier in reviers:
     tutle = revier.find("a", class_="lenta-card__book-title").text
     author = revier.find("a", class_="lenta-card__author").text
     rate = soup.find("div", class_= "lenta-card__details").find("span", class_="lenta-card__mymark").text
     comment = soup.find("div", class_="lenta-card__text-review-full").text
     date.append(["tutle", "author", "rate", "comment"])
     rates.append(["rate"])
     y = min(len(author), len(tutle), len(rate), len(comment))

     for i in range(y):
       rate_number = float(rates[i])
       if 4.5 <= rate_number <= 5:
        quotes_5 = quotes_5 + 1
        namefile = str(quotes_5).zfill(4)
        with open("dataset/" + "5" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as f:
          f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
        if 3.5 <= rate_number <= 4:
          quotes_4 = quotes_4 + 1
          namefile = str(quotes_4).zfill(4)
          with open("dataset/" + "4" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
           f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
        if 2.5 <= rate_number <= 3:
          quotes_3 = quotes_3 + 1
          namefile = str(quotes_3).zfill(4)
          with open("dataset/" + "3" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
           f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
        if 1.5 <= rate_number <= 2:
          quotes_2 = quotes_2 + 1
          namefile = str(quotes_2).zfill(4)
          with open("dataset/" + "2" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
           f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
        if 0.5 <= rate_number <= 1:
          quotes_1 = quotes_1 + 1
          namefile = str(quotes_1).zfill(4)
          with open("dataset/" + "1" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
           f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
     
