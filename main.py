from music import CloudMusic,QQMusic
_API = {'tencent':'https://y.qq.com/',
        'netease':'https://music.163.com/'}
def main(name, API = 'tencent'):
    if API == 'tencent':
        QQMusic.main(name)
    elif API == 'netease':
        CloudMusic.main(name)

if __name__ == '__main__':
    name = input('歌曲：')
    main(name,'netease')

