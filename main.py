from music import *
_API = {'QQ Music':'https://y.qq.com/',
        'CLoudMusic':'https://music.163.com/'}
def main(name, API = 'QQ'):
    if API == 'QQ':
        QQMusic.main(name)
    elif API == 'CloudMusic':
        pass

if __name__ == '__main__':
    main('可否冲破')

