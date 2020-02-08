# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    # The variable below tells Scrapy which URLs he can scrape. A slash at the
    # end of the URLs could cause a 'Filtered outside request' error.
    allowed_domains = ['www.worldometers.info']

    # By default Scrapy will use http. If necessary, change it to https.
    start_urls = ['https://www.worldometers.info/world-population/'
                  'population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # Not the coolest way to do it.
            # abs_link = "https://www.worldometers.info" + link
            # yield scrapy.Request(url=abs_link)

            # Here's the fancy way!
            # abs_link = response.urljoin(link)
            # yield scrapy.Request(url=abs_link)

            # And finally the fanciest of them all, where you don't have to
            # worry about handlgin relative URLs.
            yield response.follow(url=link, callback=self.parse_country,
                                  meta={'country_name': name})

    def parse_country(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath('(//table[@class = "table table-striped'
                              ' table-bordered table-hover table-condensed'
                              ' table-list"])[1]''/tbody/tr')
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            yield {'country_name': name, 'year': year, 'population': population}
