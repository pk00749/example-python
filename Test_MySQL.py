#coding=utf-8
import MySQLdb
import sys
import urllib2
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")# 首先设置系统的默认编码为utf-8

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='81302137',
    db='hotels',
    charset='utf8'
)

cur = conn.cursor()
# cur.execute("create table hotel(id int ,name varchar(20),address varchar(30),price varchar(10))")

# ary = [1,'abc', 'defg', '4']
# cur.execute("insert into hotel (id,name,address,price) values (%s,%s,%s,%s)", (ary[0],ary[1],ary[2],ary[3]))

cur.execute("drop table if exists hotel_1")
cur.execute("create table hotel_1(id varchar(50) ,name varchar(50),address varchar(50),price varchar(50))")
# ENGINE=MYISAM DEFAULT CHARSET=gbk")

test = u'测 试**！@#￥……%……&&*'
# test_2 = '<a title="杭州久逅•精品酒店解放路店" data-hotel="6330156" data-ctm="#ctm_ref=hod_sr_lst_dl_i_80_14" </a>'
print type(test)
print type(test.encode('utf8'))
# sql = "insert into hotel_1 (id, name) values (%s,%s)"
# value = ('100',test.encode('utf8'))
# cur.execute(sql,value)
cur.execute("insert into hotel_1 (id, name) values (%s,%s)", ('100', test.encode('utf8')))

# a = "浦发银行"
# a = a.encode("utf-8")    #编码转换为utf-8
# sql="insert into hotel_1 (id,name) values (%s,%s)"    #生成sql语句
# param=('600000',a)    #生成sql语句的参数
# cur.execute(sql,param)    #执行sql语句

cur.close()
conn.commit()
conn.close()
