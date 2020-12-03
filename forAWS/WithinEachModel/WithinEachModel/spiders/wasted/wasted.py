# -*- coding: utf-8 -*-
from scrapy.spiders import Spider
from scrapy.selector import Selector
import scrapy, json
import sys
sys.path.append("..")
from items import AMIInfoCoarse, DownLoadImage

class AMISpider(Spider):
    name = "AMISpider"
    start_urls = ['https://aws.amazon.com/marketplace/search/results?page=1&filters=fulfillment_options&fulfillment_options=AMI&category=6297422012']

    page_number = 1

    def parse(self, response):

        print("####################  page %d ############################" % (self.page_number))

        articles = response.xpath("//article/div[2]/div/h1/a/@href").extract()
        for i in range(len(articles)):
            furtherURL = "https://aws.amazon.com" + articles[i]
            print(furtherURL)
            yield scrapy.Request(furtherURL, callback=self.parse_each_page_coarse)

        next = response.xpath(
            "/html/body/div[2]/div/div/div[2]/div/div[1]/div/div/ul/li[@class='next']/a/@href").extract_first()
        if next != None:
            next_page = "https://aws.amazon.com/marketplace/search/results" + next
            #print(next_page)
            self.page_number += 1
            yield scrapy.Request(next_page, callback=self.parse)
        else:
            pass

    def parse_each_page_coarse(self, response):
        data = Selector(response)
        item = AMIInfoCoarse()
        #header
        item["header_vendor"] = data.xpath("/html/body/div/div/div/div[1]/section[1]/div/article[2]/div[1]/span/span[2]/a/text()").extract()
        item["header_latestVersion"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[1]/article/div/div[1]/div/div[1]/text()").extract()
        item["header_quickInformation"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/article/div[1]/div/div/p/text()").extract()
        item["header_typicalTotalPrice"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/div/article[3]/div/div/div/p[1]/text()").extract()
        item["header_descriptionOfTTP"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/div/article[3]/div/div/div/p[2]").extract()
        item["header_OS"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/article/div[2]/div[2]/span/text()").extract()
        item["header_extraTag"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/div/article[2]/div[3]/span[3]/span/span[2]/div/text()").extract()
        # Product Overview
        item["po_information"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[1]/article/p").extract()
        item["po_pdpAttributes"] = data.xpath("/html/body/div/div/div/div[4]/section[1]/article/div[1]").extract()
        item["po_highLights"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[1]/aside/article/ul").extract()
        # Usage Information
        item["ui_fulfillmentOptions"] = data.xpath("/html/body/div/div/div/div[4]/section[3]/usage/div/article/div/div/div[1]/div").extract()
        item["ui_requiredAWSServices"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[3]/usage/div/article/div/div/div[3]/div[2]/p[2]/text()").extract()
        item["ui_usageInstructions"] = data.xpath("/html/body/div/div/div/div[4]/section[3]/usage/div/article/div/div/div[4]/p[2]/span").extract()
        item["ui_endUserLicenseAgreement"] = data.xpath("/html/body/div/div/div/div[4]/section[3]/usage/div/article/article/div/p").extract()
        item["ui_additionalResource"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[3]/usage/div/aside/article/ul").extract()
        #support information
        item["si_general"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[4]/support/div/article").extract()
        item["si_additionalResource"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[4]/support/div/aside/article/ul").extract()
        #go to the Pricing information
        id = data.xpath("/html/body/div[1]/div/div/div[4]/section[2]/pricing/article/div[1]/div[2]/div[2]/div/div[1]/button/@value").extract_first()

        yield scrapy.Request("https://aws.amazon.com/marketplace/server/ajax/offer?productId=" + id,
                             meta={'item': item, 'id': id},
                             callback=self.parse_pricing)

    def parse_pricing(self, response):
        string = response.xpath("/html/body/pre/text()").extract_first()
        data = json.loads(string) #or .body_as_unicode()'''
        item = response.meta['item']
        id = response.meta['id']
        item["pi_offer"] = data

        yield scrapy.Request("https://aws.amazon.com/marketplace/server/ajax/reviews?productId=" + id,
                             meta={'item': item, 'id': id},
                             callback=self.parse_review)

    def parse_review(self, response):
        string = response.xpath("/html/body/pre/text()").extract_first()
        data = json.loads(string)  # or .body_as_unicode()'''
        item = response.meta['item']
        id = response.meta['id']
        item["cr_reviews"] = data
        yield item

    '''def parse_each_page(self, response):
        data = Selector(response)
        item = AMIInformation()
        # 简要信息
        item["modelName"] = data.xpath("/html/body/div/div/div/div[1]/section[1]/div/article[2]/h1/text()").extract()
        item["vendor"] = response.xpath("/html/body/div/div/div/div[1]/section[1]/div/article[2]/div[1]/span/span[2]/a/text()").extract()
        item["latestVersion"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/div/article[2]/div[1]/small/span[2]/text()").extract()
        item["quickInformation"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/div/article[2]/div[2]/div/p/text()").extract()
        item["typicalTotalPrice"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/div/article[3]/div/div/div/p[1]/text()").extract()
        item["descriptionOfTTP"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/div/article[3]/div/div/div/p[2]").extract()
        item["OS"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/article/div[2]/div[2]/span/text()").extract()
        item["extraTag"] = data.xpath("/html/body/div[1]/div/div/div[1]/section[1]/div/article[2]/div[3]/span[3]/span/span[2]/div/text()").extract()
        # Product Overview
        item["POInformation"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[1]/article/p/text()").extract()
        item["informationURL"] = data.xpath("html/body/div[1]/div/div/div[4]/section[1]/article/p/a/text()").extract()
        item["version"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[1]/article/div/div[1]/div/div[1]/text()").extract()
        item["showOtherVersion"] = data.xpath("//*[@id='otherVersionTitles']/span/div/div/ul").extract_first()
        item["operatingSystem"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[1]/article/div/div[4]/p[2]/text()").extract()
        item["deliveryMethods"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[1]/article/div/div[5]/div/ul/li/span/text()").extract()
        item["highLights"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[1]/aside/article/ul").extract()
        # Usage Information
        item["fulfillmentOptions"] = data.xpath("/html/body/div/div/div/div[4]/section[3]/usage/div/article/div/div/div[1]/div").extract()
        item["requiredAWSServices"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[3]/usage/div/article/div/div/div[3]/div[2]/p[2]/text()").extract()
        item["usageInstruction"] = data.xpath("/html/body/div/div/div/div[4]/section[3]/usage/div/article/div/div/div[4]/p[2]/span/span/text()").extract()
        item["additionalResourceUI"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[3]/usage/div/aside/article/ul").extract()
        # Support Information
        item["generalSI"] = data.xpath("/html/body/div[1]/div/div/div[4]/section[4]/support/div/article").extract()
        item["additionalResourceSI"] = data.xpath("/html/body/div/div/div/div[4]/section[4]/support/div/aside").extract()



        yield item'''