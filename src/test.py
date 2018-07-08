'''
Created on 1 Jul 2018

@author: MIkhail
'''
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import selenium.webdriver.support.ui as ui
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from html.parser import HTMLParser
import mysql.connector
import configparser
import os
import requests , urlopen
from urllib.request import URLError
from urllib import request
import progressbar
from time import sleep
import sys
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import sqlite3
config = configparser.ConfigParser()
files = ['config.ini']
dataset = config.read(files)
if len(dataset) != len(files):
    raise ValueError("Failed to open/find all files")
   

conn = mysql.connector.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'])
cursor = conn.cursor()
if conn.is_connected():
    print(" Connected to mysql Database")
else:
    print("Connection is wrong")
table_name = "employee"
# delete 
cursor.execute("""DROP TABLE """+table_name+""";""")

sql_command = """
CREATE TABLE """+table_name+""" ( 
staff_number INTEGER PRIMARY KEY, 
fname VARCHAR(20), 
lname VARCHAR(30), 
gender CHAR(1), 
joining DATE,
birth_date DATE);"""

cursor.execute(sql_command)
print("Table created")

sql_command = """INSERT  INTO """+table_name+""" (staff_number, fname, lname, gender, birth_date)
    VALUES (2, "William", "Shakespeare", "m", "1961-10-25");"""
cursor.execute(sql_command)
print("Data inserted 1")

sql_command = """INSERT  INTO """+table_name+""" (staff_number, fname, lname, gender, birth_date)
    VALUES (1, "Frank", "Schiller", "m", "1955-08-17");"""
cursor.execute(sql_command)
print("Data inserted 2")

# never forget this, if you want the changes to be saved:
conn.commit()

conn.close()
