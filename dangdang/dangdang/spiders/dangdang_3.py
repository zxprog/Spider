import scrapy
import bs4
from ..items import DangDangItem

class DoubanSpider(scrapy.Spider):
#定义一个爬虫类DoubanSpider。
    name = 'dangdang'
    #定义爬虫的名字为douban。
    allowed_domains = ['http://bang.dangdang.com']
    #定义爬虫爬取网址的域名。
    start_urls = []
    #定义起始网址。
    for i in range(1,3):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-year-2018-0-1-%d'%i
        start_urls.append(url)
        #把豆瓣Top250图书的前3页网址添加进start_urls。

    def parse(self, response):
    #parse是默认处理response的方法。
        bs = bs4.BeautifulSoup(response.text,'html.parser')
        #用BeautifulSoup解析response。
        datas = bs.find('ul',class_="bang_list_mode").find_all('li')
        for data in  datas:
        #遍历data。
            item = DangDangItem()
            item['book_name'] = data.find(class_='name').text
            #提取出书名。
            item['author'] = data.find(class_='publisher_info').text
            #提取出出版信息。
            item['price'] = data.find(class_='price').find(class_ ='price_n').text.replace('\xa5',':')
            #提取出评分。
            #print([book_name,author,price])
            #打印上述信息。
            yield item