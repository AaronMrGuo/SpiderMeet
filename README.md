<img src=".\asset\scrapy.png" style="zoom: 25%;" /><img src=".\asset\medical.png" alt="medical" style="zoom: 25%;" />

# 👷🏼医疗行业会议信息收集



## 项目简介

> - 定时采集10家医学会和1个微信公众号会议通知
> - 写入MySQL数据库，持久化储存
> - 次日发送邮件，获取上一个工作日发布的会议通知
> - 已经收集医学会190家，目前项目正在ing...
> - 案例仅供学习交流使用

## 环境准备

**安装MySQL**

**安装pymysql**

```bash
pip install pymysql
```

**安装scrapy**

```bash
pip install scrapy
```

**创建项目**

```bash
scrapy startproject SpiderMeet
```

**进入项目目录**

```bash
cd spiders
```

**创建爬虫**

```bash
scrapy genspider SpiderName example.com
```

**运行爬虫**

```bash
scrapy crawl SpiderName --nolog
```



## 📖项目目录结构

```bash
C:.
│  .gitattributes
│  .gitignore
│  items.py
│  KeyMeet.py
│  middlewares.py
│  MySQLConnector.py
│  pipelines.py
│  README.md
│  run.py
│  scrapy.cfg
│  settings.py
│  __init__.py
│
├─asset
│      medical.png
│      scrapy.png
│
├─log
│      20230607205948040405.log
│
├─spiders
│  │  beijingjiankangcujin.py
│  │  henanyixuewang.py
│  │  ningboyixuehui.py
│  │  rentijiankangkejicujinhui.py
│  │  sichuanshengyixuehui.py
│  │  xibaoshengwuxuexuehui.py
│  │  youmaihuixun.py
│  │  zhongguokangaixiehui.py
│  │  zhongguokangfuyixuehui.py
│  │  zhongguoyaoxuehui.py
│  │  zhonguoshengwuyixue.py
│  │  __init__.py
│  │
│  └─__pycache__
│          beijingjiankangcujin.cpython-39.pyc
│          henanyixuewang.cpython-39.pyc
│          ningboyixuehui.cpython-39.pyc
│          rentijiankangkejicujinhui.cpython-39.pyc
│          sichuanshengyixuehui.cpython-39.pyc
│          youmaihuixun.cpython-39.pyc
│          zhongguokangaixiehui.cpython-39.pyc
│          zhongguokangfuyixuehui.cpython-39.pyc
│          zhongguoyaoxuehui.cpython-39.pyc
│          zhonguoshengwuyixue.cpython-39.pyc
│          __init__.cpython-39.pyc
│
└─__pycache__
        items.cpython-39.pyc
        KeyMeet.cpython-39.pyc
        MySQLConnector.cpython-39.pyc
        pipelines.cpython-39.pyc
        settings.cpython-39.pyc
        __init__.cpython-39.pyc
```



## 项目运行

**安装MySQL**

**关于MySQLConnector.py**

> - MySQLConnector.py中封装了数据库的增删改查Database类
> - 可以使用Database中的create_table方法创建表

**pipelines.py中配置**

> - 修改Database类，链接自己的数据库



## 监控名单

> - [北京健康促进协会](http://www.chinahpa.org/index.php/Index/yixuehuodong.html)
> - [河南省医学会](https://meeting.henanyixue.com/web.html#/)
> - [宁波市医学会](http://www.nbygzx.org.cn/col/col8277/index.html)
> - [人体健康科技促进会](http://www.chstpa.com.cn/peroidMeeting/index?id=17&title=%E5%AD%A6%E6%9C%AF%E4%BC%9A%E8%AE%AE)
> - [四川省医学会](http://ent2006615ent2006615ent2006615www.sma.org.cn/main/xhxg.asp?xshd.asp)
> - [优麦会讯公众号](http://wechat.umer.com.cn/meeting/main/index)
> - [中国抗癌协会](http://www.caca.org.cn/xshy/hytz/)
> - [中国康复医学会](https://www.carm.org.cn/col/col6705/index.html)
> - [中国药学会](https://www.cpa.org.cn/?do=infolist&classid=270)
> - [中国细胞生物学学会](https://www.cscb.org.cn/conferencelist/35.html)
> - [中国生物医学工程学会](http://www.csbme.org/meeting/index.htm)



## 关于作者🐋

关于愿景：

​	励志成为一名医疗行业NLP工程师的打工人

关于头发：

​	偶尔掉一点，还很茂密（可能技术有很大提升空间）

关于爱好：

​	坚持每周锻炼两次，腹肌一大块

关于朋友：

​	积极向各位大佬学习，提升自身

关于联系方式：

​	🚀aaronguo0606@gmail.com





