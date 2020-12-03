# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import scrapy, json
import sys
sys.path.append("..")
from items import AMIInfoCoarse, DownLoadImage

class GmrSky(Spider):
    name = "GamerSkyEnt"
    start_urls = [
        #"https://www.gamersky.com/ent/201901/1141204.shtml",
        "https://www.gamersky.com/ent/201901/1147755.shtml",
        "https://www.gamersky.com/ent/201901/1146169.shtml",
        "https://www.gamersky.com/ent/201901/1147764.shtml",
        "https://www.gamersky.com/ent/201901/1148174.shtml",
        "https://www.gamersky.com/ent/201901/1148187.shtml",
        "https://www.gamersky.com/ent/201901/1147895.shtml",
        "https://www.gamersky.com/ent/201901/1148990.shtml",
        "https://www.gamersky.com/ent/201901/1149006.shtml",
        "https://www.gamersky.com/ent/201901/1149420.shtml",
        "https://www.gamersky.com/ent/201901/1149493.shtml",
        "https://www.gamersky.com/ent/201901/1149755.shtml",
        "https://www.gamersky.com/ent/201901/1149911.shtml",
        "https://www.gamersky.com/ent/201901/1150803.shtml",
        "https://www.gamersky.com/ent/201902/1152392.shtml",
        "https://www.gamersky.com/ent/201902/1152699.shtml",
        "https://www.gamersky.com/wenku/201902/1152662.shtml",
        "https://www.gamersky.com/ent/201902/1152924.shtml",
        "https://www.gamersky.com/ent/201902/1153527.shtml",
        "https://www.gamersky.com/ent/201902/1153978.shtml",
        "https://www.gamersky.com/ent/201902/1154310.shtml",
        "https://www.gamersky.com/ent/201902/1154487.shtml",
        "https://www.gamersky.com/ent/201902/1151764.shtml",
        "https://www.gamersky.com/ent/201902/1154535.shtml",
        "https://www.gamersky.com/news/201902/1154748.shtml",
        "https://www.gamersky.com/ent/201902/1155338.shtml",
        "https://www.gamersky.com/ent/201902/1155568.shtml",
        "https://www.gamersky.com/ent/201902/1156156.shtml",
        "https://www.gamersky.com/ent/201902/1156540.shtml",
        "https://www.gamersky.com/news/201902/1156702.shtml",
        "https://www.gamersky.com/ent/201902/1155726.shtml",
        "https://www.gamersky.com/ent/201902/1156837.shtml",
        "https://www.gamersky.com/ent/201902/1156760.shtml",
        "https://www.gamersky.com/ent/201902/1154506.shtml",
        "https://www.gamersky.com/ent/201902/1158402.shtml",
        "https://www.gamersky.com/news/201903/1158498.shtml",
        "https://www.gamersky.com/ent/201903/1158807.shtml",

    ]
    page_number = 1

    def parse(self, response):
        if response.status != 404:
            print("####################  page %d ############################" % (self.page_number))

            item = DownLoadImage() #//div[@class='Mid2L_tit']/h1/text()
            item["image_path"] = response.xpath("//div[@class='Mid2L_tit']/h1/text()").extract_first()#self.start_urls[0].replace("/", "-").replace(":", "-").replace("---", "-")#
            #version 1
            '''item["image_urls"] = response.xpath("//p[@align='center']//img/@src").extract()
            yield item'''
            #version 2
            image = []
            for url in response.xpath("//p[@align='center']/a/@href").extract():
                b = str(url).split("?")[1]
                print(b)
                image.append(b)
            item["image_urls"] = image
            yield item

            self.page_number += 1
            url = response.url
            next = ""
            if '_' in url:
                parts = url.split("_")
                tail = parts[1]
                num = int(tail.split(".")[0]) + 1
                next = parts[0] + "_%d.shtml" %(num)
            else:
                next = url[0:-6] + "_%d"%(2) + ".shtml"
            yield scrapy.Request(next, callback=self.parse)

        else:
            pass



