import psycopg2
import time
from opensky_api import OpenSkyApi

def testdbconnection():
    '''
    Summary:
            -Tests the connection to the PostgreSQL database and prints connection properties
    '''
    try:
        print("Starting...")
        connection = psycopg2.connect(user = "futurecapability", password = "BAECommTech1", host = "172.21.190.154", port = "5432", database = "adsb_data")

        cursor = connection.cursor()
        # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(), "\n")

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    
    return None                            