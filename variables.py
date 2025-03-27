config_connect = {
    "host" : "127.0.0.1",
    "port" : 3306,
    "user" : "root",
    "password" : "Siebel007**",
    "database" : "lectures"}

sql_safe_insertion = "INSERT INTO schedules (start_time, end_time, name_lecture) VALUES (%s, %s, %s)"
sql_safe_select = "SELECT name_lecture, DATE_FORMAT(start_time, '%Y-%m-%d %H:%i'), DATE_FORMAT(end_time, '%Y-%m-%d %H:%i') FROM schedules WHERE name_lecture = %s AND start_time = %s AND end_time = %s"