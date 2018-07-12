import re
import nltk
import requests
from html.parser import HTMLParser
from bs4 import BeautifulSoup
from nameparser.parser import HumanName
import html
import numpy as np
import mysql.connector
from array import array
from pydoc import plain
import requests
import bs4
from bs4 import BeautifulSoup
import time
import mysql.connector as my
from time import sleep
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

#from src.exceptions import *

import datetime
start_time = time.time()

def url_ok(url):
    r = requests.head(url)
    return r.status_code == 200
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   print(name, "=", value)

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



print("\t Test module 1  ")
print(" Use defaul user or create you own user[yes/no] ")

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

choice = input().lower()
if choice in yes:
   print("please enter you data: ")
   usr = input("Enter facebook user name: ")
   pwd = input("Enter facebook user password: ")
elif choice in no:
   print("you selecter our own acount: ")
   usr = "mixanovatski13@gmail.com"
   pwd = "devil6007472"
else:
   sys.stdout.write("Please respond with 'yes' or 'no'")
#print("\n")
#print("To connect to mysql server please fill all filed's")
#h = input("Hostname: ")
#u = input("User: ")
#p = input("Password: ")
#d = input("Database: ")
#print(h,u,p,d)
try:
   #conn = my.connect(host = h, user= u, passwd=p, db=d)
   #conn = mysql.connector.connect(user="root", passwd="devil6007472", db="testdb")
   #cursor = conn.cursor()
   #if conn.is_connected():
     # print("Connected to mysql Database")
      
   choice = ''
   while choice != 'q':    
        
    print("\n[1] Start programm.")
    print("[q] Quit.")
    
    choice = input("What would you like to do? ")
    
    if choice == '1':
        
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
        #***************************************   
        print("Set field from where to extract")
        
          
        groupname = input("Enter group name: ")
        #try:
        headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36' }
        req = request.Request(groupname)
        
        
        
        #except ValidationError as e:
            #print(e)
        try:
            response = request.urlopen(req)
        except URLError  as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server.')
                print('Reason: '), e.reason
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request.')
                print('Error code: '), e.code
        else:
            print('URL is good!')
        
        #***************************************
        print("Set the delay for scroloing")
        try:
          pause = config['pause']['value']
          print("You scroll delay set to  '"+pause+"'")
          #pause = input("enter value for scrooll delay")
        except ValueError:
            print("You scroll delay set to  '"+pause+"'")
        print("You programm has started please wait")
        
        table_name = input('Enter table name:')
        # delete 
        #cursor.execute("""DROP TABLE """+table_name+""";""")
            #print(h)
            
            
        #sql_command = """
        #CREATE TABLE """+table_name+""" ( 
        #`id` int(11) NOT NULL DEFAULT '0',
        #`plain_html` longtext,
        #`extracted` mediumtext
        #) ENGINE=MyISAM DEFAULT CHARSET=latin1;"""
        
        sql_command = """
        CREATE TABLE """+table_name+""" ( 
         `id` int(11) NOT NULL DEFAULT '0',
          `plain_html` longtext,
          `extracted` mediumtext,
          PRIMARY KEY (`id`)
        ) ENGINE=MyISAM DEFAULT CHARSET=latin1;"""
        
        
         
             
        cursor.execute(sql_command)
        print("Table created")
        print("Scrolind process have start")
        
        
        
        _browser_profile = webdriver.FirefoxProfile()
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        
        driver = webdriver.Firefox(firefox_profile=_browser_profile)
        
        driver.maximize_window()
        
        
        driver.get(groupname)
        #driver.get("https://www.facebook.com/groups/364076470395469/members/")
        #https://www.facebook.com/groups/1671435656214034/
        #driver.get("https://www.facebook.com/groups/GamersDHC/members/")
        
        
        assert "Facebook" in driver.title
        elem = driver.find_element_by_id("email")
        elem.send_keys(usr)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.find_element_by_id('loginbutton').click()
        
        
        pause = int(pause)
        wait = WebDriverWait(driver, 100)
        lastHeight = driver.execute_script("return document.body.scrollHeight")
        #print(lastHeight)
        i = 1
        #driver.get_screenshot_as_file("test03_1_"+str(i)+".jpg")
        
        while True:
            g =  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause)
            
            
        # Initial call to print 0% progress
            print("Data added to mysql database")
            
           
            try:
                newHeight = driver.execute_script("return document.body.scrollHeight")
            except:
                raise
            
            if newHeight == lastHeight:
                break
            lastHeight = newHeight
            i += 1
            
        page_source = driver.page_source
        
        driver.close()
        
        
        
        
        soup = BeautifulSoup(page_source,"lxml")
        i = 1
        for link in soup.findAll('a', {'class': '_60rg _8o _8r lfloat _ohe'}):
            r = link.get('href')
            #print(g)
            g = r.replace('\n','')
            z = g.replace('"','')
        #print(g)
            h = z.replace("'", "")
            
            
            
            sql_command = "INSERT  INTO "+table_name+" (id,extracted) VALUES ("+str(i)+",'"+h+"');"
            cursor.execute(sql_command)
            print("Data inserted 1 :" + h)
            
            
            
            #createsqltable = """"DROP TABLE IF EXISTS '"""+table_name+"""';
            #CREATE TABLE IF NOT EXISTS '"""+table_name+"""' (
            #`id` int(11) NOT NULL DEFAULT '0',
            #`plain_html` longtext,
            #`extracted` mediumtext
            # ) ENGINE=MyISAM DEFAULT CHARSET=latin1; """
            #cursor.execute(createsqltable)
            #print("table created",createsqltable)
            
            #newquery ="INSERT IGNORE INTO  "+table_name+"(id,extracted) VALUES("+str(i)+",'"+h+"')"
            #cursor.execute(createsqltable,newquery)
           # print("data inserted")
            
            #conn.commit()
            i = i + 1
        
        soup_str = str(soup)
        
        
        g = soup_str.replace('\n','')
        z = g.replace('"','')
        #print(g)
        h = z.replace("'", "")

        
        
        
      
                
       
       
       
    
        print("\nData added to mysql database! \n")
    elif choice == 'q':
        
        print("\nThanks for playing. Bye.")
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("\nI didn't understand that choice.\n")
        

    
except my.Error as e:
    print(e)