from icalevents.icalevents import events
import mysql.connector
import variables
import functions


#Conection
cnx = mysql.connector.connect(**variables.config_connect)
cursor = cnx.cursor()

if cnx.is_connected():
    functions.update_database()




