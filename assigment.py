#while loop
text = input("Enter a string: ")
i = 0
while i < len(text):
    if text[i] != " ":
        print(text[i],end="")
    i = i + 1

#print characters greater than 4 
words = ["apple", "cat", "banana", "dog", "orange", "pen"]
i = 0
while i < len(words):
    if len(words[i]) > 4:
        print(words[i])
    i = i + 1

#uupercase letters
text = input("Enter a string: ")
count = 0
i = 0
while i < len(text):
    if text[i].isupper():
        count = count + 1
    i = i + 1
print("Number of uppercase letters:", count)


#print len of each word in list
words = ["apple", "cat", "banana", "dog", "orange"]
i = 0
while i < len(words):
    print(words[i], ":", len(words[i]))
    i = i + 1

#number of vowels
words = ["apple", "cat", "banana", "dog", "orange"]
count=0
i = 0
vowels="AEIOUaeiou"
while i < len(words):
    for ch in words[i]:
        if ch in vowels:
         count+=1
    i = i + 1
print("No of vowels:",count)

#Functions
#write a function that take a list and removes dulpicates
def rem(li):
    newlist = []
    for i in li:
        if i not in newlist:
            newlist.append(i)
    return newlist
numbers = [10, 20, 10, 30, 20, 40, 50, 40]
result = rem(numbers)
print("List after removing duplicates:", result)

#write a function to accept a sentence and returns the number of words
def count(sentence):
    words = sentence.split()
    return len(words)
text = input("Enter a sentence: ")
result = count(text)
print("Number of words:", result)

#palindrome
def palindrome(text):
    rvrs_str = ""
    for ch in text:
        rvrs_str = ch + rvrs_str
    if text == rvrs_str:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")
word = input("Enter a string: ")
palindrome(word)

#function that takes list of numbers and return sum
def find_sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total
lst = [10, 20, 30, 40, 50]
result = find_sum(lst)
print("Sum =", result)

#calculate avg of 3 numbers
def average(a, b, c):
    return (a + b + c) / 3
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print("Average =", average(num1, num2, num3))

#accept a list and return new list with even numbers
def even_numbers(lst):
    even_list = []
    for i in lst:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
numbers = [2, 15, 8, 7, 22, 13, 18, 5]
result = even_numbers(numbers)
print("Original List:", numbers)
print("Even List:", result)

#digits in in a number
def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
    return count
number = int(input("Enter a number: "))
print("Number of digits =", count_digits(number))


#sum of even digits in a number
def sumevendigits(num):
    sum = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            sum = sum + digit
        num = num // 10
    return sum
number = int(input("Enter a number: "))
print("Sum of even digits =", sumevendigits(number))








         
