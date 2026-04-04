#1 count positive numbers
# numbers = [1,-3,2,-5,4,6,-7,-8,9]
# positive_number_count = 0
# for num in numbers:
#     if num > 0:
#         positive_number_count =positive_number_count + 1
# print("Final count of Positive number is:",positive_number_count)

# 2 sum of even numbers 
# n =int(input("Enter the number:"))
# sum_even = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         sum_even = sum_even+i

# print("Sum of even number:",sum_even)

#3 multiplication table printer
# number =int(input("Enter the number:"))

# for i in range(1,11):
#     if i == 5:
#         continue
#     print(number, 'x', i, '=', number*i)

#4 Reversing a string
# input_str = input("Enter the str:")
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str

# print(reversed_str)
#5find the first non repeated char
# input_str= "teether"

# for char in input_str:
#     if input_str.count(char) == 1:
#         print("Char is:", char)
#         break

#6Factorial calculations 
# number = int(input("Enter the number:"))
# factorial = int(input("Enter the number:"))

# while number > 0:
#     factorial = factorial * number
#     number = number - 1

# print("Factorial of value is:",factorial)

#7 validate input 
# while True:
#     number = int(input("Enter value b/w 1 and 10:"))
#     if 1<= number <=10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid number, try again")

#8prime no checker
# number = int(input("Enter the number:"))
# is_prime = True

# if number > 1:
#     for i in range(2,number):
#         if (number % i) == 0:
#             is_prime = False
#             break
# print(is_prime)

#9List uniqueeness
# items = ["apple","banana","orange","apple","mango"]

# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate:",item)
#         break
#     unique_item.add(item)

#10 Exponential backoff
import time

wait_time = 1
max_retries = 5
attemps = 0

while attemps < max_retries:
    print("Attempt",attemps, +1,"wait time",wait_time)
    time.sleep(wait_time)
    wait_time = wait_time * 2
    attemps = attemps + 1 
