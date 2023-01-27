#!/usr/bin/env python3

import os
import json

env = os.environ
#print(env["SHELL"])
#print(json.dumps(dict(env)))

print("Content-Type: application/json") #text/html
print()
#print(env)
print(json.dumps(dict(env), indent= 2))
#print(f"<p> USER_DATA = {os.environ['HTTP_USER_AGENT']} </p>")