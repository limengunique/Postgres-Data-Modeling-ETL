# DROP TABLES

songplay_table_drop = "Drop table IF EXISTS songplays"
user_table_drop = "Drop table IF EXISTS users"
song_table_drop = "Drop table IF EXISTS songs"
artist_table_drop = "Drop table IF EXISTS artists"
time_table_drop = "Drop table IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id serial Primary Key NOT NULL, 
                                                                  start_time bigint NOT NULL, 
                                                                  user_id int NOT NULL, 
                                                                  level varchar, 
                                                                  song_id varchar, 
                                                                  artist_id varchar, 
                                                                  session_id int, 
                                                                  location varchar, 
                                                                  user_agent varchar);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int Primary Key NOT NULL, 
                                                          first_name varchar,
                                                          last_name varchar, 
                                                          gender varchar, 
                                                          level varchar);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar Primary Key NOT NULL, 
                                                          title varchar, 
                                                          artist_id varchar, 
                                                          year int, 
                                                          duration numeric);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar Primary Key NOT NULL, 
                                                              name varchar, 
                                                              location varchar, 
                                                              latitude numeric, 
                                                              longitude numeric);
""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time timestamp Primary Key NOT NULL, 
                                                         hour int NOT NULL, 
                                                         day int NOT NULL, 
                                                         week int NOT NULL, 
                                                         month int NOT NULL, 
                                                         year int NOT NULL, 
                                                         weekday int NOT NULL);
""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) \
                 VALUES (%s, %s, %s, %s, %s)\
                 ON CONFLICT (user_id) DO UPDATE SET level=excluded.level;
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) \
                 VALUES (%s, %s, %s, %s, %s)\
                 on conflict (song_id) do nothing
""")


artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) \
                 VALUES (%s, %s, %s, %s, %s)\
                 on conflict (artist_id) do nothing
""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
                 VALUES (%s, %s, %s, %s, %s, %s, %s)\
                 on conflict (start_time) do nothing;
""")

# FIND SONGS

song_select = ("""select s.song_id, a.artist_id 
                  from songs s join artists a on s.artist_id=a.artist_id
                  where s.title=%s and a.name=%s and s.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
