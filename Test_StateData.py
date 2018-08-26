# -*- coding:utf-8 -*-
# encoding: utf-8

import urllib2
from bs4 import BeautifulSoup
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding("utf-8")  # 首先设置系统的默认编码为utf-8

conn = MySQLdb.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='81302137',
    db='hotels',
    charset='utf8'
)
cur = conn.cursor()

curURL = 'http://hotels.ctrip.com/hotel/hangzhou17/p'


def load_url(page_url, page_number):
    url = page_url + str(page_number)
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    page_soup = BeautifulSoup(response.read())
    print 'Page %d, url: ' % page_number + url
    return page_soup


def spider_state_data(detail_page):
    print "Downloading..."
    page_soup = load_url(curURL, detail_page)
    hotel_list = page_soup.find(id="hotel_list")
    hotel_detail = hotel_list.find_all("div", attrs={"class": "searchresult_list"}, limit=25)
    hotels = len(hotel_detail)

    for htl in range(0, hotels):
        if hotel_detail[htl]["id"] != "hoteltuan":
            names = hotel_detail[htl].find("h2", attrs={"class": "searchresult_name"})
            name = unicode(names.span.next_sibling.string)
            addresses = hotel_detail[htl].find("p", attrs={"class": "searchresult_htladdress"})
            address = unicode(addresses.contents[0])

            cur.execute("insert into test (name,address) values(%s,%s)", (name.encode('utf8'), address.encode('utf8')))
    print "Received"


if __name__ == '__main__':

    # cur.execute("drop table if exists test")
    # cur.execute("create table if not exists test (no int unsigned not null auto_increment,name varchar(50),address varchar(200),primary key(no))engine=InnoDB default charset='utf8'")

    # for page in range(20, 35):
    for page in range(1, 150):
        spider_state_data(page)

    cur.close()
    conn.commit()
    conn.close()

    print 'State Data Done'
