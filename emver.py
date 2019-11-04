#!/bin/python3
#by Qzacy

import requests
import json
import sys

if len(sys.argv) != 2:
    print("Usage:\npython3 emver.py [test@mail.com]")
    sys.exit()
mail = sys.argv[1]
api_key = "at_ILs0jQmYIThKqwypzUkOXdYgZeoj1"
data = requests.get("https://emailverification.whoisxmlapi.com/api/v1?apiKey=" + api_key + "&emailAddress=" + mail)
resp = data.json()

try:
    print("Results:\n")
    print("E-Mail: " + resp["emailAddress"])
    print("Format: " + resp["formatCheck"])
    print("SMTP: " + resp["smtpCheck"])
    print("DNS: " + resp["dnsCheck"])
    print("Free: " + resp["freeCheck"])
    print("Disposable: " + resp["disposableCheck"])
    print("MX Records:\n" + "\n".join(resp["mxRecords"]))
    
    print("\nCatch all: " + resp["catchAllCheck"])
except EOFError:
    print("An error occured: " + resp["ErrorMessage"])