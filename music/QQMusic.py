# -*- coding:utf-8 -*-
import requests
from requests.packages import urllib3
from urllib import parse
from bs4 import BeautifulSoup
import os
import time

def get_id(name):
    w = parse.urlencode({'w': name})
    #请求报头,可自行添加
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
    requests.packages.urllib3.disable_warnings()
    response = requests.get(url=url, headers=headers, verify=False)
    print(url)
    soup = response.json()
    #获取歌曲id
    id = soup['data']['song']['list']
    return id


def download_list(id):
    returnList = []
    musicList = []
    urlList = []
    music = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?-=getplaysongvkey5559460738919986&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"1825194589","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"1825194589","songmid":["%s"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":24,"cv":0}}'
    for i in range(len(id)):
        musicList.append(id[i]['name']+'-'+id[i]['singer'][0]['name'])
        music['name'] = id[i]['name']
        music['singer'] = id[i]['singer'][0]['name']
        returnList.append(music)
        if __name__ == '__main__':
            print('{}.{}---{}'.format(i+1, id[i]['name'], id[i]['singer'][0]['name']))
        urlList.append(url % (id[i]['mid']))
        music = {}
    for i in range(len(returnList)):
        returnList[i]['Download_parameters'] = urlList[i]
    List = returnList
    returnList = []
    for i in List:
        returnList.append(i)
    return returnList


def save(urlList, path, name=time.time()):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }
    if __name__ == '__main__':
        try:
            os.makedirs(path)
        except:
            print('目录存在！')

        try:
            print('开始下载')
            response = requests.get(url=urlList, headers=headers)
            response = response.json()
            url_ip = response['req']['data']['freeflowsip'][1]
            purl = response['req_0']['data']['midurlinfo'][0]['purl']
            music = requests.get(url=url_ip+purl, headers=headers)
            print('下载成功')
            try:
                print('尝试保存')
                with open('{}/{}.mp3'.format(path, name), 'wb') as file:
                    file.write(music.content)
                    file.close()
            except:
                print('保存失败')
            finally:
                print('下载结束')
        except:
            print('无法下载')
    else:
        try:
            os.makedirs(path)
        except:
            pass

        try:
            response = requests.get(url=urlList, headers=headers)
            response = response.json()
            url_ip = response['req']['data']['freeflowsip'][1]
            purl = response['req_0']['data']['midurlinfo'][0]['purl']
            print(url_ip, purl)
            music = requests.get(url=url_ip+purl, headers=headers)
            try:
                with open('{}/{}.mp3'.format(path, name), 'wb') as file:
                    file.write(music.content)
                    file.close()
            except:
                return 'Can not download'
            return 'OK'
        except:
            return 'Can not download'


def main():
    name = input('歌曲名字：')
    #name = '平凡之路'
    musicList = get_id(name)
    musicList = download_list(musicList)
    number = int(input('请输入音乐序号:')) - 1
    musicList = musicList[number]
    print(musicList)
    save(musicList['Download_parameters'], path='../DownloadMusic', name=musicList['name'])


def SaveMusic(name, path='../DownloadMusic', index=0):
    musicList = get_id(name)
    musicList = download_list(musicList)
    music = musicList[index]
    save(music['Download_parameters'], path=path, name=music['name'])

if __name__ == '__main__':
    main()