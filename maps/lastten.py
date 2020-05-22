from datetime import datetime

import numpy as np
import psycopg2


# creates a string for time entry into the db
def lastPlayDate():
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    dateLP = "Year: " + str(currentYear) + " Month: " + str(currentMonth) + " Day: " + str(currentDay)
    return dateLP


#formating a string for the db entry
lastPlayed = str(lastPlayDate())


# updates the lastten db
def updateDB(m):
    if (m != "No map set"):
        mapSplit = m.split(":", 1)
        map = mapSplit[0]
        sql = "INSERT INTO lastten (map_name, last_played) Values('{}', '{}')".format(str(map), str(lastPlayed))
        conn = None

        try:
            # connect to database
            conn = psycopg2.connect(
                database="mapBot",
                user="postgres",
                password="54321",
                host="localhost",
                port=5432
            )

            cur = conn.cursor()
            # prints the query and didsplays connection
            print("connected to postgres SQL LASTTEN DB")
            print(sql)
            # executes the query
            cur.execute(sql)
            # commits the entry
            conn.commit()
            # closes the cursor
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            #closes the connections
            if conn is not None:
                conn.close()


# gets the last ten maps played
def displayLastTen():
    conn = None
    # database
    #connect to database
    conn = psycopg2.connect(
        database="mapBot",
        user="postgres",
        password="54321",
        host="localhost",
        port=5432
    )

    lt = conn.cursor()
    # executes the query
    lt.execute("SELECT map_name, last_played FROM lastten ORDER BY map_id DESC LIMIT 10")
    print("connected to postgres SQL LASTTEN DB")

    # puts last ten entries into array
    lastTen = np.array(lt.fetchall())
    lt.close()
    if conn is not None:
        conn.close()
    return lastTen
