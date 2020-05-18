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

# testing sql query
print("connected to postgres SQL USER_ACCOUNT DB")
cur = conn.cursor()
data = cur.execute("SELECT username, bot_admin, server_role FROM user_account ORDER BY user_id")
userDB = np.array(cur.fetchall())


#
# userdb = np.array(users)


# host class
class Host:
    def __init__(self, host: str):
        self.host = host
