from flask import Flask,redirect,url_for,render_template,request

def newsdata():
    import csv_file
    csv_file.write_()
    global news_list,news_link,image_link,link_list,send_list,list_link,news_time
    news_list=csv_file.news_list
    news_link=csv_file.news_link
    image_link=csv_file.image_link
    news_time=csv_file.news_time
app=Flask(__name__)

@app.route("/")

def home():
    newsdata()
    return render_template("index.html",csv_file=news_list,news_link=news_link,image_link=image_link,news_times=news_time)

app.run()

