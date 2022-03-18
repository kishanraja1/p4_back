import psycopg2
from spotify_client import *

sp_api_call = spotify.search('South Pacific','album')
sp_converted_data = spotify.convert_album_data(sp_api_call)
# print(sp_converted_data)

ladygaga_api_call = spotify.search('Lady Gaga','artist')
lg_converted_data = spotify.convert_artist_data(ladygaga_api_call)
print(lg_converted_data)

def insert_album(name, year):
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
    sql = '''INSERT INTO albums_api_album(name, year) VALUES(%s, %s) RETURNING id'''
    cur.execute(sql, (name, year,))

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

def insert_artist(name, genre, image):
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
    sql = '''INSERT INTO artists_api_artist(name, year) VALUES(%s, %s, %s) RETURNING id'''
    cur.execute(sql, (name, genre, image,))

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

# print(insert_album(sp_converted_data['name'], sp_converted_data['year']))





