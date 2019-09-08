import json
from bs4 import BeautifulSoup
from lxml import html
import xml
import requests
import numpy as np
import numpy as npx
import matplotlib.pyplot as plt

import pymysql
import threading
import time


def spider():
    list = []
    old_list_int = []
    ord_shengyu = 0
    url = "https://ssl.gongyi.qq.com/cgi-bin/gywcom_1999_platform"
    f = requests.get(url)  # Get该网页从而获取该html内容
    soup = BeautifulSoup(f.content, "lxml")  # 用lxml解析器解析该网页的内容, 好像f.text也是返回的html
    data = f.content.decode()  # 尝试打印出网页内容,看是否获取成功
    # print(type(data))
    user_dict = json.loads(data)
    # print(user_dict)
    renshu = user_dict["data"]["t_date"]["t:2019-09-08"]
    jine = user_dict["data"]["m_date"]["m:2019-09-08"]
    shengyu = user_dict["data"]["c_date"]["c:2019-09-08"]
    upt = user_dict["data"]["upt"]
    inter = user_dict["data"]["inter"]
    print(renshu)
    print(jine)
    print(shengyu)
    #print(upt)
    ord_shengyu = shengyu - ord_shengyu
    # print(shengyu - ord_shengyu)
    # ord_shengyu = shengyu
    old_list_int.append(shengyu - ord_shengyu)

    # print(ord_shengyu)
    #x = np.random.random_integers(1, 20, 10)
    # print(x)
    # print(x.ndim)

    # y = old_list_int
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.plot(y, x)
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.legend(['line1', 'line2'])
    # plt.show()
    #
    # list.append(renshu)
    # list.append(jine)
    # list.append(shengyu)
    list.append(inter)

    db = pymysql.connect(host='47.94.252.83', user='pachong', password='fT5MrKs24pyiaJGn', port=3306, db='pachong')
    cursor = db.cursor()
    sql = 'INSERT INTO pc( renshu, juanzhujine, shengyujine, shijian)  values(%s, %s, %s, %s)'
    try:
        cursor.execute(sql, (renshu, jine, shengyu,upt))
        db.commit()
    except:
        db.rollback()
    db.close()

    time.sleep(1)

    return list


if __name__ == '__main__':
    old_list = []
    old_list_num = 1
    while True:
        old_list = spider()

        # old_list_num = old_list_num + 1
        # old_list.append(old_list_num)
        # print(old_list)
        # # old_list_num = list
        #
        # x = np.array(old_list).cumsum()
        # y = range(len(x))
        # # fig = plt.figure()
        # # ax = fig.add_subplot(1, 1, 1)
        # # ax.plot(x, y)
        # # plt.xlabel('y')
        # # plt.ylabel('x')
        # # plt.legend(['line1', 'line2'])
        # plt.plot(x, y, color='red')
        # plt.plot(x, y, 'blue')
        #
        # plt.show()

        # fig = plt.figure()
        # ax1 = fig.add_subplot(1, 1, 1)
        # # ax2 = fig.add_subplot(2, 2, 4)
        # temp = np.array(old_list).cumsum()
        # # print(temp)
        # ax1.plot(temp)
        # # 画折线
        # # ax2.plot(np.arange(20) + 3 * np.random.randn(20))
        # # print(old_list)
        # plt.show()

        # x = np.random.random_integers(1, 20, 10)
        # y = old_list
        # fig = plt.figure()
        # ax = fig.add_subplot(1, 1, 1)
        # ax.plot(y, x)
        # plt.xlabel('x')
        # plt.ylabel('y')
        # plt.legend(['line1', 'line2'])
        # plt.show()
