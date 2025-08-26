# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, TakeFirst


class TuffshopItem(scrapy.Item):
    name = scrapy.Field(
        input_processor=MapCompose(lambda x: x.strip()), 
        output_processor=TakeFirst()
        )
    price = scrapy.Field(output_processor=TakeFirst())
    price_notax = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field(output_processor=TakeFirst())
    image_url = scrapy.Field(output_processor=TakeFirst())
    in_stock = scrapy.Field(output_processor=TakeFirst())