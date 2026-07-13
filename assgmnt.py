# positive or negative
# posneg=lambda a: "positive" if a>0 else "Negative or zero"
# num=int(input("Enter a number"))
# print(posneg(num))

#even or odd
# evenodd=lambda a: "even" if a%2==0 else "odd"
# num=int(input("Enter a number"))
# print(evenodd(num))

#largest
# lar=lambda a,b: a if a>b else b
# print(lar(20,10))

# largest = lambda a, b, c: a if (a >= b and a >= c) else (b if b >= c else c)
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
# print("Largest number is:", largest(num1, num2, num3))

#age
# vote = lambda age: "eligible" if age>=18 else "Not eligible"
# age = int(input("Enter age: "))
# print(vote(age))

#divisible by 5
# div=lambda a: "Divisible" if a%5==0 else "not divisible"
# num=int(input("Enter a number"))
# print(div(num))

#divisible by 5&3
# div=lambda a: "Divisible" if a%5==0 and a%3==0 else "not divisible"
# num=int(input("Enter a number "))
# print(div(num))

#zerodivision error
# try:
#     num = int(input("Enter a number: "))
#     result = 100 / num
#     print(result)
# except ZeroDivisionError:
#     print("Cannot divide by zero.")
# except ValueError:
#     print("Please enter a valid integer.")
# finally:
#     print("Execution completed.")

#
# ValueError
# try:
#     num= int(input("Enter a number: "))
#     print(num)
# except ValueError:
#     print("enter a valid number")

#filenotfounderror
# try:
#     with open("python.txt", "r") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("File not found.")

#index error
# numbers = [10, 20, 30]
# try:
#     print(numbers[5])
# except IndexError:
#     print("Index out of range")

#key error
# student = {
#     "name": "Anshika",
#     "age": 20,
#     "course": "data analytics"
# }
# try:
#     print(student["mark"]) 
# except KeyError:
#     print("Key not found")

# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except ValueError:
#     print("Please enter a valid integer.")

#create text file and write
# Create a text file and write name and address

# with  open("sample.txt", "w")as f:

#   f.write("Name: Anshika P\n")
#   f.write("Address: Thalassery, Kerala\n")
# print("Data written successfully.")

#read and display content
# with open("sample.txt","r") as f:
#     data=f.read()
# print(data)

#append a new line
# with open("sample.txt","a") as f:
#     f.write("Ph:12344")











