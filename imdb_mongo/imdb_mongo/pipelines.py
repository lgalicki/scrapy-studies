# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import configparser as cp

class MongodbPipeline(object):
    collection_name = "best_movies"

    def open_spider(self, spider):
        # This is executed immediately after the spider is invoked.
        self.login_info = get_login()
        self.user = self.login_info[0]
        self.password = self.login_info[1]
        self.client = pymongo.MongoClient(f'mongodb+srv://{self.user}:{self.password}@cluster0-9jcpl.mongodb.net/test?retryWrites=true&w=majority')
        self.db = self.client['imdb']

    def close_spider(self, spider):
        # This is executed immediately before the spider is finished.
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item

    # @classmethod
    # def from_crawler(cls, crawler):
    #     print('This is used to get values defined in the settings file.')
    #     example = crawler.setting.get("ITEM_PIPELINES")

def get_login():
    config = cp.ConfigParser()
    config.read("/etc/config.txt")
    user = config.get("MongoDBCloud", "user")
    password = config.get("MongoDBCloud", "password")
    return user, password
