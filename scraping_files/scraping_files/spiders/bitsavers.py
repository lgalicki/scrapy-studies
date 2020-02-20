# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scraping_files.items import ScrapingFilesItem


class BitsaversSpider(scrapy.Spider):
    name = 'bitsavers'
    allowed_domains = ['www.bitsavers.org']
    start_urls = ['http://www.bitsavers.org/pdf/sony/floppy']

    def parse(self, response):
        items = response.xpath('//following::a[6]')
        for item in items:
            loader = ItemLoader(item=ScrapingFilesItem(), selector=item)
            url = item.xpath('.//@href').get()
            abs_url = response.urljoin(url)
            name = item.xpath('.//text()').get()
            loader.add_value('file_urls', abs_url)
            loader.add_value('name', name)
            yield loader.load_item()
