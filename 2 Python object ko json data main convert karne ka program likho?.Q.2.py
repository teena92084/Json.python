# 2 Python object ko json data main convert karne ka program likho?
import json

a={
    "name": "David", 
    "class": "I", 
    "age": 6
}
n=json.dumps(a,indent=6)
print(n)