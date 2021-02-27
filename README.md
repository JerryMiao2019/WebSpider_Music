# 这是一个音乐爬虫

**目前支持QQ音乐**

**需安装BeautifulSoup、time、os、requests等库**

### 如何使用

1. 如果仅为使用该程序，直接打开main文件夹的QQMusic文件即可

2. 如果希望将他像一个库一样导入，请参照以下步骤

```python
import music

# 使用其get_id方法，获取id值
id = music.QQMusic.get_id('This Is It')
# 将id值传入download_list方法中
List = music.QQMusic.download_list(id)
'''
其返回值为一列表
列表按火热程度排序
列表每一项都由三个字典组成
分别是Download_parameters、singer、url
选定歌手和歌名，
'''
# 调用save方法，传入Download_parameters、保存路径和曲名即可保存
music.QQMusic.save(list [ 0 ] [ 'Download_parameters' ], '/QQMusic', 'This Is It')
```

