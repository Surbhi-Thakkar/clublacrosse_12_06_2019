# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as MySQLdb
import pyodbc
from Tournaments.items import TournamentsItem
from Tournaments.spiders import database_con as dbc

class TournamentsPipeline(object):
    server = dbc.server
    database = dbc.database
    username = dbc.username
    password = dbc.password
    driver = dbc.driver
    table = dbc.table
    i = 1

    def __init__(self):
        try:
            self.cnxn = pyodbc.connect(
                'DRIVER=' + self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
            # self.cursor = self.cnxn.cursor()
            # self.cursor.execute('CREATE DATABASE '+self.database)
        except Exception as e:
            print(str(e))

        try:

            self.cnxn = pyodbc.connect('DRIVER=' + self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
            self.cursor = self.cnxn.cursor()

            qry1 = "CREATE TABLE "+self.table+""" ([Id] INT NOT NULL IDENTITY,
                                                        [Keyword] [text] NOT NULL,
                                                        [Title] [text] NOT NULL,
                                                        [Date] [text] NOT NULL,
                                                        [Location] [text] NULL,
                                                        [Icon] [text] NULL,
                                                        [Link] [varchar](250) NULL UNIQUE,
                                                        PRIMARY KEY([Id])
                                                    )"""

            self.cursor.execute(qry1)
            self.cnxn.commit()
            print('Table Created')

        except Exception as e:
            print(str(e))
    def process_item(self, item, spider):
        if isinstance(item, TournamentsItem):
            try:
                self.cnxn = pyodbc.connect(
                    'DRIVER=' + self.driver + ';SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
                self.cursor = self.cnxn.cursor()
                self.cursor.execute("INSERT INTO "+dbc.table+" ([Keyword],[Title],[Date],[Location],[Icon],[Link]) VALUES ('"+str(item['Keyword'])+"', '"+str(item['Title'])+"', '"+str(item['Date'])+"', '"+str(item['Location'])+"', '"+str(item['Icon'])+"', '"+str(item['Link'])+"')")
                self.cnxn.commit()
                print('\rData Inserted.'+str(self.i))
                self.i += 1
            except Exception as e:
                print(str(e))
            return item
        # return item
