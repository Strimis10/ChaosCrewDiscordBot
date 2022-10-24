#!/bin/bash 
import flask
from flask import request, jsonify
import json
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True
 


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
 

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Discord Attached Viritual Equipment</h1>
<h3><pre>
  /$$$$$$$                                      /$$                   /$$    
 | $$__  $$                                    | $$                  | $$    
 | $$  \ $$  /$$$$$$  /$$    /$$ /$$$$$$       | $$$$$$$   /$$$$$$  /$$$$$$  
 | $$  | $$ |____  $$l  $$  /$$//$$__  $$      | $$__  $$ /$$__  $$l_  $$_/  
 | $$  | $$  /$$$$$$$ \  $$/$$/| $$$$$$$$      | $$  \ $$| $$  \ $$  | $$    
 | $$  | $$ /$$__  $$  \  $$$/ | $$_____/      | $$  | $$| $$  | $$  | $$ /$$
 | $$$$$$$/|  $$$$$$$   \  $/  |  $$$$$$$      | $$$$$$$/|  $$$$$$/  |  $$$$/
 |_______/  \_______/    \_/    \_______/      |_______/  \______/    \___/  </pre></h3>'''


@app.route('/api/v1/user_data/all', methods=['GET'])
def api_all():
    query_parameters = request.args

    key = query_parameters.get('key')
    user = query_parameters.get('user')
    with open(f"{os.getcwd()}/jsons/api_keys.json") as userData: 
        data = json.load(userData)
    
    

    authorization = False
    for user in data:
        if str(key) == data[user]["key"]:
            clearance = data[user]["clearance"]
            if clearance < 2:
                authorization = True
    
    if authorization:
        with open(f"{os.getcwd()}/jsons/user_info.json") as userData: 
            data = json.load(userData)
        
        return data
    elif not authorization:
        return Unauthorized(401)



@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.errorhandler(401)
def Unauthorized(e):
    return "<h1>401</h1><p>You are Unauthorized to request this data</p>", 401


@app.route('/api/v1/user_data/', methods=['GET'])
def api_filter():
    query_parameters = request.args

    key = query_parameters.get('key')
    user = query_parameters.get('user')
    # author = query_parameters.get('author')



    with open(f"{os.getcwd()}/jsons/api_keys.json") as userData: 
        data = json.load(userData)

    
    if str(key) in data:
        clearance = data[str(key)]["clearance"]
    if user ==  data[str(key)]["user"]:
        clearance = 0


    if clearance >= 4:
        return Unauthorized(401)
    elif clearance == 0:
        with open(f"{os.getcwd()}/jsons/user_info.json") as userData: 
            data = json.load(userData)
        return data[str(user)]
    elif clearance == 1:
        with open(f"{os.getcwd()}/jsons/user_info.json") as userData: 
            data = json.load(userData)
        daata = {data[user]

        }
        return data[str(user)]
    elif clearance == 2:
        with open(f"{os.getcwd()}/jsons/user_info.json") as userData: 
            data = json.load(userData)
        return data[str(user)]
    elif clearance == 3:
        with open(f"{os.getcwd()}/jsons/user_info.json") as userData: 
            data = json.load(userData)
        return data[str(user)]





app.run(ip="0.0.0.0", port=8999)
