
# Q5.Json string ko check karo ki bo complex object contain karti hai ya nahi?

# import json

# def is_complex_num(objct):
#     if '__complex__' in objct:
#         return complex(objct['real'], objct['img'])
#     return objct

# complex_object =json.loads('{"__complex__": true, "real": 4, "img": 5}', object_hook = is_complex_num)
# simple_object =json.loads('{"real": 4, "img": 3}', object_hook = is_complex_num)
# print("Complex_object: ",complex_object)
# print("Without complex object: ",simple_object)



# import json

# def is_complex_num(objct):
#     if "complex" in objct:
#         return complex(objct['real'], objct['img'])
#     return objct

# obje =json.loads('{"compl": true, "real": 4, "img": 5}', object_hook = is_complex_num)
# s_obj =json.loads('{"real": 4, "img": 3}', object = is_complex_num)
# print("Complex_object: ",obje)
# print("Without complex object: ",s_obj)


 