#! /usr/bin/python3

import requests
import os
import passwords

user = passwords.user
password = passwords.password

r = requests.get("https://httpbin.org/basic-auth/mahir/test", auth=(user, password))

print(r.status_code)
