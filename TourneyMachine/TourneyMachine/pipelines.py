# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pyodbc

from TourneyMachine.items import TourneymachineItem
from TourneyMachine.spiders import database_con as dbc

class TourneymachinePipeline(object):
    server = dbc.server
    database = dbc.database
    username = dbc.username
    password = dbc.password
    driver = dbc.driver
    table = dbc.table
    i = 1

    def __init__(self):
        # try:
        #     self.connection = MySQLdb.connect(self.DB_IP, self.DB_user, self.DB_password, charset='utf8')
        #     self.cursor = self.connection.cursor()
        #     self.cursor.execute('CREATE DATABASE if not exists ' + self.DB_name)
        # except Exception as e:
        #     print(str(e))

        try:
            self.cnxn = pyodbc.connect(
                'DRIVER=' + self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
            self.cursor = self.cnxn.cursor()
            strquery2 = "CREATE TABLE " + dbc.table + """ (Id INT NOT NULL IDENTITY,
                                                                            [tournament_endpoint] [text] DEFAULT NULL,
                                                                            [tournament_division_id] [text] DEFAULT NULL,
                                                                            [tournament_id] [text] DEFAULT NULL,
                                                                            [tournament_name] [text] DEFAULT NULL,
                                                                            [time_period] [text] DEFAULT NULL,
                                                                            [Location] [text] DEFAULT NULL,
                                                                            [tournament_division_name] [text] DEFAULT NULL,
                                                                            [last_update] [text] DEFAULT NULL,
                                                                            [game_date] [text] DEFAULT NULL,
                                                                            [game_id] [text] DEFAULT NULL,
                                                                            [game_time] [text] DEFAULT NULL,
                                                                            [location_name] [text] DEFAULT NULL,
                                                                            [away_team_id] [text] DEFAULT NULL,
                                                                            [away_team] [text] DEFAULT NULL,
                                                                            [away_score] [text] DEFAULT NULL,
                                                                            [home_score] [text] DEFAULT NULL,
                                                                            [home_team] [text] DEFAULT NULL,
                                                                            PRIMARY KEY ([Id]))"""
            self.cursor.execute(strquery2)
            self.cnxn.commit()
            print('Table Created.')
        except Exception as e:
            print(str(e))
    def process_item(self, item, spider):
        if isinstance(item, TourneymachineItem):
            try:
                self.cnxn = pyodbc.connect(
                    'DRIVER=' + self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
                self.cursor = self.cnxn.cursor()
                self.cursor.execute(
                        """INSERT INTO """ + dbc.table + "([tournament_endpoint], [tournament_division_id], [tournament_id], [tournament_name], [time_period], [Location], [tournament_division_name], [last_update], [game_date], [game_id], [game_time], [location_name], [away_team_id], [away_team], [away_score], [home_score], [home_team]) VALUES('"+item['tournament_endpoint']+"', '"+item['tournament_division_id']+"', '"+item['tournament_id']+"', '"+item['tournament_name']+"', '"+item['time_period']+"', '"+item['Location']+"', '"+item['tournament_division_name']+"', '"+item['last_update']+"', '"+item['game_date']+"', '"+item['game_id']+"', '"+item['game_time']+"', '"+item['location_name']+"', '"+item['away_team_id']+"', '"+item['away_team']+"', '"+item['away_score']+"', '"+item['home_score']+"', '"+item['home_team']+"')",
                        )
                self.cnxn.commit()
                # self.connection = MySQLdb.connect(self.DB_IP, self.DB_user, self.DB_password, self.DB_name,
                #                                   charset='utf8')
                # self.cursor = self.connection.cursor()
                # self.cursor.execute("set names utf8;")
                # self.cursor.execute(
                #     """INSERT INTO """ + dbc.table + """(tournament_endpoint, tournament_division_id, tournament_id, tournament_name, time_period, Location, tournament_division_name, last_update, game_date, game_id, game_time, location_name, away_team_id, away_team, away_score, home_score, home_team) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                #     (item['tournament_endpoint'], item['tournament_division_id'], item['tournament_id'], item['tournament_name'], item['time_period'],
                #      item['Location'], item['tournament_division_name'], item['last_update'], item['game_date'],
                #      item['game_id'], item['game_time'], item['location_name'], item['away_team_id'], item['away_team'], item['away_score'], item['home_score'],item['home_team']))
                # self.connection.commit()
                print('\rData inserted..' + str(self.i))
                self.i += 1

            except Exception as e:
                print(str(e))
            return item
