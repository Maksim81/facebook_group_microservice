import configparser
#import MySQLdb.cursors
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

print("\tTest module 1  ")
config = configparser.ConfigParser()
config.read('config.ini')

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
print("Set the delay for scroloing")
pause = input("set scrool delay: ")
print("You programm has started")
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


