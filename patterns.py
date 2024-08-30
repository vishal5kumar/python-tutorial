
# # 1
# n = 5
# for i in range(n):
#     print("*")
 
    
# # #2
# n = 5
# for j in range(n):
#     print("*",end = " ")
    
    
# #3
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end=" ")
        
#     print()
    
    
#4
# n = 8
# for i in range(n):
#     for j in range(i+1):
#         print("*",end = " ")
        
#     print()
    
    
#5
# n = 4
# for i in range(n):
#     for j in range(i,n):
#         print("*",end = " ")
        
#     print()
    
    
#6
n = int(input("enter the number: "))
for i in range(n):
    for j in range(i,n):
        print(" ", end = " ")
    for j in range(i+1):
        print("*", end =" ")
        
    print()
    
    
#7
# n = int(input("enter the number: "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end = " ")
#     for j in range(i):
#         print("*",end = " ")
#     for j in range(i+1):
#         print("*",end = " ")
        
#     print()
    
#8
# n = int(input("enter the number: "))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end = " ")
#     for j in range(i,n-1):
#         print("*",end = " ")
#     for j in range(i,n):
#         print("*",end = " ")
        
#     print()
