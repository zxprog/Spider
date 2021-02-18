# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CityItem(scrapy.Item):
    city_name = scrapy.Field()  # 城市名称
    city_link = scrapy.Field()  # 城市链接

