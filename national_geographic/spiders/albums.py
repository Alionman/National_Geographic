# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
import re

class AlbumsSpider(scrapy.Spider):
    name = 'albums'
    allowed_domains = ['dili.bdatu.com', 'dili.boulderbooks.com.cn', 'apdaka01.b0.upaiyun.com']
    BASE_URL = 'http://dili.boulderbooks.com.cn/jiekou/albums/a%s.html'
    PICTURE_URL = 'http://apdaka01.b0.upaiyun.com/Upload/picimg/%s.jpg'
    cur_index = 1998
    start_urls = [BASE_URL % 1998]
    MAX_DOWNLOAD_NUM = 15
    
    def parse(self, response):
        albums = json.loads(response.body.decode('utf-8'))
        urls = []
        for album in albums['picture']:
            pic_id = re.findall(r'picimg/(\d+).jpg', album['url'])[0]
            urls.append(self.PICTURE_URL % pic_id)
        yield {'image_urls':urls}
        
        self.cur_index -= 1  
        if (1998 - self.cur_index) <= self.MAX_DOWNLOAD_NUM:
            yield Request(self.BASE_URL % self.cur_index)


