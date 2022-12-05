import csv
import datetime
import imp
import json
import logging
import sys
import time
import os
from encodings import utf_8_sig  # 액셀파일에서 한글깨질때

import azure.functions as func
import requests
import pandas as pd
from bs4 import BeautifulSoup
from azure.data.tables import TableServiceClient
from azure.core.exceptions import HttpResponseError

sys.path.append("./")
from . import coin_crawl

# import weather_az1

# def main(mytimer: func.TimerRequest) -> None:
"""
def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = (
        datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    )
"""
def main(mytimer: func.TimerRequest, tablePath:func.Out[str]) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()


    if mytimer.past_due:
        logging.info("The timer is past due!")

    logging.info("Python timer trigger function ran at %s", utc_timestamp)
    

    print("bitcoin web crawl")
    tags = coin_crawl.bit_crawl()
    logging.info("tags data %s",tags)

    new_data = {
        "crawl_date": tags[0],
        "name": tags[1],
        "marketCap": tags[2],
        "price": tags[3],
        "PartitionKey": "temp",
        "RowKey": time.time() #utc_timestamp
    }
    print("new_data=",new_data)

    tablePath.set(json.dumps(new_data))

