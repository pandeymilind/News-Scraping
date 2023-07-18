from bs4 import BeautifulSoup
import requests
import csv
import time

import webbrowser

url="https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKSlRpZ0FQAQ?hl=en-IN&gl=IN&ceid=IN%3Aen"

result=requests.get(url)

doc = BeautifulSoup(result.text,"html.parser")

prt=doc.prettify()

print()

headlines=doc.find_all(class_="gPFEn")
image=doc.find_all(class_="Quavad")
time=doc.find_all(class_="hvbAAd")
link_web=doc.find_all(class_="WwrzSb")
count_=len(headlines)
image_size=len(image)

# count_=len(image)
# print(count_)
# print(image[0])
news_headlines=[]
news_link=[]
news_time=[]
c=0
for i in range(count_):
    if c==0:
        # print(i,headlines[i]["href"])
        news_headlines.append(headlines[i].string)
        news_link.append(link_web[i]["href"])
        news_time.append(time[i].string)

        c+=1
    elif c==3:
        c=0
    else:
        c+=1

print(len(news_link),len(news_headlines),image_size )
def news_():
    
    with open('news.csv','w',encoding="utf-8",newline='') as csv_file:
        writer_=csv.writer(csv_file)
        ab=["News","Link","Image","Time"]
        writer_.writerow(ab)
        for j in range(0,60):
            
            from_="https://news.google.com"
            final_link=from_+news_link[j]
            photo=image[j]["src"]
            new_time=news_time[j]
            news_=[news_headlines[j],final_link,photo,new_time]
            
            writer_.writerow(news_)
            

    print("done")

news_()
