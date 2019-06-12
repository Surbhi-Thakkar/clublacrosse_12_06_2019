# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TournamentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Keyword = scrapy.Field()
    Title = scrapy.Field()
    Date = scrapy.Field()
    Location = scrapy.Field()
    Icon = scrapy.Field()
    Link = scrapy.Field()
    # status = scrapy.Field()

