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

from urllib.request import URLError
from urllib import request
#import progressbar
from time import sleep
import sys
#from django.core.validators import URLValidator
#from django.core.exceptions import ValidationError

#from src.exceptions import *

import datetime

#start_time = time.time()

#def url_ok(url):
   # r = requests.head(url)
   # return r.status_code == 200
#class MyHTMLParser(HTMLParser):

   # def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
      #  if tag == "a":
           # Check the list of defined attributes.
         #  for name, value in attrs:
               # If href is defined, print it.
          #     if name == "href":
           #        print(name, "=", value)

#class MLStripper(HTMLParser):
    #def __init__(self):
    #    self.reset()
    #    self.strict = False
     #   self.convert_charrefs= True
     #   self.fed = []
  #  def handle_data(self, d):
    #    self.fed.append(d)
   # def get_data(self):
      #  return ''.join(self.fed)


#def strip_tags(html):
  #  s = MLStripper()
   # s.feed(html)
   # return s.get_data()
   
def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

sys.excepthook = show_exception_and_exit

print("\t Facebook User data ")
config = configparser.ConfigParser()
files = ['config.ini']
dataset = config.read(files)
if len(dataset) != len(files):
            raise ValueError("Failed to open/find all files")
else:
    print(" File found")


print(" Select default acoount or use you own ")
print(" Please answer witch(Yes or no)")

yes = {'yes','y', 'ye', ''}
no = {'no','n'}

choice = input().lower()
if choice in yes:
   print(" Please enter you data: ")
   usr = input("Enter facebook user name: ")
   pwd = input("Enter facebook user password: ")
   print(" Data fill complete")
elif choice in no:
   print(" You have chose our accaunt ")
   usr =  config['user']['mail']
   pwd =  config['user']['password']
else:
   sys.stdout.write("Please respond with 'yes' or 'no' :") 
   
   
configMysql = {
  'user': 'root',
  'password': 'root',
  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
  'database': 'testdb',
  'raise_on_warnings': True,
}

link = mysql.connector.connect(**configMysql)
cursor = link.cursor()



#conn = mysql.connector.connect(**config)
#cursor = conn.cursor()
if link.is_connected():
      print("Connected to mysql Database")
else:
        print("Connection is wrong") 
        

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
        
        
        # delete 
        #cursor.execute("""DROP TABLE """+table_name+""";""")
            #print(h)
            
            
        #sql_command = """
        #CREATE TABLE """+table_name+""" ( 
        #`id` int(11) NOT NULL DEFAULT '0',
        #`plain_html` longtext,
        #`extracted` mediumtext
        #) ENGINE=MyISAM DEFAULT CHARSET=latin1;"""
        
        #sql_command = """
        #CREATE TABLE """+table_name+""" ( 
         #`id` int(11) NOT NULL DEFAULT '0',
         # `plain_html` longtext,
          #`extracted` mediumtext,
         # PRIMARY KEY (`id`)
        #) ENGINE=MyISAM DEFAULT CHARSET=latin1;"""
        
        
         
       # sys.excepthook = show_exception_and_exit     
        #cursor.execute(sql_command)
        #print("Table created")
        print("Scrolind process have start")
        
        
        
        _browser_profile = webdriver.FirefoxProfile()
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        
        driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',firefox_profile=_browser_profile)
        
        driver.maximize_window()
        
        #groupname = "https://www.facebook.com/groups/GamersDHC/members/" 
        groupname = config['siteLink']['link']
        print("Group name from file selected : "+groupname)
        driver.get(groupname)
        #driver.get("https://www.facebook.com/groups/364076470395469/members/")
        #https://www.facebook.com/groups/1671435656214034/
        #driver.get("https://www.facebook.com/groups/GamersDHC/members/")
        sys.excepthook = show_exception_and_exit
        
        assert "Facebook" in driver.title
        elem = driver.find_element_by_id("email")
        elem.send_keys(usr)
        elem = driver.find_element_by_id("pass")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.find_element_by_id('loginbutton').click()
        
        
        pause = 3
        wait = WebDriverWait(driver, 100)
        lastHeight = driver.execute_script("return document.body.scrollHeight")
        #print(lastHeight)
        i = 1
        #driver.get_screenshot_as_file("test03_1_"+str(i)+".jpg")
        
        while True:
            
                soup_ff = BeautifulSoup(driver.page_source,'lxml')
                        #entries = soup_ff.select('div.clearfix > a')
                entries = soup_ff.select('div._60ri > a')
                s = [x.encode('utf-8') for x in entries]
                        #print(s)
                urls = re.findall(r'(https?://[^\s]+)', str(s))
                        #print(urls)
                i = 1    
                for e in urls:
                            #print(i,e)
                            i += 1
                g =  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(pause)
                        
                soup_gg = BeautifulSoup(driver.page_source, 'lxml')
                        #entries = soup_gg.select('div.clearfix > a')
                entries = soup_gg.select('div._60ri > a')
                g = [x.encode('utf-8') for x in entries]
                        #print(g)
                _urls = re.findall(r'(https?://[^\s]+)', str(g))
                        #print(_urls)
                i = 1    
                for e in _urls:
                            #print(i,e)
                            i += 1
                z = list(set(_urls) - set(urls))
                i = 1    
                for e in z:
                            #print(i,e)
                            #i += 1
                    u = str(e)
                            #print(u)
                        
                    g = u.replace('\n','')
                    p = g.replace('"','')
                        #print(g)
                    h = p.replace("'", "")
                    #table =  config['table']['testdb.cccc_facebook']       
                    sql_command = "INSERT  INTO testdb.cccc_facebook (id,extracted) VALUES ("+str(i)+",'"+h+"');"
                    cursor.execute(sql_command)
                            
                    print("Data inserted  :" + h)
                    i += 1
            
                
            
            
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
        
        #driver.close()
        driver.execute_script("window.scrollTo(0, 0);")
        entries = soup_gg.select('div._60ri > a')
        g = [x.encode('utf-8') for x in entries]
        facebook_urls = re.findall(r'(https?://[^\s]+)', str(g))
        print(facebook_urls)
        
        cursor = link.cursor()
        cursor.execute("SELECT extracted FROM testdb.cc_facebook;")
        results = cursor.fetchall()
        mysqllinks = [x for x in results]
         
        #g = auto.replace('(','')

        #p = g.replace(')','')
        print(mysqllinks)
        
        
        
        #sys.excepthook = show_exception_and_exit
        #soup = BeautifulSoup(page_source,"lxml")
        #i = 1
        #for link in soup.findAll('a', {'class': '_60rg _8o _8r lfloat _ohe'}):
            #r = link.get('href')
            #print(g)
            #g = r.replace('\n','')
            #z = g.replace('"','')
        #print(g)
            #h = z.replace("'", "")
            
            
            #sys.excepthook = show_exception_and_exit
            #sql_command = "INSERT  INTO "+table_name+" (id,extracted) VALUES ("+str(i)+",'"+h+"');"
            #cursor.execute(sql_command)
            #print("Data inserted 1 :" + h)
            
            
            
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
            #i = i + 1
        
        #soup_str = str(soup)
        
        sys.excepthook = show_exception_and_exit
        #g = soup_str.replace('\n','')
        #z = g.replace('"','')
        #print(g)
        #h = z.replace("'", "")

        
        
        
      
                
       
       
       
    
        print("\nData added to mysql database! \n")
    elif choice == 'q':
        sys.excepthook = show_exception_and_exit
        print("\nThanks for playing. Bye.")
        #print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("\nI didn't understand that choice.\n")
        

    
except my.Error as e:
    print(e)