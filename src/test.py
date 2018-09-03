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
import numpy

#from src.exceptions import *
import difflib
d = difflib.Differ()
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

usr = "mixanovatski13@gmail.com"
pwd = "devil6007472"
url = 'https://www.facebook.com/groups/364076470395469/members/'      
        
        
_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)
        
driver = webdriver.Firefox(firefox_profile=_browser_profile)
        
driver.maximize_window()

driver.get(url)

assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(usr)
elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)
elem.send_keys(Keys.RETURN)
driver.find_element_by_id('loginbutton').click()
        
        

        #driver.get("https://www.facebook.com/groups/364076470395469/members/")
        #https://www.facebook.com/groups/1671435656214034/
        #driver.get("https://www.facebook.com/groups/GamersDHC/members/")
        #https://www.facebook.com/groups/413675908981726/members/
        
       
        
        
pause = 3
wait = WebDriverWait(driver, 100)
time.sleep(pause)
        
lastHeight = driver.execute_script("return document.body.scrollHeight")
        #print(lastHeight)
i = 1
        #driver.get_screenshot_as_file("test03_1_"+str(i)+".jpg")
        

page_source = driver.page_source 
soup1 = BeautifulSoup(page_source,"lxml")
soup_string2 = str(soup1)

    
           #print(r)
        #a = numpy.ndarray(int(r))
        #t = buffer(page_source)
g =  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
print("page loaded")
sleep(2)
page_source = driver.page_source  
soup2 = BeautifulSoup(page_source,"lxml")
soup_string2 = str(soup2)




        
        
        
           #print(r)
        #b = numpy.ndarray(int(r)) 
        #result_scroll = numpy.ndarray(rs - rz)
        #print()
           
        #time.sleep(10)
        #page_source = driver.page_source   
            
        # Initial call to print 0% progress
        #print("Collecting data(List growing)")
            
           
#try:
              #  newHeight = driver.execute_script("return document.body.scrollHeight")
#except:
             #   raise
            
#if newHeight == lastHeight:
    #    break
#lastHeight = newHeight
#i += 1
            
        #page_source = driver.page_source
        
        #gs = page_source.replace('\n','')
        #zs = gs.replace('"','')
        #print(g)
        #hs = zs.replace("'", "")
        
        #print(hs)
        #sql_command = "INSERT  INTO "+table_name+" (plain_html) VALUES ('"+hs+"');"
        #cursor.execute(sql_command)
        #print("Data inserted 1 :" + hs)
        
        #driver.close()
        
        
        
        
        #soup = BeautifulSoup(page_source,"lxml")
        #i = 1
        #for link in soup.findAll('a', {'class': '_60rg _8o _8r lfloat _ohe'}):
           # r = link.get('href')
            #print(g)
            #g = r.replace('\n','')
            #z = g.replace('"','')
        #print(g)
           # h = z.replace("'", "")
            
            
            
            #sql_command = "INSERT  INTO "+table_name+" (id,extracted) VALUES ("+str(i)+",'"+h+"');"
            #cursor.execute(sql_command)
           # print("Data inserted 1 :" + h)
            
            
            
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
        
        
        #g = soup_str.replace('\n','')
        #z = g.replace('"','')
        #print(g)
        #h = z.replace("'", "")

        
    #elif choice == '2':   
       # cursor.execute("SELECT plain_html FROM "+table_name+" where id = 1")

       # linkfromtable = list(cursor.fetchall())
       # i = 1
        #for string in linkfromtable:
           # soup_string = str(string)
            #print(soup_string)
           # soup = BeautifulSoup(soup_string,"lxml")
        # it will cover all cases id="p4423234" id="p5547" id="p4124234" id="234"
        
            #a =  soup.find_all('a', attrs={'id': re.compile('^p?\d+$')})
            #for i in a:
                #print(i['href'])
           # i = 1
            #for link in soup.findAll('a', {'class': '_60rg _8o _8r lfloat _ohe'}):
              #  r = link.get('href')
              #  print(r)
        
      
                
       
       
       
    
        