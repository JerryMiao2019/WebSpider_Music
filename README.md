# 音乐爬虫

**目前支持QQ音乐**

**需安装BeautifulSoup、time、os、requests等库**

## QQ音乐

### 如何使用？

#### QQ音乐

1. 如果仅为使用该程序，直接打开main文件夹的QQMusic文件即可

2. 如果希望将它像一个库一样导入，请参照以下步骤

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
music.QQMusic.save(list[0]['Download_parameters'], '/DownloadMusic', 'This Is It')
```

##### 新增更新：

仅使用`save(name='',path='',index='')`即可下载

`name`：歌曲名

`path`:保存路径（默认为程序下的`DownloadMusic`）

`index`：歌曲排行第几，（从零开始，默认为零）

```python
from music.QQMusic import *

SaveMusic('this is it', path='../DownloadMusic', index=1)
```

### 网易云音乐：

目前可以运行源文件，不可做库导入

*参考**[xiaoming_xiaoli](https://blog.csdn.net/xiaoming_xiaoli)**的*

[网易云音乐python爬虫（Js破解）]: https://blog.csdn.net/xiaoming_xiaoli/article/details/88019016?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522161630844116780262516469%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&amp;request_id=161630844116780262516469&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~baidu_landing_v2~default-1-88019016.first_rank_v2_pc_rank_v29&amp;utm_term=%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90%E7%88%AC%E8%99%AB+JS



## 音乐文件管理功能：

即将更新，



## 更改hosts附件工具（提升GitHub访问速度）：

即将更新



## 协议：GPL3.0     

## 
