# # Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

# # Input :-
# # Code Example


# # Text.txt:-  
# #  Name Abhishek
# #  Designation CEO of navgurukul
# #  Gender male
# #  Age 29

# # Output:-
# # Code Example

# # Json_file.json:-


# # {
# #     “Name”: “Abhishek”,
# #     “Designation”: “CEO of      navgurukul”,
# #     “Gender”:”male”,
# #     “Age”: “29”
#     }


a={
    "Name": "Abhishek",
    "Designation": "CEO of      navgurukul",
    "Gender":"male",
    "Age": "29"
    }



# d={}
# name=input("enter the name")
# deci=input("enter the designation")
# gender=input("enter the gender")
# age=int(input("enter the age"))
# d["name"]=name
# d["designation"]=deci
# d["gender"]=gender
# d["age"]=age
# print(d)

import json
with open("teena23.json","w")as f:
    json.dump(a,f,indent=10)
    


