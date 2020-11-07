import nltk, re, pprint
from urllib import request
url = ""
n = 60
while url != "break":
    url = input("Url: ")
    try:
        html = request.urlopen(url).read().decode('utf8')
        from bs4 import BeautifulSoup
        raw = BeautifulSoup(html, 'html.parser').get_text()
        i = raw.find(".20")
        date = raw[i - 5:i + 5]
        f = open("Data{} {}.txt".format(n, date), "w", encoding='utf-8')
        f.write(raw)
        f.close()
        n += 1
    except ValueError:
        print("Erroneus url.")