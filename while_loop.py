# Print No. 1 to 100
"""
i = 1
while i <=3:
    print(i)
    i+=1
    
    """

# print No. 100 to 1
"""
i = 100
while i >= 1:
    print(i)
    i -= 1
"""

# Write a program to do Sum of N series. N value should be entered by user.
# Input Please enter number to get sum of N Series 5
# Output :- Sum of 1 to 5 :- 15

"""
n = int(input("Enter number: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(f"Sum of 1 to {n} : {sum}")
"""
"""
# for create table of given number:
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1
"""
# Factorial calculator with user input
# Program to calculate the factorial of a positive integer,
# ensuring the input is valid using a while loop.
""""
n = int(input("enter number: "))
if n > 0:
   fact_result = 1
   print(f"cal of {n}")
for i in range(1, n+1):
   fact_result = fact_result * i
   print(f"{fact_result}")
"""
"""""
Numbers = input("enter any number:")
if (float(Numbers) % 2 == 0):
     print(f"{Numbers} is even")
else:
     print("No is odd")
     """
for i in range (1, 6):
  print(" " * (5 - i)  + "*" * (2*i - 1))