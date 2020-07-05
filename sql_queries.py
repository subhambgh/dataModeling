# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists; "
time_table_drop = "DROP TABLE IF EXISTS time; "

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE songplays(
	songplay_id serial PRIMARY KEY,
	start_time TIMESTAMP,
	user_id int,
	level VARCHAR (50),
	song_id VARCHAR (100),
	artist_id VARCHAR (100),
    session_id int,
    location VARCHAR (350),
    user_agent VARCHAR (350)
);
""")

user_table_create = ("""CREATE TABLE users(
	user_id int,
	first_name VARCHAR (100),
    last_name VARCHAR (100),
    gender VARCHAR (10),
    level VARCHAR (50)
);
""")

song_table_create = ("""CREATE TABLE songs (
	song_id VARCHAR (100),
	title VARCHAR (350),
    artist_id VARCHAR (100),
    year int,
    duration float8
);
""")

artist_table_create = ("""CREATE TABLE artists  (
	artist_id VARCHAR (100),
	name VARCHAR (350),
    location VARCHAR (350),
    latitude float8,
    longitude float8
);
""")

time_table_create = ("""CREATE TABLE time  (
	start_time TIMESTAMP,
	hour int,
    day int,
    week int,
    month int,
    year int,
    weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays(
	start_time,
	user_id,
	level,
	song_id,
	artist_id,
    session_id,
    location,
    user_agent ) 
values (%s,%s,%s,%s,%s,%s,%s,%s);
""")

user_table_insert = ("""INSERT INTO users(
	user_id,
	first_name,
    last_name,
    gender,
    level)
values (%s,%s,%s,%s,%s);
""")

song_table_insert = ("""INSERT INTO songs (song_id,title,artist_id,year,duration) values (%s,%s,%s,%s,%s);""")

artist_table_insert = ("""INSERT INTO artists  (
	artist_id,
	name,
    location ,
    latitude ,
    longitude ) 
values (%s,%s,%s,%s,%s);
""")


time_table_insert = ("""INSERT INTO time  (
	start_time,
	hour,
    day,
    week,
    month,
    year,
    weekday) 
values (%s,%s,%s,%s,%s,%s,%s);
""")

# FIND SONGS

song_select = (""" select song_id,
	artist_id from songs where title = %s and artist_id = (select artist_id from artists where name = %s) and duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]