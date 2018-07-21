#This is short documenation about project.

#Description: Microservice allows to store facebook profiles in the MySQL database

Getting started: 

1. Download the file from out server 
2. Put neccessarry configurations (located on config.ini)
2.1 Set your database information and scroll delay
3. Enter the correct url for group users 
4. Put the correct table name where to store you users 
5. After you fish oll then the program will start(Wait patiently for it to finish and the you have it, all data is in you mysql database) 
6. The main programm where you can start you file is Console App.py. And the directory for exe file if dist 
Have Fun !!!!!! 
This is the version 0.003 
There will be more updates soon 
#If there is an error the program doesn't crash right away

Sample config
Here you can change the data to you own 

database = "MyDB"; #Name of your db
="" # "My group "Name 

host = localhost #name of you host
user = root #You user name
pass =  #and the password for you Mysql database
db = testdb # and the name of you db



Then set you scroll delay [pause] 
value = 3 # Set scroll delay 
# This value means how long will page wait before going down, you will have 3 seconds to wait. 
# Right now the min value for this is 3, if you want to go lover you are doing it at you own risk

db = testdb 
#Dont forget to chose you db name if you dont have one you can simply create it

For now this is the only configuration that you have to do
If you have any problems read help file











