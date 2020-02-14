# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

class ImbdSqlitePipeline(object):
    def process_item(self, item, spider):
        sql = """
            INSERT INTO movies
            VALUES(?, ?, ?, ?, ?, ?);
        """
        self.cursor.execute(sql,
                            (item.get('title'),
                             item.get('year'),
                             item.get('duration'),
                             item.get('genre'),
                             item.get('rating'),
                             item.get('url')
                            ))
        self.connection.commit()
        return item


    def open_spider(self, spider):
        self.connection = sqlite3.connect('imdb.db')
        self.cursor = self.connection.cursor()
        sql = """
            CREATE TABLE IF NOT EXISTS movies
            (
                title VARCHAR,
                year INTEGER,
                duration CHAR,
                genre CHAR,
                rating CHAR,
                url VARCHAR
            );
        """
        self.cursor.execute(sql)
        self.connection.commit()


    def close_spider(self, spider):
        self.connection.close()
