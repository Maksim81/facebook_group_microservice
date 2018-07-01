'''
Created on 14 Jun 2018

@author: MIkhail
'''
'''
Created on 13 Jun 2018

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
<<<<<<< HEAD
import requests , urlopen
from urllib.request import URLError
from urllib import request

=======
>>>>>>> 35b242137a39bc8ba295e99c205d21dae038bfed

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

<<<<<<< HEAD

=======
#conn = mysql.connector.connect(host = "localhost", user="root", passwd="", db="testdb",charset='utf8')
#cursor = conn.cursor()
#if conn.is_connected():
   # print("Connected to mysql Database")
>>>>>>> 35b242137a39bc8ba295e99c205d21dae038bfed
   
print("\tTest module 1  ")

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
<<<<<<< HEAD
#***************************************   
print("Set field from where to extract")

  
groupname = input("Enter group name: ")
try:
    req = request.Request(groupname)
except RuntimeError as e:
    raise
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
  #pause = input("enter value for scrooll delay")
except ValueError:
    print("You scroll delay set to  '"+pause+"'")
=======
    
print("Set field from where to extract")
groupname = input("Enter group name: ")
print("Set the delay for scroloing")
pause = input("set scrool delay: ")
>>>>>>> 35b242137a39bc8ba295e99c205d21dae038bfed
print("You programm has started")

usr = "mixanovatski13@gmail.com"
pwd = "devil6007472"

_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)

driver = webdriver.Firefox(firefox_profile=_browser_profile)

driver.maximize_window()


<<<<<<< HEAD
driver.get(groupname)
#driver.get("https://www.facebook.com/groups/364076470395469/members/")
#https://www.facebook.com/groups/1671435656214034/
#driver.get("https://www.facebook.com/groups/GamersDHC/members/")
=======

#driver.get("https://www.facebook.com/groups/364076470395469/members/")
#https://www.facebook.com/groups/867533693430451/members/
driver.get(groupname)
>>>>>>> 35b242137a39bc8ba295e99c205d21dae038bfed


assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.find_element_by_id('loginbutton').click()

<<<<<<< HEAD

pause = int(pause)
wait = WebDriverWait(driver, 100)
lastHeight = driver.execute_script("return document.body.scrollHeight")
print(lastHeight)
i = 1
#driver.get_screenshot_as_file("test03_1_"+str(i)+".jpg")
=======
pause = int(pause)
#pause = 3
wait = WebDriverWait(driver, 100)
lastHeight = driver.execute_script("return document.body.scrollHeight")
#print(lastHeight)
i = 1

>>>>>>> 35b242137a39bc8ba295e99c205d21dae038bfed

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(pause)
<<<<<<< HEAD
   
    try:
        newHeight = driver.execute_script("return document.body.scrollHeight")
    except:
        raise
=======
    
    newHeight = driver.execute_script("return document.body.scrollHeight")
>>>>>>> 35b242137a39bc8ba295e99c205d21dae038bfed
    
    if newHeight == lastHeight:
        break
    lastHeight = newHeight
    i += 1
    
page_source = driver.page_source

driver.close()
<<<<<<< HEAD

=======
>>>>>>> 35b242137a39bc8ba295e99c205d21dae038bfed
soup = BeautifulSoup(page_source,"lxml")
i = 1
for link in soup.findAll('a', {'class': '_60rg _8o _8r lfloat _ohe'}):
    r = link.get('href')
    #print(g)
    g = r.replace('\n','')
    z = g.replace('"','')
#print(g)
    h = z.replace("'", "")
    print(h)
<<<<<<< HEAD
    
    
    table_name = "test"
    createsqltable = """DROP TABLE IF EXISTS `table333`;
    CREATE TABLE IF NOT EXISTS `table333` (
    `id` int(11) NOT NULL DEFAULT '0',
    `plain_html` longtext,
    `extracted` mediumtext
     ) ENGINE=MyISAM DEFAULT CHARSET=latin1; """
    #cursor.execute(createsqltable)
    
    newquery ="INSERT IGNORE INTO  table333(id,extracted) VALUES("+str(i)+",'"+h+"')"
    cursor.execute(newquery,createsqltable,multi=True)
=======
    #newquery="UPDATE TABLE123 set extracted = '"+h+"' where id = "+str(i)
    newquery ="INSERT INTO  testdb.table234(id,extracted) VALUES("+str(i)+",'"+h+"')"
    cursor.execute(newquery)
>>>>>>> 35b242137a39bc8ba295e99c205d21dae038bfed
    
    conn.commit()
    i = i + 1

<<<<<<< HEAD
soup_str = str(soup)


g = soup_str.replace('\n','')
z = g.replace('"','')
#print(g)
h = z.replace("'", "")

=======
>>>>>>> 35b242137a39bc8ba295e99c205d21dae038bfed





   
