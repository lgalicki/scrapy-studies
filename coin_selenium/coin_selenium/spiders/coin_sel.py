#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:08:29 2020

@author: luciano
"""
from shutil import which
import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class CoinSelSpider(scrapy.Spider):

    name = 'coin_sel'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ['https://www.livecoin.net/en']
    def __init__(self):
        # Setting up headless option
        firefox_options = Options()
        firefox_options.add_argument("--headless")

        # Setting up the driver
        firefox_path = which("./geckodriver")
        driver = webdriver.Firefox(executable_path=firefox_path, options=firefox_options)

        # Setting window size. Important to get the whole content!
        driver.set_window_size(1920, 1080)

        # Acessing the site
        driver.get('https://www.livecoin.net/en')

        # Clicking on the RUR tab
        rur_tab = driver.find_elements_by_class_name('filterPanelItem___2z5Gb')
        #rur_tab = driver.find_elements_by_class('filterPanelItem___2z5Gb')
        rur_tab[4].click()

        # Storing in a string the HTML available after the previous operations
        self.html = driver.page_source

        driver.close()


    def parse(self, response):
        # Converting the string that contains the HTML in a selector object.
        # This is required because it's on them that we apply xpath expressions.
        resp = Selector(text=self.html)

        currencies = resp.xpath("//div[contains(@class,'ReactVirtualized__Table__row tableRow___3EtiS ')]")
        for currency in currencies:
            yield {
                'currency_par': currency.xpath(".//div[1]/div/text()").get(),
                'volume_24h': currency.xpath(".//div[2]/span/text()").get(),
            }
