# -*- coding: utf-8 -*-
import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.geekbuying.com']
    start_urls = ['https://www.geekbuying.com/deals']

    def parse(self, response):
        products = response.xpath('//div[@class="category_li"]')
        for product in products:
            url = product.xpath('.//a[1]/@href').get()
            name = product.xpath('.//a[2]/text()').get()
            price = response.xpath('.//div[@class = "category_li_price"]/span/'
                                   'text()').get()
            days_left = response.xpath('.//div[@class = "category_li_clai"]'
                                       '/div[@class = "category_li_claibg"]'
                                       '/span/text()').get()

            price = price.lstrip('R$')
            days_left = days_left.rstrip(' Left')

            yield{
                'name': name,
                'price': price,
                'days_left': days_left,
                'url': url
                }

        next_page = response.xpath('.//a[@class = "next"]/@href').get()

        if next_page:
            yield response.follow(url=next_page, callback=self.parse)
