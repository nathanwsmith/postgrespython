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
from pscopg2 import Error


def main ():

    print("Starting Main")
    adsb_postgres.testdbconnection()
    return None

if __name__ == '__main__' : main()