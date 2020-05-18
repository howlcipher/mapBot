import numpy as np
import psycopg2

# database
conn = psycopg2.connect(
    database="mapBot",
    user="postgres",
    password="54321",
    host="localhost",
    port=5432
)

# connecting to SQL
print("connected to postgres SQL MAPS DB")
# select all maps
allMaps = conn.cursor()
data = allMaps.execute("SELECT map_name, download_link, map_count FROM maps ORDER BY map_id")
maps = allMaps.fetchall()

# select all maps with map_count = 3
maps3 = conn.cursor()
data3 = maps3.execute("SELECT map_name, download_link, map_count FROM maps WHERE map_count = 3 ORDER BY map_id")
mapsThree = maps3.fetchall()

# select all maps with map_count = 4
maps4 = conn.cursor()
data4 = maps4.execute("SELECT map_name, download_link, map_count FROM maps WHERE map_count = 4 ORDER BY map_id")
mapsFour = maps4.fetchall()

# select all maps with map_count = 5
maps5 = conn.cursor()
data5 = maps5.execute("SELECT map_name, download_link, map_count FROM maps WHERE map_count = 5 ORDER BY map_id")
mapsFive = maps5.fetchall()

# turn query into array
vsmapsdb3 = np.array(mapsThree)
vsmapsdb4 = np.array(mapsFour)
vsmapsdb5 = np.array(mapsFive)
vsmapsdb = np.array(maps)