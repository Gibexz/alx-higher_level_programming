#!/bin/bash
# Bash Script that makes a request to 0.0.0.0:5000/catch_me and get the response
curl -sX PUT -Ld "user_id=98" -H "Origin:HolbertonSchool" "0.0.0.0:5000/catch_me"
