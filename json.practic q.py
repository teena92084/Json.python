# import json
# from textwrap import indent
# j='{"name":"tina","city":"jaipur}'
# p=json.load(j,indent=3)
# print(p)


# import json
# a=["neelam","programer","24","2400",]
# ["komal","trainer","24","20000"]
# ["anuradha","HR","25","40000"]
# ["Abhishek","manager","29","63000"]


# c={}
# key=input("enter the key")
# i=0
# for key in a:
#     if key not in a:

#         # c.update({[key]:i[0]})
#         a[key]=a[0]
#         i=i+1
# print(c)    









# out={"name":"tina","city":"jaipur"} 

# import json
# p=open("data.text","w")
# json.load(p)

  
# # the file to be converted to 
# # json format
# fil = 'data.txt'
  
# # dictionary where the lines from
# # text will be stored
# dict1 = {}
  
# # creating dictionary
# with open(fil) as out:
  
    # for line in out:
   
#         # reads each line and trims of extra the spaces 
#         # and gives only the valid words
#         command, description = line.strip().split(None, 1)
  
#         dict1[command] = description.strip()
  
# # creating json file
# # the JSON file is named as test1
# out_file = open("test1.json", "w")
# json.dump(dict1, out_file, indent = 4, sort_keys = False)
# out_file.close()



# import json
# j={"name":"teena","surname":"kanawar","father":"sulthan"}
# s=json.dump(j)
# pr



# text file data ko json file data mai convert karo,jaise ki neeche diya hai?



# p=open("my data.text","w")
# p.write( "Name Abhishek Designation CEO of navgurukul Gender male Age 29")


# Output:-
# Code Example

# Json_file.json:-


# a={
#     "Name": "Abhishek",
#     "Designation": "CEO of      navgurukul",
#     "Gender":"male",
#     "Age": "29"
#     }



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

# import json
# with open("teena1.json","w")as f:
#     json.dump(a,f,indent=10)
    





# import json
# python_obj = '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2,"c":5,"b":8}'
# print("Original Python object:")
# print(python_obj)
# json_obj = json.loads(python_obj)
# print("\nUnique Key in a JSON object:")
# print(json_obj) 



# # o/p
# # {'a': 4, 'b': 2}



# import json
# from textwrap import indent
# a='{"name":"teena","b":"meena","c":"reena"}'
# v=json.loads(a)
# print(v)


# import json
# j={'name':"teena","class":12,"age":20}
# p=json.dumps(j,indent=5)
# print(p)


# import json
# s={'name':"teena","class":12,"age":20}
# h=open("my hobby.json","w")
# json.dump(s,h)



# import json
# a={"teena":"teena","age":20,"city":"bhilwara"}
# file=open("my datels.json","r")
# r=json.load(file)
# print(r)



# import json
# age=20
# selery=3400.50
# name="teena"
# print(json.dumps(name))
# print(json.dumps(selery))


# import json
# a='{"name":"teena","surname":"kanawar","age":20,"hobb":"dance"}'
# k=json.loads(a)
# print(k)


# import json
# d={"name":"teena","surname":"kanawar","age":20,"hobb":"dance"}
# k=json.dumps(d,indent=4)
# print(k)


# import json
# d={"name":"teena","surname":"kanawar","age":20,"hobb":"dance"}
# j=open("my wis.json","w")
# l=json.dump(d,j,indent=4)


# import json
# d={"name":"teena","surname":"kanawar","age":20,"hobb":"dance"}
# j=open("my wis.json","r")
# m=json.load(j)
# print(m)



# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?




# a={"teena":"kanawar","nettu":"sharam","piya":"kanawar","pooja":"kanawar","meena":"sharma"}
# b=[]
# for key,value in a.values():
#     # for i in a.values():
#     s="kanawar"
#     if s== (key,value):
#         b.append(s)
#     print(b)        

# import json  
# j='{"name":"teena","class":12,"age":20}'
# p=json.loads(j)
# print(p)


# import json
# p={"name":"teena","class":12,"age":20}
# g= json.dumps(p,indent=4)
# print(g)


# import json
# p=open("instaghrame id.json","w")
# v={"teena":"kanawar","nettu":"sharam","piya":"kanawar","pooja":"kanawar",
# "meena":"sharma"}
# j=json.dump(v,p,indent=8)
# print(j)



# import json
# v={"teena":"kanawar","nettu":"sharam","piya":"kanawar","pooja":"kanawar",
# "meena":"sharma"}
# k=open("teena.json","r")
# l=json.load(k)
# print(l)




# import json
# a={"teena":"teena","age":20,"city":"bhilwara"}
# file=open("my datels.json","r")
# r=json.load(file)
# print(r)




# import json
# a={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# j=json.dumps(a,sort_keys=True,indent=3)
# print(j)