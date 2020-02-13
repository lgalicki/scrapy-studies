# -*- coding: utf-8 -*-
import scrapy
from scrapy_selenium import SeleniumRequest
# from selenium.webdriver.common.keys import Keys
from scrapy.selector import Selector

class ExampleSpider(scrapy.Spider):
    name = 'example'

    def start_requests(self):
        yield SeleniumRequest(
            url='https://duckduckgo.com',
            wait_time=3,
            screenshot=True,
            callback=self.parse
            )

    def parse(self, response):
        # If you wish to save a screenshot, that's how you do it. Notice the
        # parameter in yield command in the previous method.
        # img = response.meta['screenshot']
        # with open('screenshot.png', 'wb') as file:
        #     file.write(img)

        # Creating a driver
        driver = response.meta['driver']

        # Setting window size. Important to get the whole content!
        driver.set_window_size(1080, 10000)

        # Selecting and filling in the search text box and pressing Enter
        search_input = driver.find_element_by_xpath('//input[@id="search_form_input_homepage"]')
        search_input.send_keys('Hello world')
        # search_input.send_keys(Keys.ENTER)

        # Alternitavely, clicking on search button
        search_btn = driver.find_element_by_xpath('//input[@id="search_button_homepage"]')
        search_btn.click()

        # This is how you save a screen shot after the initial request of the page
        # driver.save_screenshot('after_filling.png')
        # driver.save_screenshot('after_searching.png')

        # Getting the HTML and converting it into a selector. Gotta take it from
        # the driver, instead of the initial response, because we interacted with
        # the page and the result of the interaction is in the driver.
        html = driver.page_source
        response_obj = Selector(text=html)

        # It's time to unravel the HTML
        results = response_obj.xpath('//div[@class="result__extras__url"]/a/@href')
        for result in results:
            yield {'url': result.get()}
