import random
import requests
from Crypto.Cipher import AES
from binascii import hexlify
import json
import base64
import os

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'music.163.com',
    'Referer': 'http://music.163.com/search/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=3781266ef61a5aa2d7ede27aa0183bc1,1551083564434; _ntes_nuid=3781266ef61a5aa2d7ede27aa0183bc1; WM_TID=OZGc1XNosq1FFVUURUIpkhlLoMCtrNMy; WM_NI=8rKLP6ufZLsNyeHmP9SDIvgYp6Yeuuu9ZGfzbCvvrI%2B%2FXUYhDsvVVFRPPcN1ekPJXIbE%2FYcXpJhEf9dT8jQQUfTaONE8iXIYAb%2F6FvZ0Xr4hoDjDHTgTPQpejvbJ0%2FIHU2Q%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee92ef80fbaeb9d8b67b94a88ab2c85e829b9aafee7df4eda58df544a68f00d7ae2af0fea7c3b92afcae85add33eb7ba96adf246bbbb888ed333919c8797e653b4ea9786f87fb7e796a8e572a29dba97f143e9f198b6dc6488adbab7d54e9290a084cd3ba7b5a0abdb43a29be1bae254b496a8a6e533a88cf88bd45b97ba9c82ce4687e8a7b9cc5383bee1d7c57e9af09893b764ad9ca6a5cb60a58ca0b2f36faaaaaeabb3258b989bd3d437e2a3; JSESSIONID-WYYY=%2B0ojNXAeyKT7wKzj1AnD3RXYergSXK5S70VlZwNdlKqvuFDjOfb1Ao2PGtbBUf38RohOpdmBfcMpY3eM2jp5WiRsaJ22nosm%2F1AwqaJgomKkGAY5VfXyM%2BcVUrlgTEZFHaMNUcePUXY05Ks23XgW4yr1gPmb%2FJbtbks9nbC0OUlX82cn%3A1551237928176'
}


def get_random_str():
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    random_str = ''
    for i in range(16):
        index = random.randint(0, len(str) - 1)
        random_str += str [ index ]
    return random_str


def aes_encrypt(text, key):  # text是要加密的密文，key是密钥
    iv = b'0102030405060708'
    pad = 16 - len(text) % 16
    text = text + chr(2) * pad
    encryptor = AES.new(key.encode(), AES.MODE_CBC, iv)
    encryptor_str = encryptor.encrypt(text.encode())
    result_str = base64.b64encode(encryptor_str).decode()
    return result_str


def rsa_encrypt(text):  # text是16位的随机字符串
    pub_key = '010001'  # js中的e
    # js中的f
    modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    text = text [ ::-1 ]
    result = pow(int(hexlify(text.encode()), 16), int(pub_key, 16), int(modulus, 16))
    return format(result, 'x').zfill(131)


# b函数，两次AES加密
def get_aes(text, random_str):
    first_aes = aes_encrypt(text, key='0CoJUm6Qyw8W8jud')  # key是固定的，相当于g
    second_aes = aes_encrypt(first_aes, random_str)
    return second_aes


# 获取加密的参数
def get_post_data(text, random_str):
    params = get_aes(text, random_str)
    encSecKey = rsa_encrypt(random_str)
    return {'params': params, 'encSecKey': encSecKey}


def get_song_list(song_name, random_str):
    # 要加密的字符串
    text = {"hlpretag": "<span class=s-fc7>", "hlposttag": "</span>", "s": song_name, "type": "1", "offset": "0",
            "total": "true", "limit": "50", "csrf_token": ""}
    text = json.dumps(text)
    data = get_post_data(text, random_str)
    url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    return post_requests(url, data)


def post_requests(url, data):
    session = requests.Session()
    session.headers.update(headers)
    re = session.post(url, data=data)
    return re.json()


def get_song_url(song_id, random_str):
    # 'MD 128k': 128000, 'HD 320k': 320000
    text = {'ids': [ song_id ], 'br': 128000, 'csrf_token': ''}
    text = json.dumps(text)
    data = get_post_data(text, random_str)
    url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
    return post_requests(url, data)

def main():
    random_str = get_random_str()
    song_name = input('输入歌曲名：')
    song_list = get_song_list(song_name, random_str)
    id = song_list['result']['songs'][0]['id']
    song_url = get_song_url(id, random_str)['data'][0]['url']
    if not os.path.exists('../DownloadMusic'):
        os.mkdir(song_name)  # 新建文件夹
    with open('../DownloadMusic' + '/' + song_name + '.mp3', 'wb') as f:
        try:
            response = requests.get(song_url, timeout=10)
        except requests.exceptions.ConnectTimeout:  # 超时重新请求
            response = requests.get(song_url, timeout=10)
        f.write(response.content)

if __name__ == '__main__':
    main()
