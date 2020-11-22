from pymongo import MongoClient
import bs4
from bs4 import BeautifulSoup

path = './datas/sample03.html'
db_url = 'mongodb://192.168.219.133:27017/'
with open(path) as fp:
    soup = BeautifulSoup(fp, features='lxml')
    links = soup.select('p[id]')
    with MongoClient(db_url) as client:
        sampledb = client['sample03db']
        title = ''
        link = ''
        for link in links:
            title = str.strip(link.get_text())
            link = link['id']
            data = {'title':title, 'id':link}
            infor = sampledb.sampleCollection.insert_one(data)