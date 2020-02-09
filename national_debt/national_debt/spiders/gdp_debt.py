# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        countries = response.xpath("//tbody/tr")
        for country in countries:
            name = country.xpath(".//td/a/text()").get()
            debt_gdp_ratio = country.xpath(".//td[2]/text()").get()
            
            yield {'name': name, 'debt_gdp_ratio': debt_gdp_ratio}
