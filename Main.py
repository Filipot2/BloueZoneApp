from icalevents.icalevents import events
import mysql.connector
import variables

#Conection
cnx = mysql.connector.connect(**variables.config_connect)
cursor = cnx.cursor()

if cnx.is_connected():
    print("Connected to MySQL server")




