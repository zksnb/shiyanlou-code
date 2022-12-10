#爬
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import requests
from lxml import etree
from urllib import request
网址 = 'https://www.huya.com/g/2633'
老王家 = requests.get(网址)
保险柜 = 老王家.text
打开后的保险柜 = etree.HTML(保险柜)
#古董  名画 刀 金条   代码块[图片data-original  -----名称alt]
所有的图片代码块 = 打开后的保险柜.xpath('//img[@class="pic"]')

for a in 所有的图片代码块:
    图片 = a.xpath('./@data-original')[0]
    名称 = a.xpath('./@alt')[0]
    request.urlretrieve(图片, r'D:\新建文件夹\tt'+名称+'.jpg')








