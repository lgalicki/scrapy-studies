# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllBooksSpider(CrawlSpider):
    name = 'all_books'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3/a'),
             callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//li[@class="next"]/a'))
    )

    def parse_item(self, response):
        item = dict()
        item['book_name'] = response.xpath('//h1/text()').get()
        item['price'] = response.xpath('//p[@class="price_color"]/text()').get()
        return item
