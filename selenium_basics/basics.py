#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:25:27 2020

@author: luciano
"""
from shutil import which
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# This is for the browser to be opened in a headless state
firefox_options = Options()
firefox_options.add_argument("--headless")

firefox_path = which("./geckodriver")

driver = webdriver.Firefox(executable_path=firefox_path, options=firefox_options)
driver.get('https://www.duckduckgo.com')

# Selecting and filling the text input
search_input = driver.find_element_by_id('search_form_input_homepage')
search_input.send_keys("My User Agent")

# Selecting and clicking on the search button
# search_btn = driver.find_element_by_id('search_button_homepage')
# search_btn.click()

# It's also possible to press Enter over the text box
search_input.send_keys(Keys.ENTER)

print(driver.page_source)

# NEVER FORGET TO CLOSE THE DRIVER, OR ELSE THEY'LL PILE UP IN THE MEMORY!!!!!!!!!!!
driver.close()


# Here are some other ways to find and element
# driver.find_element_by_xpath()
# driver.find_element_by_name()
# driver.find_element_by_css_selector()
# driver.find_element_by_link_text()
# driver.find_element_by_tag_name()
# driver.find_elements_by_class_name()
# driver.find_elements_by_tag_name()
# etc