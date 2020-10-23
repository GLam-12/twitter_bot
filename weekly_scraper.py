import requests
from bs4 import BeautifulSoup
import os
import time

URL = 'https://www.reddit.com/r/memes/top/?t=week'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0'}

page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')

def get_image():
    image_tags = soup.find_all('img', attrs = {'class': '_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XWObl-3b9tPy64oaG6fax'})
    if not os.path.exists('weekly'):
        os.makedirs('weekly')
    os.chdir('weekly')
    x = 0
    for image in image_tags:
        try:
            url = image['src']
            source = requests.get(url)
            if source.status_code == 200:
                with open('image-' + str(x) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    f.close()
                    x += 1
        except:
            pass

get_image()