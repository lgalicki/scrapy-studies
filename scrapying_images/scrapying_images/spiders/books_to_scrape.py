# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapying_images.items import ScrapyingImagesItem


class BooksToScrapeSpider(scrapy.Spider):
    name = 'books_to_scrape'
    #allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com']

    def parse(self, response):
        products = response.xpath('//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]')
        for product in products:
            loader = ItemLoader(item=ScrapyingImagesItem(), selector=product)
            img_src = product.xpath('.//img/@src').get()
            abs_img_src = response.urljoin(img_src)
            loader.add_value('image_urls', abs_img_src)
            loader.add_xpath('book_name','.//h3/a/@title')

            yield loader.load_item()
