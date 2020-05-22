from datetime import datetime

import numpy as np
import psycopg2


def lastPlayDate():
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    dateLP = "Year: " + str(currentYear) + " Month: " + str(currentMonth) + " Day: " + str(currentDay)
    return dateLP


lastPlayed = str(lastPlayDate())


# updates the lastten db
def updateDB(m):
    if (m != "No map set"):
        mapSplit = m.split(":", 1)
        map = mapSplit[0]
        sql = "INSERT INTO lastten (map_name, last_played) Values('{}', '{}')".format(str(map), str(lastPlayed))
        conn = None

        try:
            conn = psycopg2.connect(
                database="mapBot",
                user="postgres",
                password="54321",
                host="localhost",
                port=5432
            )

            cur = conn.cursor()

            print(sql)
            cur.execute(sql)
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


# gets the last ten maps played
def displayLastTen():
    # database
    conn = psycopg2.connect(
        database="mapBot",
        user="postgres",
        password="54321",
        host="localhost",
        port=5432
    )

    # connecting to SQL
    print("connected to postgres SQL LASTTEN DB")
    # select all maps
    lt = conn.cursor()
    lt.execute("SELECT map_name, last_played FROM lastten ORDER BY map_id DESC LIMIT 10")

    lastTen = np.array(lt.fetchall())
    lt.close()
    return lastTen
