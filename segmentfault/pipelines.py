# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonItemExporter
import json
from pymongo import MongoClient
import os


class MongodbPipeline(object):
    
    def __init__(self, dbserver_ip, database, collection):
        self.db_ip = dbserver_ip
        self.database = database
        self.collection = collection

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get('MONGODB_SERVER_IP'),
            crawler.settings.get('MONGODB_DATABASE'),
            crawler.settings.get('MONGODB_COLLECTION')
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.db_ip)
        self.db = self.client[self.database]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection].update({'user_id': item['user_id']}, {'$set': dict(item)}, upsert=True)
        return item

class JsonPipeline(object):

    json_output_dir = 'users'

    def open_spider(self, spider):
        if not os.path.isdir(self.json_output_dir):
            os.makedirs(self.json_output_dir)
        
        self.users_to_exporter = {}
    
    def process_item(self, item, spider):
        user_name = item.get('user_name')[0]
        if user_name not in self.users_to_exporter:
            data = dict(item)
            with open('{}/{}.json'.format(self.json_output_dir, user_name), 'w') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        return item
    
    def close_spider(self, spider):
        pass