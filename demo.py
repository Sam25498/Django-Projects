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


#/me/event    
