# -*- coding: utf-8 -*-

# Scrapy settings for parameters project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'parameters'

SPIDER_MODULES = ['parameters.spiders']
NEWSPIDER_MODULE = 'parameters.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'parameters (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,gl;q=0.8,pt;q=0.7',
    'cookie': 'check=true; AMCVS_3ADD33055666F1A47F000101%40AdobeOrg=1; AMCV_3ADD33055666F1A47F000101%40AdobeOrg=1075005958%7CMCIDTS%7C18309%7CMCMID%7C40423812149329860441064399821999867366%7CMCAAMLH-1582461986%7C4%7CMCAAMB-1582461986%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1581864386s%7CNONE%7CvVersion%7C4.4.1; WebMotorsVisitor=1; __gads=ID=e558721fab2fb31d:T=1581857187:S=ALNI_MbXJ-xMWGT-dWxjbJbmJerGEGwodw; s_cc=true; blueID=dade9f9b-b80c-49a5-858b-f39d12fad9e8; _fbp=fb.2.1581857187408.2063044714; mboxEdgeCluster=17; _gcl_aw=GCL.1581857187.EAIaIQobChMI1PiXm43W5wIVxR6tBh1EHgiIEAAYASAAEgJlTPD_BwE; _st_ses=22056107186307017; _st_cart_script=helper_webmotors.js; _st_cart_url=/; _sptid=70; _spcid=80; _pxvid=59095cbd-50ba-11ea-9c26-0242ac12000a; _st_no_user=1; _hjid=c90320a0-32c9-41b6-9c45-366bad71e351; _hjIncludedInSample=1; _tggcid=06010043-e474-40a2-ac00-1f225e4939a4; _tgclid=EAIaIQobChMI1PiXm43W5wIVxR6tBh1EHgiIEAAYASAAEgJlTPD_BwE; _tgrsid=EAIaIQobChMI1PiXm43W5wIVxR6tBh1EHgiIEAAYASAAEgJlTPD_BwE; sback_browser=0-87622100-158185718791bbf3131904ec61117470cf7bd40344b7e820a819792960215e4939a3d5ecc4-08788464-13820426137,1301764087-1581857187; _cm_ads_activation_retry=false; _tgsource=www.google.com; sback_client=56d484398a20ed6d221e935d; sback_customer=$2wdxEXV4ckWOVTNz0UWUZzTZhGcSFDRR1kZ0gWWrJzTZlmeD1EWygnTqtGbKpFVy5ENyoXSxJzaNpUbXZEayclT2$12; sback_access_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuc2JhY2sudGVjaCIsImlhdCI6MTU4MTg1NzE4OCwiZXhwIjoxNTgxOTQzNTg4LCJhcGkiOiJ2MiIsImRhdGEiOnsiY2xpZW50X2lkIjoiNTZkNDg0Mzk4YTIwZWQ2ZDIyMWU5MzVkIiwiY2xpZW50X2RvbWFpbiI6IndlYm1vdG9ycy5jb20uYnIiLCJjdXN0b21lcl9pZCI6IjVlNDkzOWE0MDhmYzNjN2QyNTZiM2ZhNyIsImN1c3RvbWVyX2Fub255bW91cyI6dHJ1ZSwiY29ubmVjdGlvbl9pZCI6IjVlNDkzOWE0MDhmYzNjN2QyNTZiM2ZhOCIsImFjY2Vzc19sZXZlbCI6ImN1c3RvbWVyIn19.AoYqW3_d8GbgF6C5VFEH3rMcdSoZ42JoNWJVprzxx9I.WrWrDriYWriYDrEiWriYiY; sback_partner=false; sback_current_session=1; sback_total_sessions=1; sb_days=1581857189017; sback_customer_w=true; sback_refresh_wp=no; WebMotorsCardPreferences=%221%22; gpv_v39=%2Fwebmotors%2Fcomprar%2Fresultado; s_sq=%5B%5BB%5D%5D; WMLastFilterSearch=%7B%22car%22%3A%22carros%2Festoque%2Fvolkswagen%3Fmarca1%3DVOLKSWAGEN%22%2C%22bike%22%3A%22motos%2Festoque%22%2C%22estadocidade%22%3A%22estoque%22%2C%22lastType%22%3A%22car%22%2C%22cookie%22%3A%22v3%22%2C%22ano%22%3A%7B%7D%2C%22preco%22%3A%7B%7D%2C%22marca%22%3A%22VOLKSWAGEN%22%2C%22modelo%22%3A%22%22%7D; _spl_pv=4; _px3=8c6217bdedd269a474a33a278a49fcaa86a248da0cbcd42adfcdfbb8f53c68ad:3V3epJ7RdQtjcwIpsQgA1T2SUwdTRbwq+j9aJWJ2WA60THBvh9LYD34ag/yHGpNRdw3SdamZYNF4BnDSVRd5cw==:1000:/llHpEnVN5Cj9FDCcWRJ8QveFO+B+fpa7LM9vkR+TJqSkho4BBGte2UkYCTfXJXbCIyGUGofCfcyGLI70D9CpbjEy7lbyz39FDYfO/fMx7ODFPPwmlhwu0JpzR5EQLuDwrmtJwSk5VMeOgy58Y9Vch4amSfi26Qltkaa36oj2FM=; smeventssent_558d6270794b42c3be036d07cf2129c7=true; WebMotorsSearchDataLayer=%7B%22search%22%3A%7B%22nmEstado%22%3A%22estoque%22%2C%22nmCidade%22%3A%22nao%22%2C%22sortimento%22%3A%22a30479105g%2Cb31346454g%2Cc31668701g%2Cd30877342g%2Ce31633383g%2Cf31496623m%2Cg30939761g%2Ch31405620g%2Ci31402423g%2Cj31507735g%2Ck31707304m%2Cl31652502m%2Cm31692622m%2Cn29659334g%2Co31287515g%2Cp31717428g%2Cq31279437m%2Cr31519310g%2Cs31615873g%2Ct31278858m%2Cu31527805m%2Cv30186183m%2Cw30432738g%2Cx31643676m%22%2C%22ordenacao%22%3A1%2C%22paginacao%22%3A3%2C%22termoAutocomplete%22%3A%22nao%22%2C%22raio%22%3A%22nao%22%7D%7D; mbox=session#bc8aadc6d0a64a5d840960b6b4bc7970#1581859047|PC#bc8aadc6d0a64a5d840960b6b4bc7970.17_0#1645102225',
    'referer':'https://www.webmotors.com.br/carros/estoque',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.100 Chrome/80.0.3987.100 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'parameters.middlewares.ParametersSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'parameters.middlewares.ParametersDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'parameters.pipelines.ParametersPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
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

FEED_EXPORT_ENCONDING = 'ISO 8859-1'
