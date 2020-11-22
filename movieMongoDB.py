from pymongo import MongoClient
import bs4
from bs4 import BeautifulSoup
import requests
import time

for x in range(1, 21):
    url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'
    result = requests.get(url.format(x))
    soup = BeautifulSoup(result.content, "lxml") 
    time.sleep(2)

    # for i in range(1,11):
    #     title= soup.select(f"#old_content > table > tbody > tr:nth-child({i}) > td.title > a.movie.color_b")[0]
    #     print(i,".", title.string)
    #     table = soup.find('table', class_='list_netizen')
    #     nums = table.find_all('a', class_='author') 
    #     date = nums.nextSibling.nextSibling
    #     print(date)
    

    data = soup.select("td.title")
    i=0
    for rev in data:  
        i+=1
        print(i, rev.text.split('\n')[5])

db_url = 'mongodb://192.168.219.133:27017/'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    links = soup.select('p[id]')
    with MongoClient(db_url) as client:
        sampledb = client['moviereview']
        title = ''
        link = ''
        for link in links:
            title = str.strip(link.get_text())
            link = link['id']
            data = {'title':title, 'id':link}
            infor = sampledb.sampleCollection.insert_one(data)
