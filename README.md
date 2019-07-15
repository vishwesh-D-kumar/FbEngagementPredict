# FbEngagementPredict
This app currently does the following:
  -Scrapes a given domain for all websites using a web crawler(spider) built on the scrapy module(with a limit of 100 sites due to processing power limit)
  -Saves the same onto a database for further processing
 
Currently working on adding features such as:
-Reporting the engagement count of the crawled urls using the Facebook python api 
-Segregate keywords in "main/title" tag of the same webpage and analyze their effect on the engagement counts over at facebook
-Train a multiple regression over crawled data(keywords) of multiple websites to predict a given websites engagement count


How  to run the project :
$cd MainApp
$django manage.py runserver

Open another terminal and do the following :
$cd MainApp/scrapy_app
$scrapyd
Open http://127.0.0.1:8000/FBEngagementPredict/

Instaling Dependencies required :
pip install django scrapy scrapyd python-scrapyd-api




