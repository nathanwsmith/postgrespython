import json
from kafka import KafkaConsumer
import psycopg2


def format_dict():
    '''
    Summary:
            - Take the message and format into a dict of structure {'flight_id' : {'lat' : lat, 'long' : long}, ... }
    '''

    return None

def print_nicely(my_dict):
    '''
    Summary:
            - Print things out nicely
    '''

    for entry in my_dict:
        # NB: Sometimes data contains None for lat/long, make sure to check
        if (my_dict[entry]['lat'] is not None) and (my_dict[entry]['lon'] is not None):
            print("New Entry: %s | Latitude %.3f | Longitude %.3f" % (entry, my_dict[entry]['lat'], my_dict[entry]['lon']))

    return None


def tablewrite():

    consumer = KafkaConsumer('adsb-data', bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], auto_offset_reset='earliest')

    for message in consumer:

        # Decode the received message
        ascii_msg = message.value.decode('ascii')
        # Do some formatting
        ascii_msg = ascii_msg.replace("'", "\"")
        # Turn into a dict
        output_dict = json.loads(ascii_msg)

        '''
        ############## CUSTOM CODE GOES HERE ###################
        '''
      
# first_time = False

#     # conn.autocommit = True

#     if first_time:
#         try:
#             conn = psycopg2.connect(database="hackathon", user='postgres', password='MainDevAdmin1', host='127.0.0.1', port='5432')
#         except:
#             print("Could not connect")

#         curr = conn.cursor()

#         print('PostgreSQL database version:')
#         curr.execute('SELECT version()')

#         # Drop table if it exists:
#         curr.execute("DROP TABLE IF EXISTS adsb")

#         sql = '''CREATE TABLE adsb(
#             icao_id CHAR(255) NOT NULL,
#             lat FLOAT,
#             lon FLOAT
#         )'''

#         curr.execute(sql)
#         print("Created new table")
#         conn.close()
    
    
    # Begin ADSB loop
  

        try:
            conn = psycopg2.connect(host = "172.21.190.154", port = "5432", database="adsb_data", user='futurecapability', password='BAECommTech1')
            curr = conn.cursor()
        except:
            print("Could not connect")

       
        # Loop over each individual entry, i.e icao24 ID
        for entry in output_dict:
            print("Made it to the FOR LOOP!")
            my_id = entry
            my_lat = output_dict[entry]['lat']
            my_lon = output_dict[entry]['lon']

            # And write to postgres
            query = '''INSERT INTO adsb(icao_id, lat, lon) VALUES('%s', '%s', '%s')''' % (my_id, str(my_lat), str(my_lon))
            curr.execute(query)
            conn.commit()
            print("Records inserted ...")

        print("Awaiting new data ...")
        # result = curr.fetchone()
        # print(result)
        # time.sleep(5)
        curr.close()
        conn.close()
        print("Connection closed")


        '''
        ########################################################
        '''


    return None

if __name__ == "__main__" : main()
