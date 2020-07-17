# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists; "
time_table_drop = "DROP TABLE IF EXISTS time; "

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays(
	songplay_id SERIAL CONSTRAINT songplay_pk PRIMARY KEY,
	start_time 	TIMESTAMP 	NOT NULL ,
	user_id 	INT 		NOT NULL,
	level 		VARCHAR,
	song_id 	VARCHAR		NOT NULL,
	artist_id 	VARCHAR		NOT NULL,
	session_id 	INT, 
	location 	VARCHAR,
	user_agent 	TEXT
)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS  users(
	user_id  	INT CONSTRAINT users_pk PRIMARY KEY,
	first_name  	VARCHAR		NOT NULL,
	last_name  	VARCHAR		NOT NULL,
	gender  	CHAR(1)		NOT NULL,
	level 		VARCHAR 	NOT NULL
)""")

song_table_create = ("""CREATE TABLE  IF NOT EXISTS songs(
	song_id 	VARCHAR CONSTRAINT songs_pk PRIMARY KEY,
	title  		VARCHAR		NOT NULL,
	artist_id  	VARCHAR 	NOT NULL,
	year 		INT 	CHECK (year >= 0),
	duration 	FLOAT
)""")

artist_table_create = ("""CREATE TABLE  IF NOT EXISTS artists(
	artist_id 	VARCHAR CONSTRAINT artist_pk PRIMARY KEY,
	name 		VARCHAR		NOT NULL,
	location 	VARCHAR,
	latitude 	DECIMAL(9,6),
	longitude 	DECIMAL(9,6)
)""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS  time(
	start_time  	TIMESTAMP CONSTRAINT time_pk PRIMARY KEY,
	hour 		INT 		NOT NULL CHECK (hour >= 0),
	day 		INT 		NOT NULL CHECK (day >= 0),
	week 		INT 		NOT NULL CHECK (week >= 0),
	month 		INT 		NOT NULL CHECK (month >= 0),
	year 		INT 		NOT NULL CHECK (year >= 0),
	weekday 	VARCHAR 	NOT NULL
)""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s )
""")


# Updating the user level on conflict
user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) 
                        ON CONFLICT (user_id) DO UPDATE SET 
                        level = EXCLUDED.level 
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) 
                        ON CONFLICT (song_id) DO NOTHING                        
""")


# Artist location, latitude and longitude might change .
artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) 
                          ON CONFLICT (artist_id) DO UPDATE SET
                          location = EXCLUDED.location,
                          latitude = EXCLUDED.latitude,
                          longitude = EXCLUDED.longitude
""")

time_table_insert = ("""INSERT INTO time VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = (""" select song_id,
	artist_id from songs where title = %s and artist_id = (select artist_id from artists where name = %s) and duration = %s;
""")

# QUERY LISTS

create_table_queries = [user_table_create, artist_table_create, song_table_create, time_table_create,songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
