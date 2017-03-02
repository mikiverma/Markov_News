# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class SourceItem(scrapy.Item):
    sourceurl = scrapy.Field()
    sourcename = scrapy.Field()
    response_body = scrapy.Field(default=None)
    date = scrapy.Field(default=None)
    title = scrapy.Field(default=None)

    def __repr__(self):
        """only print out attr1 after exiting the Pipeline"""
        return repr({"url": self['sourceurl']})
