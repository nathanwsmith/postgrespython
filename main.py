'''
Module Summary:
 -Stores adsb stream data in a postgresql database
Inputs:
 -
Outputs:
 -
Author:
 - Nathan Smith : nathan.smith11@baesystems.com
Team:
 -
Date:
- 11/11/2020     
 '''

import json
import psycopg2
from kafka import KafkaConsumer
import adsb_postgres
import consume



def main ():

    print("Starting Main")
    consume.main()
    return None

if __name__ == '__main__' : main()