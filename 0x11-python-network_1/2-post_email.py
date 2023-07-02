#!/usr/bin/python3
"""
 Python script that takes in a URL and an email, sends a POST request to
 the passed URL with the email as a parameter, and displays the
 body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    mail = {"email": sys.argv[2]}
    url = sys.argv[1]
    data = urllib.parse.urlencode(mail).encode("utf-8")

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as respon:
        content = respon.read()

    print(content.decode("utf-8"))
