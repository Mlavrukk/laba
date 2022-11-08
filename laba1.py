import os
from bs4 import BeautifulSoup
import requests
from requests import get
import time
from tqdm import tqdm
import random
import string
##-*- coding: utf-8 -*-

headers = {
    'Connection':'keep-alive',
    'Cookie':"__ll_tum=1654684410; __ll_ab_mp=1; __ll_unreg_session=6189823623b7232cd200d40713ea3c9d; __ll_unreg_sessions_count=3; __llutmz=0; __llutmf=0; __ll_fv=1666111952; __ll_dv=1666151708; __ll_cp=3; iwatchyou=3fcd1d453fb01ff2f05aae874e144193; __r=pc3319c2_; LiveLibId=6189823623b7232cd200d40713ea3c9d; promoLLid=7jcp65jk7c78q3t6kc8gpj2430; ll_asid=1050121097; __ll_dvs=5; __utnt=g0_y0_a15721_u0_c0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

def get_page(url):
    req = requests.get(url, headers = headers)
    if req.status_code == 200:
        return BeautifulSoup(req.content, "html.parser")
    else:
        print("Page not found")
        exit()


def main():
    print("heum")
    if not os.path.isdir("Dataset"):
        os.mkdir("Dataset")
        os.chdir("Dataset")
        for i in range(1, 6):
            if not os.path.isdir(str(i)):
                os.mkdir(str(i))
    elem = 0
    page = 0
    quotes_1 = 0
    quotes_2 = 0
    quotes_3 = 0
    quotes_4 = 0
    quotes_5 = 0
    url = "https://www.livelib.ru/reviews"
    count = 1
    reviers = []
     
    while  ((quotes_1 != 1000) and (quotes_2 != 1000) and (quotes_3 != 1000) and (quotes_4 != 1000) and (quotes_5 != 1000)):
        # letters = string.ascii_lowercase
        # rand_string = ''.join(random.sample(letters, 7))
        # _headers = {
        #     "User-Agent": rand_string
        #     }
        for i in range(1, 9000):
            print(f"Страница: {i}")
            soup = get_page(url + "~" + str(i) + "#reviews")
            print(soup)    
            articles = (
                soup.find("main", class_="main-body page-content")
                .find("section", class_="lenta__content")
                .find_all("article", class_="review-card lenta__item")
            )
            return articles
        rates = list()
        names = list()  
        comments_texts = list()
        for article in articles:
            lenta_card = article.find("div", class_="lenta-card")
            h3 = lenta_card.find("h3", class_="lenta-card__title")
            rate = h3.find("span", class_="lenta-card__mymark").text.strip()
            rates.append(rate)
            lenta_card = article.find("div", class_="lenta-card")
            lenta_card_book_wrapper = lenta_card.find("div", class_="lenta-card-book__wrapper")
            name = lenta_card_book_wrapper.find( "a", class_="lenta-card__book-title" ).text.strip()
            names.append(name)
            lenta_card = article.find("div", class_="lenta-card")
            text_without_readmore = lenta_card.find("div", class_="lenta-card__text without-readmore")
            comment = text_without_readmore.find(id="lenta-card__text-review-escaped").text
            comments_texts.append(comment)
        new_rates = []    
        for rate in rates:
            new_rates.append(str((rate.text.replace(" ", "")).replace("\n", "")))
        y = min(len(names), len(comments_texts), len(new_rates))
    

   
     



       
        # for revier in reviers:
        #     tutles = revier.find_all(class_ = "lenta-card__book-title")
        #     authors = revier.find_all(class_ = "lenta-card__author")
        #     rates = revier.find_all(class_ = "lenta-card__mymark")
        #     comments = revier.find_all(class_ = "lenta-card__text-review-escaped")
        #     new_rates = []
        #     for rate in rates:
        #         new_rates.append(str((rate.text.replace(" ", "")).replace("\n", "")))
        #     y = min(len(authors), len(tutles), len(comments), len(new_rates))
        if y == 0:
            continue
        print(y)
        x = float(new_rates[0])
        if 4.5 <= x <= 5:
            quotes_5 = quotes_5 + 1
            if quotes_5 >= 1000:
                continue
            namefile = str(quotes_5).zfill(4)
            with open("dataset/" + "5" + '/' + namefile + ".txt", "w+", encoding="utf-8") as file:
                file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names(0) + '\n' + 'Рецензия:' + '\n' + comments_texts(0))
            elem = elem + 1
        elif 3.5 <= x < 4.5:
            quotes_4 = quotes_4 + 1
            if quotes_4 >= 1000:
                continue
            namefile = str(quotes_4).zfill(4)
            with open("dataset/" + "4" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
                    file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names(0) + '\n' + 'Рецензия:' + '\n' + comments_texts(0))
            elem = elem + 1
        elif 2.5 <= x < 3.5:
            quotes_3 = quotes_3 + 1
            if quotes_3 >= 1000:
                continue
            namefile = str(quotes_3).zfill(4)
            with open("dataset/" + "3" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
                file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names(0) + '\n' + 'Рецензия:' + '\n' + comments_texts(0))
            elem = elem + 1
        elif 1.5 <= x < 2.5:
            quotes_2 = quotes_2 + 1
            if quotes_2 >= 1000:
                continue
            namefile = str(quotes_2).zfill(4)
            with open("dataset/" + "2" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
                file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names(0)  + '\n' + 'Рецензия:' + '\n' + comments_texts(0))
            elem = elem + 1
        else:
            quotes_1 = quotes_1 + 1
            if quotes_1 >= 1000:
                continue
            namefile = str(quotes_1).zfill(4)
            with open("dataset/" + "1" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
                file.write('Оценка: ' + str(x) + '\n' + 'Название: ' + names(0) + '\n' + 'Рецензия:' + '\n' + comments_texts(0))
            elem = elem + 1
        time.sleep(2)                  
        # page = page + 1 
        # url = 'https://www.livelib.ru/reviews' + '~' + str(page) + '#reviews'                    
            

if __name__ == "__main__":
     url = "https://www.livelib.ru/reviews/"
     least_num_of_marks = 1000 
     max_num_of_requests = 9000
     main()           
#  for revier in reviers:
#      tutle = revier.find("a", class_="lenta-card__book-title").text
#      author = revier.find("a", class_="lenta-card__author").text
#      rate = soup.find("div", class_= "lenta-card__details").find("span", class_="lenta-card__mymark").text
#      comment = soup.find("div", class_="lenta-card__text-review-full").text
#      date.append(["tutle", "author", "rate", "comment"])
#      rates.append(["rate"])
#      y = min(len(author), len(tutle), len(rate), len(comment))

#      for i in range(y):
#        rate_number = float(rates[i])
#        if 4.5 <= rate_number <= 5:
#         quotes_5 = quotes_5 + 1
#         namefile = str(quotes_5).zfill(4)
#         with open("dataset/" + "5" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as f:
#           f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
#         if 3.5 <= rate_number <= 4:
#           quotes_4 = quotes_4 + 1
#           namefile = str(quotes_4).zfill(4)
#           with open("dataset/" + "4" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
#            f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
#         if 2.5 <= rate_number <= 3:
#           quotes_3 = quotes_3 + 1
#           namefile = str(quotes_3).zfill(4)
#           with open("dataset/" + "3" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
#            f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
#         if 1.5 <= rate_number <= 2:
#           quotes_2 = quotes_2 + 1
#           namefile = str(quotes_2).zfill(4)
#           with open("dataset/" + "2" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
#            f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
#         if 0.5 <= rate_number <= 1:
#           quotes_1 = quotes_1 + 1
#           namefile = str(quotes_1).zfill(4)
#           with open("dataset/" + "1" + '/' + namefile + '.txt', 'w+', encoding="utf-8") as file:
#            f.write(str(rate_number) + '\n' + tutle[i].text + '\n' + author[i].text + '\n' + comment[i].text)
     
