# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as MySQLdb

from Tournaments.items import TournamentsItem
from Tournaments.spiders import database_con as dbc

class TournamentsPipeline(object):
    DB_IP = dbc.host
    DB_user = dbc.username
    DB_password = dbc.passwd
    DB_name = dbc.database
    i = 1

    def __init__(self):
        try:
            self.connection = MySQLdb.connect(self.DB_IP, self.DB_user, self.DB_password, charset='utf8')
            self.cursor = self.connection.cursor()
            self.cursor.execute('CREATE DATABASE if not exists ' + self.DB_name)
        except Exception as e:
            print(str(e))

        try:
            self.connection = MySQLdb.connect(self.DB_IP, self.DB_user, self.DB_password, self.DB_name, charset='utf8')
            self.cursor = self.connection.cursor()
            strquery2 = "CREATE TABLE if not exists " + dbc.table + """ (Id INT NOT NULL AUTO_INCREMENT,
                                                                                Keyword longtext DEFAULT NULL,
                                                                                Title longtext DEFAULT NULL,
                                                                                Date longtext DEFAULT NULL,
                                                                                Location longtext DEFAULT NULL,
                                                                                Icon longtext DEFAULT NULL,
                                                                                Link varchar(255) DEFAULT NULL,
                                                                                status longtext DEFAULT NULL,
                                                                                PRIMARY KEY (`Id`),
                                                                                UNIQUE (Link))"""
            self.cursor.execute(strquery2)
        except Exception as e:
            print(str(e))
    def process_item(self, item, spider):
        if isinstance(item, TournamentsItem):
            try:
                self.connection = MySQLdb.connect(self.DB_IP, self.DB_user, self.DB_password, self.DB_name,
                                                  charset='utf8')
                self.cursor = self.connection.cursor()
                self.cursor.execute("set names utf8;")
                self.cursor.execute(
                    """INSERT INTO """ + dbc.table + """(Keyword,Title,Date,Location,Icon,Link,status) VALUES(%s, %s, %s, %s, %s, %s, %s)""",
                    (item['Keyword'],item['Title'],item['Date'], item['Location'], item['Icon'], item['Link'],item['status']))
                self.connection.commit()
                print('\rData inserted..' + str(self.i), end = "")
                self.i += 1

            except Exception as e:
                print(str(e))
            return item
        # return item
