from bs4 import BeautifulSoup
import requests
from urllib import parse

def seach_Music(name):
    data = {'wd': name}
    post_data = parse.urlencode(data)
    #print(post_data[3:])
    search = 'https://music.163.com/#/search/m/?s=%E6%B5%B7%E9%98%94%E5%A4%A9%E7%A9%BA&type=1'#% post_data[3:]
    headers = {
        'referer': 'https://music.163.com/',
        'Host': 'music.163.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    response = requests.get(url=search, headers=headers)
    print(response)
    soup = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
    #print(soup)
    div = soup.find_all('div', class_='ztag j-flag')
    print(div, '\n')

seach_Music('真的爱你')
