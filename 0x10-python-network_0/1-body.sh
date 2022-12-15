#!/bin/bash
# Bash script that takes in a URL, sends a GET request, and displays the body response
curl -sL $1 -X GET
