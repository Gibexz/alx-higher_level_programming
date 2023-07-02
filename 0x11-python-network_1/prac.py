#!/usr/bin/python3
import urllib.request
import shutil
import tempfile
with urllib.request.urlopen('http://python.org/') as response:
    #html = response.read()
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)
with open(tmp_file.name) as html:
    tmp = html.read()
print(tmp)
