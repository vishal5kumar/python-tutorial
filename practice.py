#DICTIONARY
# student= {'amy':11,'buny':12,'zuno':13,'kity':14,'mity':15,101:'dollar'}

# print(student)
# print(["amy"])
# student['buny']='tumy'
# print(student)

# student['dummy']=16
# print(student)

# del student[101]
# print(student)

# print('amy'in student)
# print(101 in student)
# new_student = student.copy()
# print(new_student)

# list1 = ['a','b','c','d']
# list2 = [1,2,3,4]

# new_list = dict(zip(list1,list2))
# print(new_list)

# key = (101,102,103)
# value = ('good','very','fair')
# d = dict.fromkeys(key,value)
# print(d)
# print(student.items())

workers = {'ami':11,'bani':12,'cani':13,'dani':14,'eni':15}
#print(workers)

# all_keys=(workers.keys())
# print(all_keys)
# #print(workers['ami'])
# keys_lst = list(all_keys)
# print(keys_lst)
# print(keys_lst[0])



# for k in keys_lst:
#     print(k)

# all_values=workers.values()
# print(all_values)
# print(type(all_values))

# value_lst=list(all_values)
# print(value_lst)
# print(type(value_lst))
# print(value_lst[0])

# for v in value_lst:
#     print(v)

# workers.update({'femi':16})
# # print(workers)
# new_workers= {'gemi':17,'heni':18} 

# # new_workers.pop('gemi')
# # print(new_workers)

# default= new_workers.setdefault('heni')
# print(default)


#accessing dict using loop

# stu = {'bozo':101,'cozo':102,'dozo':103}
# for k in stu:
#     print(k)
#     print(stu[k])

# for k in stu:
#     print(k, '=',stu[k])
    
a = {}
n = int(input("no of elements: "))
for i in range(n):
    k = input("enter key: ")
    v = input("enter value: ")
    a.update({k:v})
print(a)


#RANGE
# for i in range(5):
#     print(i)
    
# for i in range(5,10):
#     print(i)
    
# for i in range(0,10,3):
#     print(i)
   
marks = [10,20,30,40,50,60]
for i in range(len(marks)):
    print(i,marks[i])


marks = [12,14,15,17,16,18,14]
print(len(marks))

