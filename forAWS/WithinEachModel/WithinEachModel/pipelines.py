# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# exporter references:
#http://scrapingauthority.com/2016/09/19/scrapy-exporting-json-and-csv/

#https://stackoverflow.com/questions/8372703/how-can-i-use-different-pipelines-for-different-spiders-in-a-single-scrapy-proje
#https://www.cnblogs.com/zhangjpn/p/6838384.html
#https://blog.csdn.net/weixin_36485376/article/details/78388843
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy.exporters import JsonItemExporter
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import os, scrapy
import json, shutil

data_directory = "C:\\Users\\XMK23\\PycharmProjects\\GamerSkyEnt\\forAWS\WithinEachModel\\WithinEachModel\\Data"
AMI_Name = "AMI_Coarse_Pretty.json"
ASM_Name = "ASM_Coarse_Pretty.json"

imageDirectory = "C:\\Users\\XMK23\\Pictures\\Saved Pictures\\Gamersky"

class DownloadPipeline(ImagesPipeline):
    img_store = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):#重写ImagesPipeline   get_media_requests方法
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]

        # 定义分类保存的路径
        img_path = "%s%s" % (self.img_store, "%s" %(item['image_path']))
        # 目录不存在则创建目录
        if os.path.exists(img_path) == False:
            os.mkdir(img_path)

        for i in image_paths:
            shutil.move(self.img_store + i, img_path + "/")# +image_paths[0]
            print("move success\n\n")

        if not image_paths:
            raise DropItem("Item contains no images")

        return item

'''class WithineachmodelPipeline(object):

    def __init__(self):
        self.tmp_name = "tmp.json"
        self.file = open(os.path.join(data_directory, self.tmp_name), 'w')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()
        return

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

        f = open(os.path.join(data_directory, self.tmp_name), 'r')
        data = json.load(f)
        f.close()

        if spider.name == "AMISpider":
            f = open(os.path.join(data_directory, AMI_Name), 'w')
            json.dump(data, f, sort_keys=True, indent=4)
            f.close()
        elif spider.name == "ASMSpider":
            f = open(os.path.join(data_directory, ASM_Name), 'w')
            json.dump(data, f, sort_keys=True, indent=4)
            f.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item'''

