# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpidermeetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class MeetItem(scrapy.Item):
    title = scrapy.Field()
    date_time = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()
    state = scrapy.Field()
    claw_date = scrapy.Field()
