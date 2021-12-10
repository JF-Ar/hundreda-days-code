# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnimelistItem(scrapy.Item):
    # define the fields for your item here like:
    Titulo = scrapy.Field()
    Nota = scrapy.Field()
    Eps = scrapy.Field()
    Ano = scrapy.Field()
    Membros = scrapy.Field()
    Assista = scrapy.Field()
    Image = scrapy.Field()
