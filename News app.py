import requests
import json
query=input("What type of news are you interested in :")
url =f"https://gnews.io/api/v4/search?q={query}&lang=en&country=us&max=10&apikey=1f6f3eacbad646bca1817fe85e1f1f07"
r=requests.get(url)
news=json.loads(r.text)
#print(news,type(news))
for article in news(["articles"]):
    print(article["Title"])
    print(article["Description"])
    print("---------------------------------------------------------------------")