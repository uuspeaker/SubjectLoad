# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SubjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    id = scrapy.Field()
    key = scrapy.Field()
    knowledgeId = scrapy.Field()
    knowledgeType = scrapy.Field()
    questionContent = scrapy.Field()
    options = scrapy.Field()
    questionLevel = scrapy.Field()
    questionType = scrapy.Field()
    questionResource = scrapy.Field()
    answer = scrapy.Field()
    parse = scrapy.Field()
    useTime = scrapy.Field()
    updateDate = scrapy.Field()

    pass
