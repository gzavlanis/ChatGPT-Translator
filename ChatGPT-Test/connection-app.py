import psycopg2
from config import config

def connect(): 
    """ Connect to a postgres database """
    connection = None

    try: 
        params = config()
        print("Connecting to the PostgreSQL database...")
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        print("PostgreSQL database version: ")
        cursor.execute('SELECT version()')
        print(cursor.fetchone())
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if connection is not None:
            connection.close()
            print("Database connection closed.")

if __name__ == "__main__":
    connect()
