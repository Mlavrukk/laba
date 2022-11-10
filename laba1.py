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
    if not os.path.exists("C:/Users/marGO.LAPTOP-CEGVK39N/laba/dataset"):
        os.mkdir("C:/Users/marGO.LAPTOP-CEGVK39N/laba/dataset")
        for i in range(1, 6):
            if not os.path.exists("C:/Users/marGO.LAPTOP-CEGVK39N/laba/dataset"+f"/{i}"):
                os.mkdir("C:/Users/marGO.LAPTOP-CEGVK39N/laba/dataset"+f"/{i}")
    
    elem = 0
    page = 0
    quotes_1 = 0
    quotes_2 = 0
    quotes_3 = 0
    quotes_4 = 0
    quotes_5 = 0
    url = "https://www.livelib.ru/reviews/"
    count = 1
    articles = []
     
    while  ((quotes_1 != 1001) and (quotes_2 != 1001) and (quotes_3 != 1001) and (quotes_4 != 1001) and (quotes_5 != 1001)):
        for i in tqdm(range(1, 9000), desc="Страница:"):
            soup = get_page(url + "~" + str(i) + "#reviews")   
            articles = (
                soup.find("main", class_="main-body page-content")
                .find("section", class_="lenta__content")
                .find_all("article", class_="review-card lenta__item")
            )
            for article in articles:
                try:
                    lenta_card = article.find("div", class_="lenta-card")
                    rates = article.find("span", class_="lenta-card__mymark")
                except AttributeError as e:
                    print("Не найдена оценка")    
                try:
                    lenta_card = article.find("div", class_="lenta-card")
                    lenta_card_book_wrapper = lenta_card.find("div", class_="lenta-card-book__wrapper")
                    names = lenta_card_book_wrapper.find( "a", class_="lenta-card__book-title" )
                except AttributeError as e:
                    print("Не найдено название")
                try:
                    lenta_card = article.find("div", class_="lenta-card")
                    text_without_readmore = lenta_card.find("div", class_="lenta-card__text without-readmore")
                    comments_texts = text_without_readmore.find(id="lenta-card__text-review-escaped")
                except AttributeError as e:
                    print("Не найдена рецензия")
                new_rates = []
                if rates is not None:
                    for rate in rates:
                        new_rates.append(str((rate.text.replace(" ", "")).replace("\n", "")))
                else:
                    print("Нет оценки")
                    continue    
                try:
                    y = min(len(names), len(comments_texts), len(new_rates))
                except Exception as e:
                    print(e)
                    pass
                    continue
                if y is None or y==0:
                    continue
                print(y)
                x = float(new_rates[0])
                if 4.5 <= x <= 5:
                    quotes_5 = quotes_5 + 1
                    if quotes_5 >= 1000:
                        continue
                    namefile = str(quotes_5).zfill(4)
                    with open(f"dataset/5/{namefile}.txt", "w+", encoding="utf-8") as file:
                        file.write(f"Оценка:{str(x)}\nНазвание:{names.text}\nРецензия:{comments_texts.text}")
                    elem = elem + 1
                elif 3.5 <= x < 4.5:
                    quotes_4 = quotes_4 + 1
                    if quotes_4 >= 1000:
                        continue
                    namefile = str(quotes_4).zfill(4)
                    with open(f"dataset/4/{namefile}.txt", "w+", encoding="utf-8") as file:
                            file.write(f"Оценка:{str(x)}\nНазвание:{names.text}\nРецензия:{comments_texts.text}")
                    elem = elem + 1
                elif 2.5 <= x < 3.5:
                    quotes_3 = quotes_3 + 1
                    if quotes_3 >= 1000:
                        continue
                    namefile = str(quotes_3).zfill(4)
                    with open(f"dataset/3/{namefile}.txt", 'w+', encoding="utf-8") as file:
                        file.write(f"Оценка:{str(x)}\nНазвание:{names.text}\nРецензия:{comments_texts.text}")
                    elem = elem + 1
                elif 1.5 <= x < 2.5:
                    quotes_2 = quotes_2 + 1
                    if quotes_2 >= 1000:
                        continue
                    namefile = str(quotes_2).zfill(4)
                    with open(f"dataset/2/{namefile}.txt", 'w+', encoding="utf-8") as file:
                        file.write(f"Оценка:{str(x)}\nНазвание:{names.text}\nРецензия:{comments_texts.text}")
                    elem = elem + 1
                else:
                    quotes_1 = quotes_1 + 1
                    if quotes_1 >= 1000:
                        continue
                    namefile = str(quotes_1).zfill(4)
                    with open(f"dataset/1/{namefile}.txt", 'w+', encoding="utf-8") as file:
                        file.write(f"Оценка:{str(x)}\nНазвание:{names.text}\nРецензия:{comments_texts.text}")
                    elem = elem + 1
                time.sleep(2)                                 
            

if __name__ == "__main__":
    url = "https://www.livelib.ru/reviews/"
    least_num_of_marks = 1000 
    max_num_of_requests = 9000
    main()           
