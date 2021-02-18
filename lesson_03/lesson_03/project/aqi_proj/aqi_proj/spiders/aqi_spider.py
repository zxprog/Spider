# -*- coding: utf-8 -*-
import scrapy
from aqi_proj.items import CityAqiItem
from bs4 import BeautifulSoup


class AqiSpider(scrapy.Spider):
    name = 'aqi_spider'
    allowed_domains = ['http://www.pm25.in/']
    start_urls = ['http://www.pm25.in/']

    def parse(self, response):
        # 解析首页URL
        bs = BeautifulSoup(response.body, 'lxml')
        bottom_div = bs.find('div', class_='all')
        city_tag_list = bottom_div.find_all('li')

        for city_tag in city_tag_list:
            city_aqi_item = CityAqiItem()
            city_aqi_item['city_name'] = city_tag.find('a').text
            city_link = 'http://www.pm25.in' + city_tag.find('a')['href']
            city_aqi_item['city_link'] = city_link
            # 解析二级链接
            yield scrapy.Request(city_link,
                                 meta={'item': city_aqi_item},
                                 callback=self.parse_city_link,
                                 dont_filter=True)

    def parse_city_link(self, response):
        city_aqi_item = response.meta['item']
        # 解析二级链接
        bs = BeautifulSoup(response.body, 'lxml')

        print('正在爬取', city_aqi_item['city_name'])

        data_div_tag = bs.find('div', class_='span12 data')
        value_div_tag_list = data_div_tag.find_all('div', class_='value')

        city_aqi_item['aqi'] = float(value_div_tag_list[0].text)
        city_aqi_item['pm25'] = float(value_div_tag_list[1].text)
        city_aqi_item['pm10'] = float(value_div_tag_list[2].text)
        city_aqi_item['co'] = float(value_div_tag_list[3].text)
        city_aqi_item['no2'] = float(value_div_tag_list[4].text)
        city_aqi_item['o3_1h'] = float(value_div_tag_list[5].text)
        city_aqi_item['o3_8h'] = float(value_div_tag_list[6].text)
        city_aqi_item['so2'] = float(value_div_tag_list[7].text)

        yield city_aqi_item

