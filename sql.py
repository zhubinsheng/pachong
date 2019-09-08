#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
import numpy as npx
import matplotlib.pyplot as plt
import pymysql

# 打开数据库连接
db = pymysql.connect(host='47.94.252.83', user='pachong', password='fT5MrKs24pyiaJGn', port=3306, db='pachong')

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM pc WHERE pc.`shengyujine` <>10000000000"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()

    array = []
    array3 = []
    orl_c = 5652465

    x_data = []
    y_data = []
    for row in results:
        renshu = row[1]
        shijian = row[4]
        arr = int(renshu)
        c = arr - orl_c
        orl_c = arr
        if c < 1:  # 判断num的值
            print("重复数据")
        else:
            x_data.append(shijian)
            y_data.append(c)
    print(x_data)
    print(y_data)




    # for (c,) in results:
    #     #print(c)
    #     arr = int(c)
    #     array3.append(c)
    #     array.append(arr - orl_c)
    #     orl_c =arr
    #     #print(arr)
    #
    # array2 = []
    # for (c) in array:
    #
    #     if c == 0:  # 判断num的值
    #         print
    #     else:
    #         array2.append(c)
    #
    # print(array2)
    #
    # x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
    # y_data = [10367, 9008, 10147, 9680, 10211, 10203, 10203]
    plt.plot(x_data, y_data, color='red', linewidth=2.0, linestyle='--')
    plt.show()
    # x = np.array(array2).cumsum()
    # y = range(len(x))
    # fig = plt.figure()
    # ax = fig.add_subplot(1, 1, 1)
    # ax.plot(y, x)
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.legend(['line1', 'line2'])
    # plt.plot(x, y, color='red')
    # plt.show()

    # for row in results:
    #    fname = row[0]
    #    lname = row[1]
    #    age = row[2]
    #    sex = row[3]
    #    income = row[4]
    #    # 打印结果
    #    print
    #    var = "fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
    #          (fname, lname, age, sex, income)
except:
    print("Error: unable to fecth data")

# 关闭数据库连接
db.close()
