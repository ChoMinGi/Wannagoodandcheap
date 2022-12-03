import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['naver.com']
    start_urls = ['http://naver.com/']

    def parse(self, response):
        print('dir',dir(response))
