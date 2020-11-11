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
from kafka import KafkaConsumer
import adsb_postgres
import consume
import libpq

def main ():

    print("Starting Main")
    adsb_postgres.testdbconnection()
    return None

if __name__ == '__main__' : main()