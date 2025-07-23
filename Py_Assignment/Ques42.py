# Write a program to parse and display JSON data from a string.

import json
info = '{"name": "Suhani", "age": 19}'
parsed = json.loads(info)
print(parsed["name"], parsed["age"])