# BrandScrapy

> 这个项目是为了给推荐系统寻找语料库，包括各大网站常用的品牌标签。算是第一次写爬虫，中间也遇到了不少的坑。在这里特意记录一下，以供参考。

# 爬取内容

## 瑞丽网 http://hzp.rayli.com.cn/

参考spiders.rayli，主要选择了 品牌中文名（英文名）、创建者、创建时间、发源地、归属集团、品牌故事、目录、功能、系列等数据

## 中国男装网 http://na.efu.com.cn/

参考spiders.naefu，主要选择了适用年龄和品牌故事两个数据。

## 中国女装网 http://www.nz86.com/brands/p1/

参考spiders.nz86，这个网站有防爬虫机制，超过1000左右，就开始403 forbidden了。
试了一下动态ip，不过爬到的免费ip代理，都不好使，最后手动切分目录，分块爬下来了。

## 快代理 http://www.kuaidaili.com/

参考spiders.proxy，快代理，里面大多是马上就失效的代理

## data5u http://www.data5u.com/

参考spiders.proxy2, data5u，里面ip有很多国外的，几乎也没有好使的。

## chinasspp http://www.chinasspp.com/

参考spiders.chinasspp，真心喜欢这个网站，没有任何防爬虫限制，感谢感谢！

# 关于Scrapy

