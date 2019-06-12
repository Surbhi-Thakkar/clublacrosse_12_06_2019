import pymysql as MySQLdb
import os
import pyodbc
import pandas as pd
from Tournaments.spiders import database_con as dbc
from Tournaments.spiders import paths

def Export_CSV():

    current_folder = os.path.dirname(os.path.abspath(__file__))
    csv_folder = current_folder+"/csv/"

    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    server = dbc.server
    database = dbc.database
    username = dbc.username
    password = dbc.password
    driver = dbc.driver
    table = dbc.table

    cnxn = pyodbc.connect(
        'DRIVER=' + driver + ';SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

    csv_Path = paths.csv_path+'tourneymachine_mainpage_data_01_05_2019.csv'

    try:
        # File_1 = csv_folder + "temp.csv"
        File_2 = csv_Path

        sql = "SELECT [Keyword],[Title],[Date],[Location],[Icon],[Link] FROM "+dbc.table

        df = pd.read_sql(sql,cnxn)
        # df.drop_duplicates(subset=None, inplace=True)
        # df.rename(columns={"page_url": "Page URL",'video_title':'Video Title','video_embed_link':'Video Embed link','thumbnail_images':'Thumbnail Images URL','category_tree':'Category Tree'}, inplace=True)
        df.drop_duplicates(subset=None, inplace=True)
        df.to_csv(File_2, index=False)

        print ("\nCSV genrated...")

    except Exception as e:
        print ("Cant Genrate csv : " + str(e))

# Export_CSV()