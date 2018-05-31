# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class user_basic_info_item(scrapy.Item):

    user_name = scrapy.Field()       # 昵称
    major = scrapy.Field()           # 行业
    personal_page = scrapy.Field()   # 个人主页
    follows_count = scrapy.Field()   # 关注人数
    followers_count = scrapy.Field() # 粉丝个数
    skills = scrapy.Field()          # 擅长技能
    # following_link = scrapy.Field()  # 关注链接

class tag1(scrapy.Item):        # 1级标题
    
    title = scrapy.Field()
    tag2s = scrapy.Field()
    links = scrapy.Field()            

class tag2(scrapy.Item):

    title = scrapy.Field()
    rank_monthly = scrapy.Field()
    rank_all = scrapy.Field()


class user_info(scrapy.Item):

    user_id = scrapy.Field()                # 唯一ID
    user_name = scrapy.Field(output_processor=TakeFirst())
    medal_count_gold = scrapy.Field(output_processor=TakeFirst())
    medal_count_silver = scrapy.Field(output_processor=TakeFirst())
    medal_count_bronze = scrapy.Field(output_processor=TakeFirst())
    education = scrapy.Field(output_processor=TakeFirst())
    occupation = scrapy.Field(output_processor=TakeFirst())
    followers_count = scrapy.Field(output_processor=TakeFirst())
    skills = scrapy.Field()                 # 擅长技能
    open_sources = scrapy.Field(            # 开源项目＆著作
        # output_processor = combine_opensources()
    )
    skills_points_dic = scrapy.Field()      # 技能分数
    
class article_info(scrapy.Item):

    user_id = scrapy.Field()
    doc_title = scrapy.Field(output_processor=TakeFirst())
    tags = scrapy.Field()
    count = scrapy.Field(output_processor=TakeFirst())         # 赞数
