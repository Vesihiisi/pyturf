#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import requests, json
from datetime import datetime
from dateutil.parser import parse
from dateutil import tz

def utc_to_local(string):
    mydate = parse(string)
    HERE = tz.tzlocal()
    UTC = tz.gettz('UTC')
    result = mydate.replace(tzinfo=UTC)
    return result.astimezone(HERE)

def time_object_print(datetime):
    return datetime.strftime("%Y-%m-%d %H:%M:%S")

def request_blocktime(name):
    the_url="http://api.turfgame.com/v4/users"
    data  = json.dumps([{"name" : name}])
    r = requests.post(the_url, data)
    return int(r.json()[0]["blocktime"])

def request_zone(name):
    the_url="http://api.turfgame.com/v4/zones"
    data = json.dumps([{"name" : name}])
    r = requests.post(the_url, data)
    print("zone: ", r.json()[0]["name"])
    print("current owner: " + r.json()[0]["currentOwner"]["name"])
    timestamp = utc_to_local(r.json()[0]["dateLastTaken"])
    print("taken: " + time_object_print(timestamp))   

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('zonename')
    args = parser.parse_args()
    if args.zonename:
        request_zone(args.zonename)

if __name__ == '__main__':
    main()
