# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TuffshopItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    price_notax = scrapy.Field()
    url = scrapy.Field()
    image_url = scrapy.Field()