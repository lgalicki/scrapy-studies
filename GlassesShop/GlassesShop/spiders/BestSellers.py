# -*- coding: utf-8 -*-
import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'BestSellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath('//div[@class = "col-sm-6 col-md-4 m-p-product"]')

        for product in products:
            url = product.xpath('.//div[@class = "row"]/p[@class ='
                                ' "pname col-sm-12"]/a/@href').get()

            # This is an ad, not a product.
            if not url:
                continue

            image_url = product.xpath('.//div[@class = "pimg'
                                      ' default-image-front"]/a/img[@class'
                                      ' = "default-image-front"]/@src').get()
            name = product.xpath('.//div[@class = "row"]/p/a/text()').get()
            price = product.xpath('.//div[@class = "row"]/div[@class = "pprice'
                                  ' col-sm-12"]/span[@class = "pull-right"]'
                                  '/text()').get()

            # This is an item for sale. Price must be captured in another way.
            if price == '\n                                        ':
                price = product.xpath('.//div[@class = "row"]/div[@class ='
                                      ' "pprice col-sm-12"]/span[@class ='
                                      ' "pull-right"]/span[@class ='
                                      ' "sprice"]/text()').get()

            yield{
                'name': name,
                'price': price,
                'url': url,
                'image_url': image_url
                }

        next_page = response.xpath('.//ul[@class = "pagination"]/'
                                   'li[position() = last()]/a/@href').get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
