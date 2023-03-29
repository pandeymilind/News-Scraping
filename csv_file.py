import webbrowser
import csv

import Scrapping
news_time,image_link,news_link,news_list=[],[],[],[]

def write_():    
    with open("news.csv",'r',encoding="utf8" )as csv_file:
        csv_reader=csv.reader(csv_file)
        a= next(csv_reader)
        
        for i in csv_reader:
            news_list.append(i[0])
            news_link.append(i[1])
            image_link.append(i[2])
            news_time.append(i[3])


