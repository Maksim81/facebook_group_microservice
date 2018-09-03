import requests
from bs4 import BeautifulSoup
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
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
import os
import xmltodict
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import traceback
import random
import re
import mysql.connector


print("\tTest module 1  ")

config = configparser.ConfigParser()
files = ['config.ini']
dataset = config.read(files)
if len(dataset) != len(files):
    raise ValueError("Failed to open/find all files")

conn = mysql.connector.connect(host = "localhost", user="root", passwd="", db="testdb")
cursor = conn.cursor()
if conn.is_connected():
    print("Connected to mysql Database")
    
conn = mysql.connector.connect(host = config['mysqlDB']['host'],
                           user = config['mysqlDB']['user'],
                           passwd = config['mysqlDB']['pass'],
                           db = config['mysqlDB']['db'])
cursor = conn.cursor()
if conn.is_connected():
    print(" Connected to mysql Database")
else:
    print("Connection is wrong")
    
print("Set field from where to extract")

groupname = input("Enter group name: ")
#try:
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.107 Safari/537.36' }
req = request.Request(groupname)


usr = "mixanovatski13@gmail.com"
pwd = "devil6007472"

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
    
    
print("Set the delay for scroloing")
try:
  pause = config['pause']['value']
  print("You scroll delay set to  '"+pause+"'")
  #pause = input("enter value for scrooll delay")
except ValueError:
    print("You scroll delay set to  '"+pause+"'")
print("You programm has started please wait")

#table_name = 'test_Table'
table_name = input('Enter group name:')


#sql_command = """
#CREATE TABLE """+table_name+""" ( 
# `id` int(11) NOT NULL DEFAULT '0',
 # `plain_html` longtext,
 # `extracted` mediumtext,
#  PRIMARY KEY (`id`)
#) ENGINE=MyISAM DEFAULT CHARSET=latin1;"""

sql_command = """
CREATE TABLE """+table_name+""" ( 
`id` int(11) NOT NULL DEFAULT '0',
  `plain_html` longtext,
  `extracted` mediumtext
  
) ENGINE=MyISAM DEFAULT CHARSET=latin1;"""



cursor.execute(sql_command)
print("Table created")


#driver = None
#driver = webdriver.Firefox()
#driver.maximize_window()

links = []
#url = 'https://www.facebook.com/groups/364076470395469/members/'
#'https://www.facebook.com/groups/834886230029028/about/
#https://www.facebook.com/groups/834886230029028/members/
#'


_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)
        
driver = webdriver.Firefox(firefox_profile=_browser_profile)
        
driver.maximize_window()
driver.get(groupname)

assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.find_element_by_id('loginbutton').click()


sleep(1)

soup_fff = BeautifulSoup(driver.page_source,'lxml')
#entriess = soup_fff.select('div.clearfix > a')
entriess = soup_fff.select('div._60ri > a')
ss = [x.encode('utf-8') for x in entriess]
#print(ss)
urlss = re.findall(r'(https?://[^\s]+)', str(ss))
    #print(urls)
   
i = 1    
for se in urlss:
        #print(e)
        #i += 1
        us = str(se)
        #print(u)
    
        g = us.replace('\n','')
        z = g.replace('"','')
    #print(g)
        h = z.replace("'", "")
        
        #print(i,h)
        
        sql_command = "INSERT  INTO "+table_name+" (id,extracted) VALUES ("+str(i)+",'"+h+"');"
        cursor.execute(sql_command)
        print("Data inserted 1 :" + z)
        i += 1




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
        print(i,e)
        i += 1
    
    
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(1)
    print("Scroll")
        
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
        #print(e)
        #i += 1
        u = str(e)
        #print(u)
    
        g = u.replace('\n','')
        z = g.replace('"','')
    #print(g)
        h = z.replace("'", "")
        
        #print(i,h)
        
        sql_command = "INSERT  INTO "+table_name+" (id,extracted) VALUES ("+str(i)+",'"+h+"');"
        cursor.execute(sql_command)
        #print("Data inserted 1 :" + z)
        i += 1
        
        
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)        
        
      
        
    #sql_command = "INSERT  INTO testdb.cc_games (extracted) VALUES ('"+h+"');"
    #cursor.execute(sql_command)
    #print("Data inserted 1 :" + z)
               # if e['href'].strip() not in entries:
                #  links.append(e['href'])
                   #print(z)
    #i = 1               
    #for l in links:
       # print(i,l) 
       # i =+ 1         
    #print(links)
