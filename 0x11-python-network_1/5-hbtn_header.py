#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    req = requests.get(url)
    resp = req.headers

    print(resp["X-Request-Id"])
