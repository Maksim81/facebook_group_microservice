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



print("\t Test module 1  ")
#print("    Please login to mysql server")
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
         #display_title_bar()
    
    # Let users know what they can do.
    print("\n[1] Start")
    print("[q] Quit.")
    
    
    if choice == '1':
        
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
            
            table_name = input("Enter group name: ")
            # delete 
            #cursor.execute("""DROP TABLE """+table_name+""";""")
                #print(h)
                
                
            sql_command = """
            CREATE TABLE """+table_name+""" ( 
            `id` int(11) NOT NULL DEFAULT '0',
            `plain_html` longtext,
            `extracted` mediumtext
            ) ENGINE=MyISAM DEFAULT CHARSET=latin1;"""
                 
            cursor.execute(sql_command)
            print("Table created")
            
            usr = "mixanovatski13@gmail.com"
            pwd = "devil6007472"
            
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
            print(lastHeight)
            i = 1
            #driver.get_screenshot_as_file("test03_1_"+str(i)+".jpg")
            
            while True:
                g =  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(pause)
                
                
                #i = 1
                
            
            # Initial call to print 0% progress
                
               
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
        
              
            print("\nI can't wait to meet this person!\n")
            
    elif choice == '2':
        try:
         groupname = input("Enter group name: ")
        except SyntaxError:
            groupname = None
        
        #id = is_valid('35701105226')
        #print(id)
        
           #id = is_valid(str(all))
           #print(id)
           #print(x)
           
           
            
           
           #id = is_valid(int(str(result)))
           #print(id)
           

           
        
           
    
        
        print("\nI can't wait to meet this person!\n")
    elif choice == '3':
        
        pause = input("set scrool delay: ")
        #for string in linkfromtable:
           #soup_string = str(string)
          # match = re.findall(r'[\w\.-]+@[\w\.-]+', soup_string)
           #print(match)
        print("\n+'"+pause+"'\n")
    elif choice == '4':  
          #i = 1
          #for string in linkfromtable:
             # newquery="UPDATE TABLE4 set extracted = '"+str(result)+"' where id = "+str(i)
              #cursor.execute(newquery)
              #conn.commit()
             # i = i + 1
             # print() 
             #conn = mysql.connector.connect(host = "localhost", user="root", passwd="", db="testdb",charset='utf8')
             #cursor = conn.cursor()
             #if conn.is_connected():
                #print("Connected to mysql Database")
            
             usr = "mixanovatski13@gmail.com"
             pwd = "devil6007472"
            
             _browser_profile = webdriver.FirefoxProfile()
             _browser_profile.set_preference("dom.webnotifications.enabled", False)
            
             driver = webdriver.Firefox(firefox_profile=_browser_profile)
            
             driver.maximize_window()
             
             #h = "https://www.facebook.com/groups/364076470395469/members/";
             
             driver.get(groupname)

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
             print(lastHeight)
             i = 1
            #driver.get_screenshot_as_file("test03_1_"+str(i)+".jpg")
            
             while True:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(pause)
                #page_source1 = driver.page_source
                #print(page_source1.encode("utf-8"))
                #print('*****************')
                #soup = BeautifulSoup(page_source1,"lxml")
                #for link in soup.findAll('a', {'class': '_60rg _8o _8r lfloat _ohe'}):
                    #r = link.get('href')
                    
                    #print(r)
                    
                    #g = r.replace('\n','')
                    #z = g.replace('"','')
            #print(g)
                    #h = z.replace("'", "")
                    #print(h)
                    
                    #newquery ="INSERT INTO  testdb.table555(id,extracted) VALUES("+str(i)+",'"+h+"')"
                    #cursor.execute(newquery)
                
                    #conn.commit()
                    #i = i + 1
                #insert into mysql data from last scroll 
                #create executed file 
                #create new table for each group 
                #driver.close()
                newHeight = driver.execute_script("return document.body.scrollHeight")
                ##print(newHeight)
                if newHeight == lastHeight:
                    break
                lastHeight = newHeight
                i += 1
                #driver.get_screenshot_as_file("test03_1_"+str(i)+".jpg")
             page_source = driver.page_source
            
             driver.close()
            #_60ri fsl fwb fcb
            #_60rg _8o _8r lfloat _ohe
            #soup = BeautifulSoup(page_source,"lxml").decode('unicode_escape').encode('ISO-8859-1','ignore').decode('utf8','ignore')
            #print(soup.encode("utf-8"))
            #for link in soup.findAll('a', {'class': '_sv4'}):
                #print(link.get('href'))
            #elem = soup.findAll('a', {'id': 'js_4n'})
            #print(elem)
            #parser = MyHTMLParser()
            #g = parser.feed(str(soup))
            #print(g)
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
                #newquery="UPDATE TABLE123 set extracted = '"+h+"' where id = "+str(i)
                newquery ="INSERT INTO  testdb.table234(id,extracted) VALUES("+str(i)+",'"+h+"')"
                cursor.execute(newquery)
                
                conn.commit()
                i = i + 1
            
             soup_str = str(soup)
            
            
             g = soup_str.replace('\n','')
             z = g.replace('"','')
            #print(g)
             h = z.replace("'", "")

              
             print("\nI can't wait to meet this person!\n")
    elif choice == 'q':
        
        print("\nThanks for playing. Bye.")
        print("--- %s seconds ---" % (time.time() - start_time))
    else:
        print("\nI didn't understand that choice.\n")
        

    
except ValueError as valerr:
    print(valerr)