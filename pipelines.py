# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
import requests
from scrapy.pipelines.images import ImagesPipeline
from TiebaPic import settings

class TubaexPipeline(ImagesPipeline):

    def get_media_requests(self,item,info):
        img_link = item['img_url']
        yield scrapy.Request(img_link)

    def item_completed(self,results,item,info):
        images_store="E://pic4//"
        img_path=item['img_url']
        return item
