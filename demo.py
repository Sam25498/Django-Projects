# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:10:09 2022

@author: Sam
"""

import requests
from rich import console
from ms_graph import generate_access_token, GRAPH_API_ENDPOINT
import json

console = console.Console() 
APP_ID = 'afa25714-fab7-480a-bc86-734818136ebb'
SCOPES = ['Calendars.ReadWrite']

#Step 1. Generate Access Token
access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

# Step 2. Create an event
def construct_event_detail(event_name, **event_details):
    request_body = {
        'subject': event_name
        }
    for key, val in event_details.items():
        request_body[key] = val
    return request_body

response1_create = requests.post(
    GRAPH_API_ENDPOINT + f'/me/events',
    headers=headers,
    json=construct_event_detail('Movie Night')
)
console.print(response1_create.json())    
    
    


#/me/event    
