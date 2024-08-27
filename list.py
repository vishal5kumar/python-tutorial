# marks = [1,13,34,"hello","car",65]

# print(marks)
# print(marks[2])
# print(marks[-4])

# if "hello" in marks:
#     print("yes")
# else:
#     print("no")
    
# if "lo" in "hello":
#     print("yo")
    
# print(marks[:])

# print(marks[1:4:2])

# #change element in a list
# marks[2]=25
# print(marks)

# List = [10, 20, 14]
# print("\nList of numbers: ")
# print(List)

#list comprehension

#simple comprehension
# lst1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# new_lst1 = []
# for i in lst1:
#     new_lst1.append(i+1)
# print(new_lst1)

# #or with range
# lst3 = []
# for i in range(20):
#     lst3.append(i+1)
# print(lst3)



# #with list comprehension
# lst2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# new_lst2 = [i+1 for i in lst2]
# print(new_lst2)

# #or with range
# lst4 =[i+1 for i in range(20)]
# print(lst4)

# #with conditions
# #simple
# lst5 = []
# for i in range(20):
#     if (i%2==0):
#         lst5.append(i)
# print(lst5)
        
# #with list comp

# lst6 = [i for i in range(20) if i%2==0]
# print(lst6)

# #with nested loop
# lst7 = []
# for i in range(20):
#     if (i%2==0):
#         if(i%3==0):
#          lst7.append(i)
# print(lst7)

# #with list comp nested loop
# lst8 = [i for i in range(20) if i%2==0 if i%3==0]
# print(lst8)

# #with if and else statement
# lst9 = []
# for i in range(10):
#     if (i%2==0):
#         lst9.append(i)
#     else:
#         lst9.append("invalid")
# print(lst9)

# # if else with list comp
# lst10 = [i if i%2==0 else "invalid" for i in range(10)]
# print(lst10)



#Questions
#1
# list1 = [100, 200, 300, 400, 500]
# list1.reverse()
# print(list1)

#2
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list1.extend(list2)
# print(list1)

#or using * opertor
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = ["s", "dw", "k", "kj"]
# all_list = [*list1,*list2,*list3]
# print(all_list)

# or += opertor 
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list1+=list2
# print(list1)

#3
# numbers = [1, 2, 3, 4, 5, 6, 7]
# ans = [x*x for x in numbers]
# print(ans)

#or 
#ans = []
# for i in numbers:
#     ans.append(i*i)
# print(ans)


#4 ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# ans = [x+y for x in list1 for y in list2]
# print(ans)


#6 remove empty string from list below 
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# list1 = [i for i in list1 if i != ""]
# print(list1)


#7
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
# print(list1[2][2][1])


#8
# list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
# # sub list to add
# sub_list = ["h", "i", "j"]
# list1[2][1][2].extend(sub_list)
# print(list1)


#9
# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[3]=200
# print(list1)


#10
# list1 = [5, 20, 15, 20, 25, 50, 20]

# while 20 in list1:
#     list1.remove(20)
# print(list1)

#11
# num1=[1,2,3,4]
# print (min(num1))
# print (max(num1))

#12
# num=[1,2,3,4,5]
# num[1:3]=[11,22]
# print (num)

#13 remove duplicate items from the list 
# list1 = [1,1,2,2,2,3,5,6,4,7,7,9,8,8,8,0,0,0]
# newlist=set(list1)
# print(list(newlist))



#14 printing only odd from the given list 
# newlist = []
# list2 = [1,3,2,5,1,2,3,1,4,2,1]
# for a in list2:
#     if a%2==0:
#         newlist.append(a)
       
# print(newlist)   

# #15 print no with color
# for i in range(1,51):
#     if i%2==0:
#         print(i,'=',"green")
#     elif i%3==0:
#         print(i,'=',"red")
#     elif i%5==0:
#         print(i,'=',"blue")    

# #16
# list1 = [1,3,2,5,1,2,3,1,4,2,1,[],1,4,[],3,5,[]]
# count = 0
# for a in list1:
#     if a%2==0:
#         count = count + 1
# print(count)


#
# a = list1.index([])
# print(a)
# b = list1.index([], a + 1)
# print(b)
# c = list1.index([], b + 1)
# print(c) 

# #short method 
# for i in range(len(list1)):
#     if list1[i] == []:
#         print(i)