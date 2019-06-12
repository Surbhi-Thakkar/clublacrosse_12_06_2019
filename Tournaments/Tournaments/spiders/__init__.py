# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import os
import platform

current_directory = os.getcwd()
os_type = str(platform.system()).lower()

class paths:
    if "windows" in os_type:
        html_path = current_directory+'\\Html\\'
        if not os.path.exists(html_path):
            os.makedirs(html_path)

        csv_path = current_directory + '\\csv\\'
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)
    else:
        html_path = current_directory+'/Html/'
        if not os.path.exists(html_path):
            os.makedirs(html_path)

        csv_path = current_directory + '/csv/'
        if not os.path.exists(csv_path):
            os.makedirs(csv_path)