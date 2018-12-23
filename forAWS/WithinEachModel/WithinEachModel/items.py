# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
'''

class WithineachmodelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DownLoadImage(scrapy.Item):
    image_path = scrapy.Field()
    image_urls = scrapy.Field()
    #images_name = scrapy.Field()


class ASMInfoCoarse(scrapy.Item):
    modelName = scrapy.Field() #/html/body/div/div/div[2]/section[1]/div/article[2]/div[1]/h2/text()
    #header: //div[@class='title-area'] = /html/body/div/div/div[2]/section[1]/div/article[2]/div[1]
    header_vendor = scrapy.Field() #//div[@class='title-area']/div/span[1]/span[2]/a/text()
    header_latestVersion = scrapy.Field() #//div[@class='title-area']/div/span[2]/span[2]/text()
    header_quickInformation = scrapy.Field() #//div[@class='sidebar-box short-description']/p/text()
    header_badge = scrapy.Field() #/html/body/div/div/div[2]/section[1]/div/article[2]/div[1]/h2/awsui-badge/span/div/text()
    #product overvivew: //section[@class='awsui row overview-section awsui-util-pt-l']
    po_information = scrapy.Field() #//section[@class='awsui row overview-section awsui-util-pt-l']/article/p/text()
    po_keydataTable = scrapy.Field() #/html/body/div/div/div[3]/section[3]/article/div/awsui-table/div/div[2]/table/tbody
    po_highLights = scrapy.Field() #/html/body/div/div/div[3]/section[3]/aside/article/ul
    #pricing information
    #
    #usage information
    ui_usageInstructions =scrapy.Field() #/html/body/div/div/div[3]/section[5]/article/div/awsui-table/div/div[2]/div/p
    ui_endUserLicenseAgreement = scrapy.Field()  # /html/body/div/div/div[3]/section[5]/article/article/div/p
    ui_additionalResource = scrapy.Field() #/html/body/div/div/div[3]/section[5]/aside/div[1]/article/ul
    #support information
    si_general = scrapy.Field() #/html/body/div/div/div[3]/section[6]/support/article/div
    #customer reviews
    #

    pass


class AMIInfoCoarse(scrapy.Item):
    modelName = scrapy.Field()

    #Header
    header_vendor = scrapy.Field() # /html/body/div/div/div/div[1]/section[1]/div/article[2]/div[1]/span/span[2]/a/text()
    header_latestVersion = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[1]/article/div/div[1]/div/div[1]/text()
    header_quickInformation = scrapy.Field()#/html/body/div[1]/div/div/div[1]/section[1]/article/div[1]/div/div/p/text()
    header_typicalTotalPrice = scrapy.Field()  # /html/body/div[1]/div/div/div[1]/section[1]/div/article[3]/div/div/div/p[1]/text() 这里数据会有两行
    header_descriptionOfTTP = scrapy.Field() #coarse  # /html/body/div[1]/div/div/div[1]/section[1]/div/article[3]/div/div/div/p[2] 这一级底下的信息
    header_OS = scrapy.Field()  # /html/body/div[1]/div/div/div[1]/section[1]/article/div[2]/div[2]/span/text()
    header_extraTag = scrapy.Field()  # /html/body/div[1]/div/div/div[1]/section[1]/div/article[2]/div[3]/span[3]/span/span[2]/div/text() 不是所有的模型都有这个标签
    #Product Overview
    po_information = scrapy.Field() #coarse #/html/body/div[1]/div/div/div[4]/section[1]/article/p
    po_pdpAttributes = scrapy.Field() #coarse #/html/body/div/div/div/div[4]/section[1]/article/div[1]      或者//div[@class="pdp-attributes"]
    po_highLights = scrapy.Field() #coarse #/html/body/div[1]/div/div/div[4]/section[1]/aside/article/ul
    #Pricing information
    pi_offer = scrapy.Field() #very coarse # https://aws.amazon.com/marketplace/server/ajax/offer?productId=<productID>
    #Usage Information
    ui_fulfillmentOptions = scrapy.Field() #coarse #/html/body/div/div/div/div[4]/section[3]/usage/div/article/div/div/div[1]/div
    ui_requiredAWSServices = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[3]/usage/div/article/div/div/div[3]/div[2]/p[2]/text()
    ui_usageInstructions = scrapy.Field() #coarse #/html/body/div/div/div/div[4]/section[3]/usage/div/article/div/div/div[4]/p[2]/span
    ui_endUserLicenseAgreement = scrapy.Field() #coarse #/html/body/div/div/div/div[4]/section[3]/usage/div/article/article/div/p
    ui_additionalResource = scrapy.Field()  #coarse #/html/body/div[1]/div/div/div[4]/section[3]/usage/div/aside/article/ul
    #Support Information
    si_general = scrapy.Field() #coarse #/html/body/div[1]/div/div/div[4]/section[4]/support/div/article
    si_additionalResource = scrapy.Field() #coarse #/html/body/div[1]/div/div/div[4]/section[4]/support/div/aside/article/ul
    #Customer Reviews
    cr_reviews = scrapy.Field() #very coarse # https://aws.amazon.com/marketplace/server/ajax/reviews?productId=<productID>
    pass

'''class AMIInformation(scrapy.Item):
    modelName = scrapy.Field() #Datameer Express  /html/body/div/div/div/div[1]/section[1]/div/article[2]/h1/text()

    # 简要信息：快速了解大致情况
    vendor = scrapy.Field() # /html/body/div/div/div/div[1]/section[1]/div/article[2]/div[1]/span/span[2]/a/text()
    latestVersion = scrapy.Field() #7.2.3 /html/body/div[1]/div/div/div[1]/section[1]/div/article[2]/div[1]/small/span[2]/text()
    quickInformation = scrapy.Field()
    #Datameer Express is an agile analytics lifecycle platform that helps unlock your raw data. Rapidly integrate, transform, discover, and operationalize datasets for your projects, without writing any code.
    #/html/body/div[1]/div/div/div[1]/section[1]/article/div[1]/div/div/p/text()
    # or
    #/html/body/div[1]/div/div/div[1]/section[1]/div/article[2]/div[2]/div/p/text()
    typicalTotalPrice = scrapy.Field() #/html/body/div[1]/div/div/div[1]/section[1]/div/article[3]/div/div/div/p[1]/text() 这里数据会有两行
    descriptionOfTTP = scrapy.Field() # /html/body/div[1]/div/div/div[1]/section[1]/div/article[3]/div/div/div/p[2] 这一级底下的信息
    OS = scrapy.Field() #/html/body/div[1]/div/div/div[1]/section[1]/article/div[2]/div[2]/span/text()
    extraTag = scrapy.Field() #/html/body/div[1]/div/div/div[1]/section[1]/div/article[2]/div[3]/span[3]/span/span[2]/div/text() 不是所有的模型都有这个标签

    # Product Overview

    POInformation = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[1]/article/p/text() 这里不知道能否用这个，因为text里面有<br>
    informationURL = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[1]/article/p/a 不知道是不是所有的模型都有，得具体看看
    version = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[1]/article/div/div[1]/div/div[1]/text()
    showOtherVersion = scrapy.Field() #//*[@id="otherVersionTitles"]/span/div/div/ul 底下可能有好多东东，要查实具体情况才行
    operatingSystem = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[1]/article/div/div[4]/p[2]/text()
    deliveryMethods = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[1]/article/div/div[5]/div/ul/li/span/text()
    highLights = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[1]/aside/article/ul 底下可能有好多标签

    # Pricing Information
    # 这里情况比较复杂，可能要用复杂的方法
    # 目前来看，只要管选择 region 和 fulfillment options,然后看Software Pricing Details就行
    # 然后Software Pricing Details 有的表格有annually和hourly两个选项。
    # 无论哪种表格，都有4列

    # Usage Information
    fulfillmentOptions = scrapy.Field() #/html/body/div/div/div/div[4]/section[3]/usage/div/article/div/div/div[1]/div 底下的两行
    requiredAWSServices = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[3]/usage/div/article/div/div/div[3]/div[2]/p[2]/text()
    usageInstruction = scrapy.Field() #/html/body/div/div/div/div[4]/section[3]/usage/div/article/div/div/div[4]/p[2]/span/span/text() 注意这个信息里面可能有链接
    additionalResourceUI = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[3]/usage/div/aside/article/ul 底下可能有不止一个条目

    # Support Information
    #目前做的还不够细致，这部分的实现目前尚比较粗糙。
    generalSI = scrapy.Field() #/html/body/div[1]/div/div/div[4]/section[4]/support/div/article 底下可能有多个条目
    additionalResourceSI = scrapy.Field() # /html/body/div/div/div/div[4]/section[4]/support/div/aside 底下可能有多个条目

    # Customer Reviews
    # 最好要进入view more页面深入处理。所以暂时先不做。

    pass

class CFTInformation(scrapy.Item):

    pass

class CtnInformation(scrapy.Item):

    pass

class SaaSInformation(scrapy.Item):

    pass'''

