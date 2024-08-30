#defining a function
# def greet():
#     print("hello")
#     print("welcome")
    
# greet()


#defining a simple function with argument
# def greet(name):
#      print("hello",name)
#      print("welcome")
    
# greet("vishal")


#function adding two numbers
# def add_numbers(n1,n2):
#     result=n1+n2
#     print("the sum is ",result)
# number1=5.4
# number2=6.7

# add_numbers(number1,number2)


#function with return 
# def greet(name):
#     print("hello",name)
#     return
#     print("welcome")
# greet("vishal")


#function with return
# def add_numbers(n1,n2):
#     result=n1+n2
#     return
# number1=5.4
# number2=6.7
# result= add_numbers(number1,number2)
# print


#function to find the average marks
# def find_average_marks(marks):
#     sum_of_marks = sum(marks)
#     total_subjects = len(marks)
#     average_marks = sum_of_marks/total_subjects
#     return average_marks

# marks = [55,64,75,80,65]
# average_marks = find_average_marks(marks)
# print("your average marks is: ",average_marks)


# also finding grade in above function
# def find_average_marks(marks):
#      sum_of_marks = sum(marks)
#      total_subjects = len(marks)
#      average_marks = sum_of_marks/total_subjects
#      return average_marks
     
#calculate the grade & return it
# def compute_grade(average_marks):
#     if average_marks >=80:
#         grade = 'A'
#     elif average_marks >=60:
#         grade = 'B'
#     elif average_marks >=50:
#         grade = 'c'
#     else:
#         grade = 'f'
#     return grade
    
    
# marks = [55,64,75,80,65]
# average_marks = find_average_marks(marks)
# print("your average marks is: ",average_marks)

# grade = compute_grade(average_marks)
# print("your grade is:",grade)



# Arguments in function
#positional argument
# def add_numbers(n1,n2):
#      sum = n1 + n2
#      return sum

# result = add_numbers(5.4,6.7)
# print(result)

# with default values
# def add_numbers(n1=100,n2=1000):
#      sum = n1 + n2
#      return sum

# result = add_numbers(5.4)
# print(result)

# with keyword arguments
# def person(name,age):
#     print(name)
#     print(age)
    
# person(age=15,name='vishal')

# #variable length arguments
# def sum(a, *b):
#     c = a
#     for i in b:
#         c = c + i
#     print(c)
# sum(5,6,10,15)

#QUESTIONS
#q1 write a functio to calculate & return square of a number
# def square(number):
#     return number ** 2
    
# print(square(4))

#q2  write a function multipy that multiplies two numbers,but can also accepts and multipy strings
# def multiply(p1,p2):
#     return p1 * p2
    
# print(multiply(8,5))
# print(multiply('a',5))
# print(multiply(5,'a'))

## q3 create a function that returns both the area and circumference of the circle given its radius
# import math
# def circle(radius):
#     area = math.pi * radius ** 2
#     circumference = 2 * math.pi * radius
#     return area,circumference
    
# a,c = circle(3)
# print('Area:',a,'circumference:',c)

##q4 write a function that takes variable numbers of arguments and return there sum.
# def sum_all(*args):
#     return sum(args)
# print(sum_all(1,2))
# print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))


# #q5
# def mystery_func(x, y):
#     result = 0
#     for i in range(x):
#         for j in range(y):
#             if i == j:
#                 result += i
#             else:
#                 result += j
#     return result

# print(mystery_func(3, 4))




