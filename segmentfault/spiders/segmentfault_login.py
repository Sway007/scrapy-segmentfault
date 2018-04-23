# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from scrapy.loader import ItemLoader
from segmentfault.items import user_basic_info_item, tag1, tag2, user_info
from scrapy.loader.processors import MapCompose, Compose, TakeFirst

from urllib.parse import urljoin, urlparse

import json



class SegmentfaultLoginSpider(Spider):

    name = 'segmentfault_login'
    allowed_domains = ['segmentfault.com']
    # url = 'https://segmentfault.com/u/justjavac/about'

    url_tag = 'https://segmentfault.com/tags'

    url_components = urlparse( url_tag )
    domain = url_components.scheme + '://' + url_components.netloc

    def start_requests(self):
        
        # yield Request(self.url, self.parse_profile_page, 
        # headers=self.settings['DEFAULT_REQUEST_HEADERS'], 
        # cookies=self.settings['COOKIES'])

        yield Request(self.url_tag, self.tagpage_parse, 
        headers=self.settings['DEFAULT_REQUEST_HEADERS'], 
        cookies=self.settings['COOKIES'])

    def tagpage_parse(self, response):

        tag1s = []

        tag_list_selector = response.css('div.container div.row.tag-list.mt20 div.tag-list__itemWraper')
        for sel in tag_list_selector:
            tag1_loader = tag1Loader(item=tag1(), selector=sel)
            tag1_loader.add_css('title', 'h3.h5.tag-list__itemheader::text')
            tag1_loader.add_css('links', 'li.tagPopup a.tag::attr(href)')
            tag1_loader.add_css('tag2s', 'li.tagPopup a.tag::attr(data-original-title)')
            
            # # test
            # title = tag1_loader.get_css('h3.h5.tag-list__itemheader::text')
            # # input('title: {}\n'.format(title[0]))
            # with open('output/'+title[0], 'w') as f:
            #     json.dump(dict(tag1_loader.load_item()), f, indent=4, ensure_ascii=False)
            # #

            # yield tag1_loader.load_item()
            tag1s.append(tag1_loader.load_item())
        
        for item in tag1s:
            tag2_links = item['links']
            for link in tag2_links:
                link = urljoin(self.domain, link)
                # print(link)
                yield Request(link, callback=self.tag2page_parse, 
                headers=self.settings['DEFAULT_REQUEST_HEADERS'], 
                cookies=self.settings['COOKIES'])


    # TODO
    def tag2page_parse(self, response):
        
        tag2_loader = ItemLoader(item=tag2(), response=response)
        tag2_loader.add_css('title', 'div.wrap div.row section.tag-info.tag__info a.tag.tag-lg::attr(data-original-title)')
        tag2_loader.add_css('rank_monthly' ,'div.row div.widget-box.widget-taguser ol.widget-top10 li.text-muted.text-muted.showMonthTagHeroList a::attr(href)')
        tag2_loader.add_css('rank_all' ,'div.row div.widget-box.widget-taguser ol.widget-top10 li.text-muted.text-muted.showAllTagHeroList a::attr(href)')

        # test
        item = tag2_loader.load_item()

        # title = item['title'][0]
        # # input('title: {}\n'.format(title))
        # with open('output/'+title, 'w') as f:
        #     json.dump(dict(item), f, indent=4, ensure_ascii=False)
        # #

        rank_all_links = item['rank_all']
        for link in rank_all_links:
            user_id = link.split(sep='/')[1]
            link = urljoin(self.domain, link)
            yield Request(link, self.parse_profile_page, 
            headers=self.settings['DEFAULT_REQUEST_HEADERS'], 
            cookies=self.settings['COOKIES'], meta={'user_id': user_id})


        for link in item['rank_monthly']:
            user_id = link.split(sep='/')[1]
            link = urljoin(self.domain, link)
            yield Request(link, callback=self.parse_profile_page, 
                headers=self.settings['DEFAULT_REQUEST_HEADERS'], 
                cookies=self.settings['COOKIES'], meta={'user_id': user_id}
            )


    def parse_profile_page(self, response):
        # input('test!!!!!! url: ' + response.url)
        user_info_loader = customItemLoader(item=user_info(), response=response)
        user_info_loader.add_value('user_id', response.meta.get('user_id'))
        user_info_loader.add_css('user_name', 'div.profile div.container h2.profile__heading--name::text').re(u'\w+')
        user_info_loader.add_css('medal_count_gold', 'header div.profile__heading--award div.profile__heading--award-badge span:nth-child(2)::text')
        user_info_loader.add_css('medal_count_silver', 'header div.profile__heading--award div.profile__heading--award-badge span:nth-child(4)::text')
        user_info_loader.add_css('medal_count_bronze', 'header div.profile__heading--award div.profile__heading--award-badge span:nth-child(6)::text')
        user_info_loader.add_css('education', 'header div.profile__heading--other span.profile__heading--other-item span.profile__school::text').re(u'\w+')
        user_info_loader.add_css('occupation', 'header div.profile__heading--other span.profile__heading--other-item span.profile__company::text').re(u'\w+')
        user_info_loader.add_css('followers_count', 'div.profile div.row div.col-md-2 div.profile__heading-info.row div.col-md-6.col-xs-6:nth-child(2) span.h5::text')
        user_info_loader.add_css('skills', 'div.row div.profile__tech li.tagPopup a.tag::text').re(u'\w+')
        user_info_loader.add_css('open_sources', '')

        # yield basic_loader.load_item()


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
   
class tag1Loader(ItemLoader):

    pass