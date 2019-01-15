import time

import mysql.connector
import configparser

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys


def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute( """
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format( tablename.replace( '\'', '\'\'' ) ) )
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False


def hold_screen(exc_type, exc_value, tb):
    import traceback
    traceback.print_exc( exc_type, exc_value, tb )
    input( "Press key to exit" )
    sys.exit( -1 )


config = configparser.ConfigParser()
file = ["/Users/mikhailnovatskiy/PycharmProjects/Facebook_User_Data/src/dist/config.ini"]
datainput = config.read( file )
if len( datainput ) != len( file ):
    raise ValueError( "Failed to find file" )
else:
    print( "Config file is ready to use" )

host = config['mysqlDB']['host']
port = config['mysqlDB']['port']
usr = config['mysqlDB']['user']
pas = config['mysqlDB']['pass']
db = config['mysqlDB']['db']
mysql_table = config['mysql_table']['table']
group_name = config['Link']['link']
facebook_usr = config['user']['mail']
facebook_pwd = config['user']['password']
pause = config['pause']["value"]

config = {

    'user': "" + usr + "",
    'password': "" + pas + "",
    'host': "" + host + "",
    'port': "" + port + "",
    'database': "" + db + "",
    'raise_on_warnings': True,
}

link = mysql.connector.connect( **config )
cursor = link.cursor()

if link.is_connected():
    print( " Connection to mysql database was successful " )
else:
    print( " Connection to mysql database failed " )

check_table = checkTableExists( link, mysql_table )
if check_table is True:
    print( " Table exist" )
    print( " Pleace rename you table and start this programm all over again  " )
    sys.excepthook = hold_screen

    # _browser_profile = webdriver.FirefoxProfile()
    # _browser_profile.set_preference( "dom.webnotifications.enabled", False )

    # driver = webdriver.Firefox( _browser_profile )

    # driver.maximize_window()

    # driver.get( group_name )

    # assert "Facebook" in driver.title
    # elem = driver.find_element_by_id( "email" )
    # elem.send_keys( facebook_usr )
    # elem = driver.find_element_by_id( "pass" )
    # elem.send_keys( facebook_pwd )
    # elem.send_keys( Keys.RETURN )
    # driver.find_element_by_id( 'loginbutton' ).click()

    # time.sleep( int( pause ) )
    # last_height = driver.execute_script( "return document.body.scrollHeight" )
    # i = 1
    # while True:
    # plain_code_before_scroll = driver.page_source

    # upper_soup = BeautifulSoup( plain_code_before_scroll, 'html.parser' )
    # links_from_start = [a['href'] for div in upper_soup.find_all( "div", attrs={"class": "_60ri"} ) for a in
    # div.find_all( 'a' )]

    # time.sleep( int( pause ) )

    # first_scroll = driver.execute_script( "window.scrollTo(0, document.body.scrollHeight);" )
    # time.sleep( int( pause ) )

    # plain_code_before_scroll = driver.page_source

    # new_user_soup = BeautifulSoup( plain_code_before_scroll, 'html.parser' )
    # links_for_new_user = [a['href'] for div in new_user_soup.find_all( "div", attrs={"class": "_60ri"} ) for a in
    # div.find_all( 'a' )]

    # execute_duplicates = list( set( links_for_new_user ) - set( links_from_start ) )
    # for dublicates in execute_duplicates:
    # print(i, "Scanning links " + dublicates )
    # i += 1

    # new_height = driver.execute_script( "return document.body.scrollHeight" )

    # if new_height == last_height:
    # break
    # last_height = new_height

    # plain_code = driver.page_source
    # html_soup = BeautifulSoup( plain_code, 'html.parser' )
    # links_from_soup = [a['href'] for div in html_soup.find_all( "div", attrs={"class": "_60ri"} ) for a in
    # div.find_all( 'a' )]
    # print(links_from_soup)
    # driver.close()

    # cursor.execute( "SELECT extracted FROM cccc_facebook" )
    # table_data = cursor.fetchall()
    # data_from_db_1 = [x[0] for x in table_data]
    # print( data_from_db_1 )
    # i = 1
    # a = [1,2,3,4,5,6]
    # b = [1,7,4,6,8,9,0]

    # remove_duplicates = [i for i in a if i not in b]

    # print(remove_duplicates)
    # for deleted in remove_duplicates:
    # if not deleted:
    # print("No NEW users found ")

    # else:
    # print("New users found")
    # i += 1

    # print( data_from_db_1 )
    # i = 1
    # for d in data_from_db_1:
    # print( i, d )
    # i += 1

    # zs = ( set( data_from_db_2) - ( set( data_from_db_1) ) )

    # i = 1
    # for z in zs:
    # print( i, z )
    # i += 1

elif check_table is False:
    print( " Table is missing" )
    print( " New table will be created " )

    sql_command_create_table = """ 
    CREATE TABLE """ + mysql_table + """ (
      `id` int(11) NOT NULL DEFAULT '0',
      `plain_html` longtext,
      `extracted` mediumtext,
      PRIMARY KEY (`id`),
      UNIQUE KEY `id_UNIQUE` (`id`)
    ) ENGINE=MyISAM DEFAULT CHARSET=latin1"""

    cursor.execute( sql_command_create_table )
    print( " Table created """ + mysql_table + "" )

    _browser_profile = webdriver.FirefoxProfile()
    _browser_profile.set_preference( "dom.webnotifications.enabled", False )

    driver = webdriver.Firefox( _browser_profile )

    driver.maximize_window()

    driver.get( group_name )

    assert "Facebook" in driver.title
    elem = driver.find_element_by_id( "email" )
    elem.send_keys( facebook_usr )
    elem = driver.find_element_by_id( "pass" )
    elem.send_keys( facebook_pwd )
    elem.send_keys( Keys.RETURN )
    driver.find_element_by_id( 'loginbutton' ).click()

    time.sleep( int( pause ) )

    # Get scroll height
    # last_height = driver.execute_script( "return document.body.scrollHeight" )
    i = 1
    while True:

        plain_code_before_scroll = driver.page_source

        upper_soup = BeautifulSoup( plain_code_before_scroll, 'html.parser' )
        links_from_start = [a['href'] for div in upper_soup.find_all( "div", attrs={"class": "_60ri"} ) for a in
                            div.find_all( 'a' )]

        # Wait for page to load
        time.sleep( int( pause ) )

        # Scroll down to bottom
        driver.execute_script( "window.scrollTo(0, document.body.scrollHeight);" )

        # Wait to load page
        time.sleep( int( pause ) )

        # Get page sourse code
        plain_code_after_scroll = driver.page_source

        middle_soup = BeautifulSoup( plain_code_after_scroll, 'html.parser' )
        links_from_first_scroll = [a['href'] for div in middle_soup.find_all( "div", attrs={"class": "_60ri"} ) for a in
                                   div.find_all( 'a' )]

        execute_duplicates = list( set( links_from_first_scroll ) - set( links_from_start ) )

        for e in execute_duplicates:
            string_convert = str( e )
            first_replace = string_convert.replace( '\n', '' )
            second_replace = first_replace.replace( '"', '' )
            final_replace = second_replace.replace( "'", "" )
            sql_command_insert = "INSERT  INTO " + mysql_table + " (id,extracted) VALUES (" + str(
                i ) + ",'" + final_replace + "');"
            cursor.execute( sql_command_insert )
            print( "Got link " + final_replace )
            i += 1

        # Calculate new scroll height and compare with last scroll height
        # new_height = driver.execute_script( "return document.body.scrollHeight" )
        # if new_height == last_height:
        # break
    # last_height = new_height
    # sys.excepthook = hold_screen
    driver.close()

    # i = 1
    # while True:

    # plain_code_before_scroll = driver.page_source

    # upper_soup = BeautifulSoup( plain_code_before_scroll, 'html.parser' )
    # links_from_start = [a['href'] for div in upper_soup.find_all( "div", attrs={"class": "_60ri"} ) for a in
    # div.find_all( 'a' )]

    # time.sleep( int( pause ) )

    # second_scroll = driver.execute_script( "window.scrollTo(0, document.body.scrollHeight);" )
    # time.sleep( int( pause ) )

    # plain_code_after_scroll = driver.page_source

    # middle_soup = BeautifulSoup( plain_code_after_scroll, 'html.parser' )
    # links_from_first_scroll = [a['href'] for div in middle_soup.find_all( "div", attrs={"class": "_60ri"} ) for a in
    #  div.find_all( 'a' )]

    # execute_duplicates = list( set( links_from_first_scroll ) - set( links_from_start ) )

    # for e in execute_duplicates:
    # string_convert = str( e )
    #  first_replace = string_convert.replace( '\n', '' )
    #   second_replace = first_replace.replace( '"', '' )
    #  final_replace = second_replace.replace( "'", "" )
    #  sql_command_insert = "INSERT  INTO " + mysql_table + " (id,extracted) VALUES (" + str(
    #      i ) + ",'" + final_replace + "');"
    #  cursor.execute( sql_command_insert )
    #  print( "Got link" + final_replace )
    #  i += 1

    # driver.close()
