# a = 10
# b = 1.2
# c = "Shweta"
# d = {1,4,6,8}
# e = [12,32,43,54]
# f = True
# g = 3 + 5j
# h = None
# i = {"Name":"Riya","Age":22,"City":"Bhusawal"} 
# j = (43,65,87,2)

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))
# print(type(h))
# print(type(i))
# print(type(j))



# a = 345
# print(type(a))
# a = 5.87
# print(type(a))

# employee_id = 1
# name = "Shreya"
# salary = 35000
# department = "IT"
# employment_status = True

# print("Employee ID:", employee_id)
# print("Name:", name)
# print("Salary:", salary)
# print("Department:", department)
# print("Employment Status:", employment_status)


# a = 25
# b = 56
# print(a,b)
# a = a - b
# b = a + b 
# print ("a:",a,"b:",b)



# length = 30
# width = 20
# area = length * width
# print("Area of rectangle:", area)
# print(type(length))
# print(type(width))
# print(type(area))


# a = 10
# b = 20.5
# c = "30"
# print(type(a + b))
# print(type(str(a)))
# print(type(float(c)))      


# a = "250"
# b = int(a)
# print(b * b)


# a = 45
# print(float(a))
# print(str(a))
# print(bool(a))


# a = 99.99
# b = int(a)
# print(b)
# # Output is 99 bcoz int() fuction removes the decimal part of a number



# a = "87"
# b = (int(a))
# print(b)




# marks = "88.97"
# marks = float(marks)
# percentage = (marks / 100) * 100
# print("percentage :",percentage)




# a = 100
# b = 20.5
# print(str(a) + str(b))
# print(int(b))
# print(float(a))
# print(bool(0))
# print(bool(""))




# name = "sita patil"
# print( name.upper())
# print( name.lower())



# text = ("Vurjita patil")
# print("Number of characters:", len(text))



# text = "Java"
# rev = ""
# for ch in text:
#     rev = ch + rev
# print(rev)



# a = "banana"
# count = 0
# for i in a:
#     if i == "a":
#         count = count +1
# print(count)




# a = "vurjita suresh patil"
# b = a.replace(" ","-")
# print(b)



# a = "python"
# if "python" in a:
#     print("word exist")
# else:
#     print("not exist")




# email = "patil123@gmail.com"
# a = email.split("@")
# print("Username :", a[0])
# print("Domain :", a[1])



# name = "vurjita"
# age = 22
# city = "Bhusawal"
# print("My name is",name , "I am ",age , "years old", "I am from ",city)



# numbers = [10, 20, 55, 60, 75, 98, 90, 45, 80, 15, 65, 25, 100, 40, 70]
# for num in numbers:
#     if num > 50:
#         print(num)



# a = [ 20, 40, 50, 70, 64, 96]
# a.sort()
# print(a[-2])



# num = [10, 20, 10, 30, 20, 40, 50]
# result = list(set(num))
# print(result)  #A set stores only unique elements, removes duplicate



# list1 = [10, 20, 30, 40]
# list2 = [40, 50, 60, 70]
# list3 = list1 + list2
# print(list3)



# a = [10, 20, 30, 40]
# b = [30, 40, 50, 60]
# for i in a:
#     if i in b:
#         print(i)




# marks = [35, 60, 80, 25, 45, 90]
# count = 0
# for i in marks:
#     if i >= 40:
#         count = count + 1
# print("Passed students =", count)




# a = [10, -5, 0, 20, -10, 0, 5]
# positive = []
# negative = []
# zero = []
# for i in a:
#     if i > 0:
#         positive.append(i)
#     elif i < 0:
#         negative.append(i)
#     else:
#         zero.append(i)
# print("Positive =", positive)
# print("Negative =", negative)
# print("Zero =", zero)





# a = [10, 15, 20, 25, 30]
# total = 0
# for i in a:
#     if i % 2 == 0:
#         total = total + i
# print(total)





# a = [
#     ["Rahul", 80],
#     ["Priya", 90],
#     ["Amit", 70]
# ]
# print(a[0][0])
# print(a[0][1])

# print(a[1][0])
# print(a[1][1])

