'''
Module Summary:
 -Stores adsb stream data in a postgresql database
Inputs:
 - a
Outputs:
 - b
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
import consume
from consume import tablewrite

def main ():

    print("Starting Main")
    consume.tablewrite()

    return None

if __name__ == '__main__' : main()