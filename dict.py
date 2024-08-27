# keys = ["car","bike","cycle","bus","train"]
# values = [101,102,103,104,105]

# dic = {}
# for i in range(len(keys)):

#     dic[keys[i]]=values[i]
# print(dic)


# keys = {"car","bike","cycle","bus","train"}
# kys = {"boat","aeroplane"}

# keys.update(kys)
# print(keys)


# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"]["physics"])


# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}

# d = dict.fromkeys(employees,defaults)
# print(d)


# sampleDict = { 
#   "name": "Kelly",
#   "age":25, 
#   "salary": 8000, 
#   "city": "New york" }
# keys = ["name", "salary"]

# dict = {}

# for key in keys:
#     if key in sampleDict:
#         dict[key]=sampleDict[key]
# print(dict)


# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
# # Keys to remove
# keys = ["name", "salary"]

# del sample_dict["name"]
# del sample_dict["salary"]
# print(sample_dict)



# sample_dict = {'a': 100, 'b': 200, 'c': 300}

# # Expected output:
# # 200 present in a dict

# if 200 in sample_dict.values():
#     print("200 present")
# else:
#     print("200 not present")


# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)

# data = sample_dict["salary"]
# del sample_dict["salary"]
# sample_dict["income"] = data

# print(sample_dict)
