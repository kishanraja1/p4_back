# used www.postgresqltutorial.com to help with much of this code

import psycopg2
from spotify_client import *

purple_api_call = spotify.search('Purple Rain','album')
purple_converted_data = spotify.convert_album_data(purple_api_call)
# print(sp_converted_data)

# ladygaga_api_call = spotify.search('Lady Gaga','artist')
# lg_converted_data = spotify.convert_artist_data(ladygaga_api_call)
# bruce_api_call = spotify.search('Bruce Springsteen','artist')
# bruce_converted_data = spotify.convert_artist_data(bruce_api_call)
# print(bruce_converted_data)

def insert_album(album_obj):
  conn = None
  album_id = None
  try: 
    # SET UP DB CONNECT WITH psycopg2
    # creates connection to PostgreSQL server
    conn = psycopg2.connect("dbname=music") 
    print (conn)

    # creates a cursor (used to execute SQL statements)
    cur = conn.cursor()

    # execute the INSERT statement
    sql = '''INSERT INTO albums_api_album(name, year, image) VALUES(%s, %s, %s) RETURNING id'''
    cur.execute(sql, (album_obj['name'], album_obj['year'], album_obj['image']))

    # get the generated id back
    album_id = cur.fetchone()[0]

    # commit the changes to the db
    conn.commit()

    # close communication with the db
    cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

  return album_id

def insert_artist(artist_obj):
  conn = None
  artist_id = None
  try: 
    # SET UP DB CONNECT WITH psycopg2
    # creates connection to PostgreSQL server
    conn = psycopg2.connect("dbname=music") 
    print (conn)

    # creates a cursor (used to execute SQL statements)
    cur = conn.cursor()

    # execute the INSERT statement
    sql = '''INSERT INTO artists_api_artist(name, genre, image) VALUES(%s, %s, %s) RETURNING id'''
    cur.execute(sql, (artist_obj['name'], artist_obj['genre'], artist_obj['image'],))

    # get the generated id back
    artist_id = cur.fetchone()[0]

    # commit the changes to the db
    conn.commit()

    # close communication with the db
    cur.close()
  except (Exception, psycopg2.DatabaseError) as error:
    print(error)
  finally:
    if conn is not None:
      conn.close()

  return artist_id

# print(insert_album(sp_converted_data))
# print(insert_artist(bruce_converted_data))
# print(insert_album(haiti_converted_data))
print(insert_album(purple_converted_data))




