#!/usr/bin/python3
import urllib.request
rq = urllib.request.Request('http://python.org/')
with urllib.request.urlopen(rq) as res:
    print(res.read())