# print(a[2][0])
# print(a[2][1])




# a = [10, 20, 30, 40, 50, 60]
# rev = []
# for i in a :
#     rev.insert(0, i)
# print(rev)




# a = (10,30,40,58,79,59,60,100,164,76,12,32,25,74,97,)
# for i in a :
#     if i>50:
#         print(i)


# a = (10,60,38,29,69,45)
# b = sorted(a)
# print(b[-2])



# a = (10,20,10,30,20,40)
# b = tuple(set(a))
# print(b)



# a = (10,20,30)
# b = (40,50,60)
# c = a + b
# print(c)



# a = (10,20,30,40)
# b = (30,40,50,60)
# for i in a:
#     if i in b :
#         print(i)



# marks = (75,76,34,54,85,96,45,30,90)
# count = 0
# for i in marks :
#     if i >= 40:
#         count = count + 1
# print(count)



# a = (10,-5,0,40,60,-35,0,68,-90)
# positive = []
# negative = []
# zero = []
# for i in a:
#     if i > 0 :
#         positive.append(i)
#     elif i < 0:
#         negative.append(i)
#     else :
#         zero.append(i)
# print(tuple(positive))
# print(tuple(negative))
# print(tuple(zero))



# a = (10,15,20,25,30,64)
# total = 0
# for i in a:
#     if i %2 == 0 :
#         total= total+ i
# print(total)



# a = (
#     ("Rahul", 80),
#     ("Priya", 90),
#     ("Amit", 70)
#  )
# print(a[0][0])
# print(a[0][1])
# print(a[1][0])
# print(a[1][1])
# print(a[2][0])
# print(a[2][1])



# a = ( 10,20,30,40,50)
# rev = ()
# for i in a:
#     rev = (i,) + rev
# print(rev)


# a = { 103,106,109,112}
# b = { 102,104,106,112}
# print(a.intersection(b))



# a = { 10,20,30,40}
# b = { 30,40,50,60}
# print(a.difference(b))


# a = {10,20,30}
# b = {10,20,30,40,50}
# print(a.issubset(b))



# a = "banana"
# b = set(a)
# print(b)



# a = {10,20,30,40}
# b = {20,30,50}
# c = {20,30,60}
# print(a.intersection(b,c))



# emp = {
#     "Rahul": 24000,
#     "Riya": 36000,
#     "Amit": 28000,
#     "Yogita":67000,
# }
# print(emp)




# emp = {
#     "Rahul": 24000,
#     "Riya": 36000,
#     "Amit": 28000,
#     "Yogita":67000,
# }
# highest = max(emp, key=emp.get)
# print(highest)
# print(emp[highest])








# emp = {
#     "Rahul": 24000,
#     "Riya": 36000,
#     "Amit": 28000,
#     "Yogita":67000,
# }
# total = 0
# for i in emp:
#     total = total +emp[i]
# print(total)




# a = "banana"
# d = {}
# for i in a:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1
# print(d)



# keys = ["name","age","city"]
# values = ["rahul",22,"pune"]
# c = dict(zip(keys, values))
# print(c)


# a = {"name":"rahul", "age":23}
# b = {"city":"pune", "salary":26000}
# a.update(b)
# print(a)



# products = {
#     "mobile": 33000,
#     "mouse":400,
#     "keyboard":700,
#     "pen":30,
#     "bag":900
# }
# for i in products:
#     if products[i]> 500:
#         print(i,products[i])




# students = {
#     "student1": {
#         "name": "Rahul",
#         "marks": 80
#     },
#     "student2": {
#         "name": "Priya",
#         "marks": 90
#     },
#     "student3": {
#         "name": "Amit",
#         "marks": 70
#     }
# }
# for i in students:
#     print(students[i])


# student = {
#     "name": "Rahul",
#     "age": 22,
#     "city": "Pune"
# }
# if "age" in student:
#     print("Key exists")
# else:
#     print("Key not found")



# marks = {
#     "Python": 90,
#     "Java": 75,
#     "SQL": 85,
#     "HTML": 80
# }
# highest = max(marks, key=marks.get)
# print("Highest subject =", highest)
# print("Marks =", marks[highest])