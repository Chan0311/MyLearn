import scrapy
from TiebaPic.items import TiebapicItem

class TubaexSpider(scrapy.Spider):
    name = "tieba"
    #allowed_domains = ["https://tieba.baidu.com/p/4803144798"]
    baseURL="https://tieba.baidu.com/p/3646792267?pn="

    offset=0
    start_urls=[baseURL+str(offset)]
    
    def parse(self,response):
        end_page=response.xpath("//div[@id='thread_theme_5']/div/ul/li[2]/span[2]/text()").extract()
        img_list=response.xpath("//img[@class='BDE_Image']/@src").extract()
        for img in img_list:
            item=TiebapicItem()
            item['img_url']=img
            yield item
    
        url=self.baseURL

        if self.offset<int(end_page[0]):
            self.offset+=1
            yield scrapy.Request(self.baseURL+str(self.offset),callback=self.parse)
        