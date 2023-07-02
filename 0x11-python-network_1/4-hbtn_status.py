#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    req = requests.get(url)
    resp = req.text

    print("Body response:")
    print(f"\t- type: {type(resp)}")
    print(f"\t- content: {resp}")
