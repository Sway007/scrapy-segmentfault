# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from segmentfault.items import user_basic_info_item
from scrapy.loader.processors import MapCompose, Compose

from urllib.parse import urljoin, urlparse



class SegmentfaultLoginSpider(Spider):

    name = 'segmentfault_login'
    allowed_domains = ['segmentfault.com']
    url = 'https://segmentfault.com/u/justjavac/about'

    url_components = urlparse( url )
    domain = url_components.scheme + '://' + url_components.netloc

    def start_requests(self):
        
        yield Request(self.url, self.parse_profile_page, 
        headers=self.settings['DEFAULT_REQUEST_HEADERS'], 
        cookies=self.settings['COOKIES'])

    def parse_profile_page(self, response):
        
        basic_loader = customItemLoader(item=user_basic_info_item(), response=response)
        basic_loader.add_xpath('user_name', '/html/body/div[2]/header/div/div/div[2]/h2/text()', re=r'\w+')
        basic_loader.add_xpath('major', '/html/body/div[2]/header/div/div/div[2]/div[2]/span[3]/span/text()')
        basic_loader.add_xpath('personal_page', '/html/body/div[2]/header/div/div/div[2]/div[2]/span[4]/span/a/@href')
        basic_loader.add_xpath('follows_count', '/html/body/div[2]/div/div/div/div[1]/div[2]/div[1]/a/span[2]/text()', re=r'\d+')
        basic_loader.add_xpath('followers_count', '/html/body/div[2]/div/div/div/div[1]/div[2]/div[2]/a/span[2]/text()', re=r'\d+')
        basic_loader.add_xpath('skills', '/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/div/div[2]/ul//text()')

        yield basic_loader.load_item()


        # TODO: following page
        following_link = response.xpath('/html/body/div[2]/div/div/div/div[1]/div[2]/div[1]/a/@href').extract_first()
        
        following_link = urljoin(self.domain, following_link)

        yield Request(following_link, self.parse_following_page, 
        headers=self.settings['DEFAULT_REQUEST_HEADERS'], 
        cookies=self.settings['COOKIES'])    

    def parse_following_page(self, response):
        
        following_users_sels = response.xpath('/html/body/div[2]/div/div/div/div[2]/ul[2]')
        links = following_users_sels.xpath('.//a/@href').extract()
        links = [urljoin(self.domain, link + '/about') for link in links]

        for link in links:
            yield Request(link, self.parse_profile_page,
            headers=self.settings['DEFAULT_REQUEST_HEADERS'], 
            cookies=self.settings['COOKIES'])

        next_page_link = response.xpath('/html/body/div[2]/div/div/div/div[2]/div/ul/li[@class="next"]/a/@href').extract_first()
        if next_page_link is not None:
            next_page_link = urljoin(response.url, next_page_link)
            yield Request(next_page_link, self.parse_following_page,
            headers=self.settings['DEFAULT_REQUEST_HEADERS'], 
            cookies=self.settings['COOKIES'])



class customItemLoader(ItemLoader):

    major_in = MapCompose(str.strip)
    skills_in = MapCompose(str.rstrip, str.strip)
   