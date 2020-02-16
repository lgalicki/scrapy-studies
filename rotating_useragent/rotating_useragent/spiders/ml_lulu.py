# -*- coding: utf-8 -*-
import scrapy


class MlLuluSpider(scrapy.Spider):
    name = 'ml_lulu'
    allowed_domains = ['mercadolivre.com.br']
    start_urls = ['https://lista.mercadolivre.com.br/lulu-da-pomer%C3%A2nia']

    def parse(self, response):
        products = response.xpath('//div[@class = "item__info "]')
        user_agent = response.request.headers.get('User-Agent').decode('utf-8')

        for product in products:
            desc = product.xpath('normalize-space(.//span[@class = "main-title"]/text())').get()
            price = product.xpath('.//span[@class = "price__fraction"]/text()').get()
            url = product.xpath('.//parent::node()/@href').get()

            yield{
                'desc': desc,
                'price': price,
                'url': url,
                'user-agent': user_agent
                }

        next_page = response.xpath('.//a[@class = "andes-pagination__link prefetch"]/@href').get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
