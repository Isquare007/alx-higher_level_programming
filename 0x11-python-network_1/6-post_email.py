#!/usr/bin/python3
"""
A Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import requests
import sys

if __name__ == '__main__':
    data = {'email': sys.argv[2]}
    url = sys.argv[1]
    r = requests.post(url, data)
    print(r.text)