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
import numpy

#from src.exceptions import *
import difflib
#from src import driver
d = difflib.Differ()
import datetime
#start_time = time.time()


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
   sr =  config['user']['mail']
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
    
       choice = ''
       while choice != 'q':    
            
        print("\n[1] Start programm.")
        print("[q] Quit.")
        
        choice = input("What would you like to do? ")
        
        if choice == '1': 
            
            

            usr =  config['user']['mail']
            pwd =  config['user']['password']
            
            
            groupname = config['siteLink']['link']
            print("Group name from file selected : "+groupname)
            #url = 'https://www.facebook.com/groups/364076470395469/members/'  
            
            pause = config['pause']['value']
            print("Scroll dalay from config file : "+pause) 
            pause = int(pause)
            
               
                    
                    
            _browser_profile = webdriver.FirefoxProfile()
            _browser_profile.set_preference("dom.webnotifications.enabled", False)
            #_browser_profile.set_preference("network.cookie.cookieBehavior", 2)
            _browser_profile.cookies_enabled = False
                    
            #driver = webdriver.Firefox(firefox_profile=_browser_profile)
            driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver',firefox_profile=_browser_profile)
                    
            driver.maximize_window()
            
            driver.get(groupname)
            
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
                    
                   
                    
                    
            #pause = 1
            wait = WebDriverWait(driver, 100)
            time.sleep(pause)
                  
            lastHeight = driver.execute_script("return document.body.scrollHeight")
            
            
            
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
                            
                    sql_command = "INSERT  INTO testdb.cc_facebook (id,extracted) VALUES ("+str(i)+",'"+h+"');"
                    cursor.execute(sql_command)
                            
                    print("Data inserted  :" + h)
                    i += 1
                            
                new_height = driver.execute_script("return document.body.scrollHeight")
                
                
                if new_height == lastHeight:
                        break
                last_height = new_height
            
            #driver.close()
            driver.execute_script("window.scrollTo(0, 0);")
            entries = soup_gg.select('div._60ri > a')
            g = [x.encode('utf-8') for x in entries]
            print(g)
            _urls = re.findall(r'(https?://[^\s]+)', str(g))
            #print(_urls)
            i = 1    
            for e in _urls:
                    #print(e)
                    #i += 1
                    u = str(e)
                    #print(u)
                
                    g = u.replace('\n','')
                    p = g.replace('"','')
                #print(g)
                    h = p.replace("'", "")
                            
                            
            #cursor.execute("SELECT extracted FROM testdb.cc_facebook;")
                              # use fetchall to get all the return results which is a list object
            #result_set = cursor.fetchall()
                            #print(result_set)  
            #extracted_result = [x for x in result_set]
                            #print(extracted_result)
                                
            cursor.execute("SELECT extracted FROM testdb.cc_facebook;")
                              # use fetchall to get all the return results which is a list object
            result_set = cursor.fetchall()
                            #print(result_set)  
            auto = [x for x in result_set]  
                            #print(auto)  
                            #i = 1    
                            #for e in _urls:
                                    #print(i,e)
                                   # i += 1
                            
            zs = list(set(g) - set(auto))
            print("New users"+str(zs))
            i = 1
            for e in zs:
                                    #print(i,e)
                i += 1
                            
        elif choice == 'q':
                    #sys.excepthook = show_exception_and_exit
                    print("\nThanks for playing. Bye.")
                        #print("--- %s seconds ---" % (time.time() - start_time))
        else:
                    print("\nI didn't understand that choice.\n")           
                        
                        
except mysql.connector.Error as e:
    print(e)     