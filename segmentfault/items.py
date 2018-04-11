# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class user_basic_info_item(scrapy.Item):
    # define the fields for your item here like:
    user_name = scrapy.Field()       # 昵称
    major = scrapy.Field()           # 行业
    personal_page = scrapy.Field()   # 个人主页
    follows_count = scrapy.Field()   # 关注人数
    followers_count = scrapy.Field() # 粉丝个数
    skills = scrapy.Field()          # 擅长技能
    # following_link = scrapy.Field()  # 关注链接
