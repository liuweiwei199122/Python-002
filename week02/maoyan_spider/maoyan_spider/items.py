# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    type = scrapy.Field()
    on_time = scrapy.Field()

