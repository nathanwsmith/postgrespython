import psycopg2


def testdbconnection():
    '''
    Summary:
            -Tests the connection to the PostgreSQL database and prints connection properties
    '''
    try:

        connection = psycopg2.connect(user = "futurecapability",
                                    password = "BAECommTech1",
                                    host = "10.72.124.159",
                                    port = "5432",
                                    database = "adsb_stream")

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