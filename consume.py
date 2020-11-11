import json
from kafka import KafkaConsumer


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


def main():

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
        # Call nice printout function
        print_nicely(output_dict)
        '''
        ########################################################
        '''


    return None

if __name__ == "__main__" : main()
