# -*- coding:utf-8 -*-
import requests
from urllib import parse
from bs4 import BeautifulSoup
import os

def get_id(name):
    w = parse.urlencode({'w': name})
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&' \
          'qqmusic_ver=1298&new_json=1&' \
          'remoteplace=txt.yqq.song&' \
          'searchid=63229658163010696&' \
          't=0&aggr=1&' \
          'cr=1&catZhida=1&' \
          'lossless=0&' \
          'flag_qc=0&' \
          'p=1&n=10&' \
          '%s&' \
          'g_tk=5381&' \
          'loginUin=0&' \
          'hostUin=0&' \
          'format=json&' \
          'inCharset=utf8&' \
          'outCharset=utf-8&' \
          'notice=0&' \
          'platform=yqq.json&' \
          'needNewCode=0'%(w)
    #print(url)
    response = requests.get(url=url, headers=headers)
    soup = response.json()
    id = soup['data']['song']['list']
    print(id)
    return id

def download(id):
    musicList = []
    urlList = []
    music = None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey5559460738919986&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"1825194589","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"1825194589","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'
    for i in range(len(id)):
        musicList.append(id[i]['name']+'-'+id[i]['singer'][0]['name'])
        print('{}.{}---{}'.format(i+1, id[i]['name'], id[i]['singer'][0]['name']))
        urlList.append(url % (id[i]['mid']))

    number = int(input('音乐序号：'))
    try:
        os.mkdir('./QQ音乐')
    except:
        print('目录存在！')

    try:
        print('开始下载')
        response = requests.get(url=urlList[number-1], headers=headers)
        response = response.json()
        url_ip = response['req']['data']['freeflowsip'][1]
        purl = response['req_0']['data']['midurlinfo'][0]['purl']
        print(url_ip, purl)
        music = requests.get(url=url_ip+purl, headers=headers)
        print('下载成功')
        try:
            print('尝试保存')
            with open('./QQ音乐/{}.mp3'.format(musicList [ number - 1 ]), 'wb') as file:
                file.write(music.content)
                file.close()
        except:
            print('保存失败')
        finally:
            print('下载结束')
    except ValueError as v:
        print('无法下载', v)

def main(times):
    for i in range(times):
        name = input('歌曲名字：')
        download(get_id(name))

if __name__ == '__main__':
    main(int(input('循环次数:')))