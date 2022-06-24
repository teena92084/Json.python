# Python object key unique key value ko access karne ka program likho?
# Code Example

# '{
#  "a":  1,
#  "a":  2,
#  "a":  3, 
#  "a": 4,   
#  "b": 1, 
#  "b": 2
# }'
# Output:-
# Code Example

# Original Python object:- 

# {
#     "a":  1, 
#     "a":  2, 
#     "a":  3, 
#     "a": 4, 
#     "b": 1, 
#     "b": 2
# }


# Unique Key in a JSON object:-

# import json

# python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2,"c":5,"b":8}'
# print("Original Python object:")
# print(python_obj)
# json_obj = json.loads(python_obj)
# print("\nUnique Key in a JSON object:")
# print(json_obj) 



# o/p
# {'a': 4, 'b': 2}