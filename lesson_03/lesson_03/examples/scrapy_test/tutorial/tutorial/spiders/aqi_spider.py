# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import CityItem
from bs4 import BeautifulSoup


class AqiSpider(scrapy.Spider):
    name = 'aqi_spider'
    allowed_domains = ['http://www.pm25.in/']
    start_urls = ['http://www.pm25.in/']

    # def parse(self, response):
    #     print('======================')
    #     print('type:', type(response))
    #     print('status:', response.status)
    #     print('body:')
    #     print(response.body)
    #     print('======================')

    def parse(self, response):
        bs = BeautifulSoup(response.body, 'lxml')
        bottom_div = bs.find('div', class_='all')
        city_tag_list = bottom_div.find_all('li')
        # print(city_tag_list)

        for city_tag in city_tag_list:
            city_item = CityItem()
            city_item['city_name'] = city_tag.find('a').text
            city_item['city_link'] = city_tag.find('a')['href']

            yield city_item
