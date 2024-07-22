import psycopg2



# conn = psycopg2.connect(
#     user='postgres',
#     dbname='kinobot',
#     password='nuriddin2323',
#     port=5432,
#     cursor_factory=DictCursor
#
# )
#
# cur = conn.cursor()

import psycopg2
from psycopg2.extras import DictCursor
# try:
#     conn = psycopg2.connect(
#
#     user='postgres',
#     dbname='kinobot',
#     password='nuriddin2323',
#     port=5432,
#     cursor_factory=DictCursor
#
#
#
#     )
#     print("Connected to PostgreSQL!")
#     # Further operations like executing queries or fetching data can go here
# except psycopg2.OperationalError as e:
#     print(f"Unable to connect to PostgreSQL: {e}")
import psycopg2
from psycopg2.extras import DictCursor
# Establish a connection to your PostgreSQL database
conn = psycopg2.connect(
        user='postgres',
        dbname='kinobot',
        password='nuriddin2323',
        port=5432,
        cursor_factory=DictCursor
)

# Create a cursor object to execute SQL queries
cur = conn.cursor()

def startup_table():
    query = '''
    CREATE TABLE IF NOT EXISTS users(
        id BIGSERIAL PRIMARY KEY,
        telegram_id VARCHAR(60) UNIQUE,
        created_at TIMESTAMP DEFAULT now()
    )
    '''
    channel_query = '''
    CREATE TABLE IF NOT EXISTS channels(
        id BIGSERIAL PRIMARY KEY,
        username VARCHAR(128) NOT NULL,
        channel_id VARCHAR(128) UNIQUE,
        created_at TIMESTAMP DEFAULT now()
    )
    '''
    media_query = '''
    CREATE TABLE IF NOT EXISTS movies(
        id BIGSERIAL PRIMARY KEY,
        post_id INT NOT NULL,
        file_id VARCHAR(800) NOT NULL,
        caption TEXT,
        created_at TIMESTAMP DEFAULT now()
    )
    '''
    cur.execute(query)
    cur.execute(channel_query)
    cur.execute(media_query)
    conn.commit()

# Call the function to create the tables
startup_table()

# Close cursor and connection when done
cur.close()
conn.close()

