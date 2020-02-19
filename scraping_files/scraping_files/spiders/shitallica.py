# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scraping_files.items import ScrapingFilesItem


class ShitallicaSpider(scrapy.Spider):
    name = 'shitallica'
    allowed_domains = ['195.122.253.112']
    start_urls = ['http://195.122.253.112/public/mp3/Metallica/Albums/1996%20-%20Load']

    def parse(self, response):
        items = response.xpath('//following::tr[4]/td[2]/a[contains(@href, "mp3")]')
        for item in items:
            loader = ItemLoader(item=ScrapingFilesItem(), selector=item)
            url = item.xpath('.//@href').get()
            abs_url = response.urljoin(url)
            name = item.xpath('.//text()').get()
            loader.add_value('file_urls', abs_url)
            loader.add_value('name', name)
            yield loader.load_item()
