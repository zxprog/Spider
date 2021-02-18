# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangDangItem(scrapy.Item):
	book_name = scrapy.Field()
	#定义书名的数据属性
	author = scrapy.Field()
	#定义出版信息的数据属性
	price = scrapy.Field()
	#定义评分的数据属性
