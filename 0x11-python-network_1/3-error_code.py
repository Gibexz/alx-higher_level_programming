#!/usr/bin/python3
"""
 Python script that takes in a URL, sends a request to the URL and
 displays the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import sys
    import urllib.error

    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as respon:
            content = respon.read()
            print(content.decode("utf-8"))

    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
