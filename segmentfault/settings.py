# -*- coding: utf-8 -*-

# Scrapy settings for segmentfault project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'segmentfault'

SPIDER_MODULES = ['segmentfault.spiders']
NEWSPIDER_MODULE = 'segmentfault.spiders'

# add custom settings by sway
COOKIES = {
        # '_ga': 'GA1.2.1173634495.1510805391', 
        # 'PHPSESSID': 'web1~u9ls6dfclhr2qk4b9hlfobtp2j',
        # 'last-url': '/',
        # '_gid': 'GA1.2.245177295.1523080522', 
        # 'sf_remember': 'e3223b8b1ac21415f1c534835ee8d28a','Hm_lvt_e23800c454aa573c0ccb16b52665ac26': '1523080523,1523080761,1523080813,1523080894',
        # '_gat':1,
        # 'io': 'lW4IPrOnjs_L-NEFIRk9', 
        # 'Hm_lpvt_e23800c454aa573c0ccb16b52665ac26': '1523104193'

        '_ga': 'GA1.2.1173634495.1510805391',
        'sf_remember': 'd8084e3c7e66cb82f4a7eef56421e7bc',
        'PHPSESSID': 'web2~po18mm2pebb1njmp2ice3tvavd',
        '_gid': 'GA1.2.1311403443.1527737948',
        '_gat': 1,
        'Hm_lvt_e23800c454aa573c0ccb16b52665ac26': '1525240685,1525682616,1527647785,1527737948',
        'io': 's99qnwt7ax_lx2JcH7HH',
        'Hm_lpvt_e23800c454aa573c0ccb16b52665ac26': '1527737975'
    }


MONGODB_SERVER_IP = '47.75.87.76'
MONGODB_DATABASE   = 'segmentfault'
# MONGODB_COLLECTION = 'user_baisic_info'
MONGODB_COLLECTION = 'user_info_v2_local'

# DEPTH_LIMIT = 4
# end 


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'segmentfault (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.5
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': '*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'Connection': 'keep-alive',
    'Host': 'segmentfault.com:9443',
    'Origin': 'https://segmentfault.com',
    'Referer': 'https://segmentfault.com/u/justjavac/about',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) ,AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}

USER_AGENT_POOL = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "  
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",  
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "  
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",  
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "  
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",  
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "  
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",  
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "  
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",  
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "  
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",  
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "  
    "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",  
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "  
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "  
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",  
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  
    "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",  
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "  
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "  
    "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",  
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "  
    "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",  
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "  
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",  
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "  
    "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'segmentfault.middlewares.SegmentfaultDownloaderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'segmentfault.middlewares.SegmentfaultDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
#    'segmentfault.pipelines.JsonPipeline': 200,
   'segmentfault.pipelines.MongodbPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
