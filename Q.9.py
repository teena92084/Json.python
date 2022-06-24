# import json
# a={
#     "shoping_list":
#     {
#      "chaco":"15",
#      "biscute":"50" ,
#      "ice_cream":"20",  
#     }
# }

# n=input("entr item ")
# n1=int(input("enter the quantity"))
# for i in a:
#     for j in a[i]:
#         if n in a[i]:
#             if j==n and int(a[i][j])>=n1:
#                 b=int(a[i][j])-n1
#                 a[i][j]=str(b)
#                 break
#         elif j!=n:
#             print("not avelabile ") 
#             break
# n2=open("purchase.json","w")
# json.dump(a,n2,indent=4)        




