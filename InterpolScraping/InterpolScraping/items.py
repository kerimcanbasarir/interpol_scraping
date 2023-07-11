# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class InterpolscrapingItem(scrapy.Item):

    # Suçluyla ilgili verileri temsil eden Scrapy öğesi (item) tanımlanır

    name = scrapy.Field()
    forename = scrapy.Field()
    weight = scrapy.Field()
    date_of_birth = scrapy.Field()
    entity_id = scrapy.Field()
    languages_spoken_ids = scrapy.Field()
    nationalities = scrapy.Field()
    sex_id = scrapy.Field()
    country_of_birth_id = scrapy.Field()
    distinguishing_marks = scrapy.Field()
    eyes_colors_id = scrapy.Field()
    hairs_id = scrapy.Field()
    place_of_birth = scrapy.Field()
    charge = scrapy.Field()
