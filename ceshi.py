import pyecharts.options as opts
from example.commons import  Faker
from pyecharts.charts import Line
# import pandas as pd
#
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdate
# from matplotlib.pyplot import rcParams
# %matplotlib inline



import json

from bs4 import BeautifulSoup
from lxml import html
import xml
import requests

url = "https://97bd8fc25c64468ebd3aaa48e5d696fe@report.url.cn/sentry/497"
f = requests.get(url)                 #Get该网页从而获取该html内容
soup = BeautifulSoup(f.content, "lxml")  #用lxml解析器解析该网页的内容, 好像f.text也是返回的html
data = f.content.decode()						#尝试打印出网页内容,看是否获取成功
print(data)
# user_dict = json.loads(data)
# print(user_dict)
# renshu = user_dict["data"]["t_date"]["t:2019-09-07"]
# jine = user_dict["data"]["m_date"]["m:2019-09-07"]
# shengyu = user_dict["data"]["q_date"]["q:2019-09-08"]
# print(renshu)
# print(jine)
# print(shengyu)
#content = soup.find_all('div',class_="p12" )   #尝试获取节点，因为calss和关键字冲突，所以改名class_

