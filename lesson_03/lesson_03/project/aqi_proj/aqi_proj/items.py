# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AqiProjItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CityAqiItem(scrapy.Item):
    city_name = scrapy.Field()  # 城市名称
    city_link = scrapy.Field()  # 城市链接
    aqi = scrapy.Field()        # AQI
    pm25 = scrapy.Field()       # PM2.5
    pm10 = scrapy.Field()       # PM10
    co = scrapy.Field()         # CO
    no2 = scrapy.Field()        # NO2
    o3_1h = scrapy.Field()      # O3/1h
    o3_8h = scrapy.Field()      # O3/8h
    so2 = scrapy.Field()        # SO2

