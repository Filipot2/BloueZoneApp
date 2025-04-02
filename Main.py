import mysql.connector
from lecture_manager.utils import functions, variables

#Conection
cnx = mysql.connector.connect(**variables.config_connect)
cursor = cnx.cursor()

if cnx.is_connected():
    functions.update_database()




