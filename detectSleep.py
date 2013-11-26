#!/usr/bin/env python

import requests, json
import pandas as pd

url = "http://restwell.herokuapp.com/sleep/sleepRecord.json"
resp = requests.get(url=url)
data = json.load(resp.content)
