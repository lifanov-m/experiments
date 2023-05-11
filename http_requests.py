#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:59:18 2023

@author: user
"""

import requests
from requests.exceptions import HTTPError


#response = requests.get('https://api.github.com')

for url in ['https://api.github.com' ,'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        response.raise_for_status()
        print(response.status_code)
        
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}') 
    else:
        print('Success')
        

