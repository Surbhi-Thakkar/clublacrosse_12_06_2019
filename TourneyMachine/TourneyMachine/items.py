# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TourneymachineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    tournament_endpoint = scrapy.Field()
    tournament_division_id = scrapy.Field()
    tournament_id = scrapy.Field()
    tournament_name = scrapy.Field()
    time_period = scrapy.Field()
    Location = scrapy.Field()
    tournament_division_name = scrapy.Field()
    last_update = scrapy.Field()
    game_date = scrapy.Field()
    game_id = scrapy.Field()
    game_time = scrapy.Field()
    location_name = scrapy.Field()
    away_team_id = scrapy.Field()
    away_team = scrapy.Field()
    away_score = scrapy.Field()
    home_score = scrapy.Field()
    home_team = scrapy.Field()

    pass
