#!/usr/bin/python3
"""
 Python script that takes in a URL and an email, sends a POST request to
 the passed URL with the email as a parameter, and displays the
 body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    import sys

    url = sys.argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as respon:
            content = respon.read()
        print(content.decode("utf-8"))

    except HTTPError as e:
        print("Error: ", e.code)
