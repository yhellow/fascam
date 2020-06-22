import requests
url = ''
headers = {}
r = requests.get(url, headers= headers)
rjson = r.json()

from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')

import random
import os 
import sys
from imp import reload

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbName

from flask import Flask, requet, render_template, jsonify
app = Flask(__name__)
if __name__ == '__main__':
    app.run('0.0.0.0', port= 5000, debug= True)


