# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']

    script = """
        function main(splash, args)
          -- Faking the headers
          splash:on_request(function(request)
            request:set_header('User_Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36')
          end)
          
          -- Disabling Splash's default incognito mode
          splash.private_mode_enabled = false
          
          -- Grabbing the URL and sending HTTP request
          url = args.url
          assert(splash:go(url))
          assert(splash:wait(1))
        
          -- Setting screen size to full
          splash:set_viewport_full()
          return {
            html = splash:html(),
            png = splash:png()
          }
        end
    """

    def start_requests(self):
        yield SplashRequest(url='http://quotes.toscrape.com/js',
                            callback=self.parse, endpoint='execute',
                            args={'lua_source': self.script})

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//span[@class="text"]/text()').get()
            author = quote.xpath('.//span[2]/small[@class="author"]/text()').get()
            tags = quote.xpath('.//div[@class="tags"]/a/text()').getall()

            yield {
                'text': text,
                'author': author,
                'tags': tags
                }

        next_page = response.xpath('//li[@class="next"]/a/@href').get()

        if next_page:
            abs_url = f"http://quotes.toscrape.com{next_page}"
            yield SplashRequest(url=abs_url,
                                callback=self.parse, endpoint='execute',
                                args={'lua_source': self.script})
