import scrapy, re
from scrapy import Selector
from maoyan_spider.items import MaoyanSpiderItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com']

    # def parse(self, response):
    #     pass
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.get_ten_url)

    def get_ten_url(self, response):
        movie_urls = Selector(response=response).xpath('//div[@class="movie-item film-channel"]/a/@href')
        i = 0
        #print(movies)
        for url in movie_urls:
            c_url = 'https://maoyan.com' + url.extract()
            i += 1
            if i <= 10:
                yield scrapy.Request(url=c_url, callback=self.getinfo)

    def getinfo(self, response):
        name = Selector(response=response).xpath('//h1/text()').extract()[0]
        type_list = Selector(response=response).xpath('//a[@class="text-link"]/text()').extract()
        timeinfo = Selector(response=response).xpath('//li[@class="ellipsis"][last()]/text()').extract()[0]

        pattern = re.compile('\d{4}-\d{2}-\d{2}')
        on_time = re.match(pattern, timeinfo).group()
        t = '/'.join(type_list)
        item= MaoyanSpiderItem()
        item['name'] = name
        item['type'] = t
        item['on_time'] = on_time
        yield item