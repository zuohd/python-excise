# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3


class GanjiPipeline(object):
    def open_spider(self, spider):
        self.con = sqlite3.connect("xarenthouse.sqlite")

    def process_item(self, item, spider):
        print(spider.name)
        # insert_sql="insert into zufang(title,money) values('{}','{}')".format(item['title'],item['money'])
        # print("1111",insert_sql)
        # self.con.cursor().execute(insert_sql)
        # self.con.commit()
        return item

    def close_spider(self, spider):
        self.con.close()
