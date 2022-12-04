import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="db",
    user="postgres",
    password="322585")
cur = conn.cursor()


SQL_GET_TASK_BY_ARTIST = f"""select m.artist_name, c.music_track
                         FROM music_artist m, composition c, artist_track at2
                         where m.id = at2.id_music_artist
                         and at2.id_composition = c.id
                         and m.artist_name = '{id_artist}'"""

cur.execute(SQL_GET_TASK_BY_ARTIST)
records = cur.fetchall()
for row in records:
    print(row)

SQL_GET_TASK_BY_LOCAION = f"""select c.music_track, a."location", a.media_type
                          FROM composition c, composition_album ca, album a
                          where c.id = ca.id_composition
                          and ca.id_album = a.id
                          and c.music_track  = '{composition}'"""

cur.execute(SQL_GET_TASK_BY_LOCAION)
records = cur.fetchall()
for row in records:
    print(row)


SQL_GET_TASK_BY_TYPE = f"""select c.music_track, a.media_type
                       FROM composition c, composition_album ca, album a
                       where c.id = ca.id_composition
                       and ca.id_album = a.id
                       and c.music_track  = '{composition}'"""

cur.execute(SQL_GET_TASK_BY_TYPE)
records = cur.fetchall()
for row in records:
    print(row)


SQL_GET_TASK_BY_GENRE = f"""select c.music_track, a.genre
                        FROM composition c, composition_album ca, album a
                        where c.id = ca.id_composition
                        and ca.id_album = a.id
                        and a.genre  = '{genre}'"""

cur.execute(SQL_GET_TASK_BY_GENRE)
records = cur.fetchall()
for row in records:
    print(row)



SQL_GET_TASK_BY_MASS = f"""select c.music_track, a.album_title
                        FROM composition c, composition_album ca, album a
                        where c.id = ca.id_composition
                        and ca.id_album = a.id
                        and c.music_track  = '{track}'
                        or a.release_year = '{year}'
                        or a.album_title = '{album}'
                        GROUP by c.music_track, a.album_title
                        order by a.album_title"""

cur.execute(SQL_GET_TASK_BY_MASS)
records = cur.fetchall()
for row in records:
    print(row)



SQL_GET_TASK_BY_YEAR = f"""select m.artist_name, c.music_track, a.release_year 
                           FROM music_artist m, composition c, artist_track at2, album a, composition_album ca 
                           where m.id = at2.id_music_artist 
                           and at2.id_composition = c.id 
                           and c.id = ca.id_composition 
                           and ca.id_album = a.id 
                           and m.artist_name = '{artist_two}' 
                           and a.release_year = '{year_two}'
                           GROUP by c.music_track, m.artist_name, a.release_year """

cur.execute(SQL_GET_TASK_BY_YEAR)
records = cur.fetchall()
for row in records:
    print(row)

#db.conn(close)