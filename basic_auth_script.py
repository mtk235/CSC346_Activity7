#! /usr/bin/python3

import requests
import passwords

user = passwords.user
password = passwords.password

r = requests.get("https://api.github.com/user/repos", auth=(user, password))

print(r.status_code)
