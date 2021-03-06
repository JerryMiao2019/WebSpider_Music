from bs4 import BeautifulSoup
import requests

def seach_Music(name):
    search = 'https://music.163.com/#/search/m/?s=%s&type=1'% name
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    response = requests.get(url=search, headers=headers)
    print(response)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)
    h_flag = soup.find_all('div', 'item f-cb')
    h_flag_even = soup.find_all('div', 'item f-cb h-flag')
    print('\n\n\n\n\n\n\n\n',h_flag, '\n', h_flag_even)

seach_Music('this is it')
