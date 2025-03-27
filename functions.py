from icalevents.icalevents import events
import mysql.connector
import variables

#updates database if there are new events
def update_database():
    #Conection
    cnx = mysql.connector.connect(**variables.config_connect)
    cursor = cnx.cursor()

    ical_url = "https://is.muni.cz/calendar/ical/Zmnh4Apy4d5QQAsRYK7Vdw_T"
    my_events = events(ical_url)

    for event in my_events:

        naive_start = event.start.replace(tzinfo=None)
        naive_end = event.end.replace(tzinfo=None)

        cursor.execute(variables.sql_safe_select, (event.summary, naive_start, naive_end))
        cur_event = cursor.fetchone()

        if (event.summary, naive_start.strftime('%Y-%m-%d %H:%M'), naive_end.strftime('%Y-%m-%d %H:%M')) != cur_event:
            cursor.execute(
                variables.sql_safe_insertion,
                (event.start, event.end, event.summary)
            )
    cnx.commit()
    cnx.close()

def fecth_events():
    cnx = mysql.connector.connect(**variables.config_connect)
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM schedules")
    x = cursor.fetchall()
    cnx.close()
    return x



print(fecth_events())





