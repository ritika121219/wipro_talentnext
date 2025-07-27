#ques 1. WAP to check if a given no is positive , negetive or zero.
num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")


#ques2. WAP to check if given no is odd or even.
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("The number is Even.")
else:
    print("The number is Odd.")


#ques3. given two non negative value, print true if they have the same last digit, such as with 27 and 57.

num1 = int(input("Enter first non-negative number: "))
num2 = int(input("Enter second non-negative number: "))

if num1 % 10 == num2 % 10:
    print("True")  # Same last digit
else:
    print("False")  # Different last digits


#ques4. WAP to print no from 1 to 10 in a single row with on tab space.
for i in range(1, 11):
    print(i, end="\t")

#ques.5WAP to print even no between 23 and 57.each no should be printed in a separate row.
# Print even numbers from 23 to 57
for num in range(23, 58):  
    if num % 2 == 0:
        print(num)

#ques6. WAP to check if a given no is prime or not.
# Take input from the user
num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

#ques7. WAP to print prime no between 10 and 99.
# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            return False
    return True

for number in range(10, 100):
    if is_prime(number):
        print(number)

#ques8. WAP to print the sum of all given digits of a given no.
num = int(input("Enter a number: "))
sum_of_digits = 0
while num > 0:
    digit = num % 10        
    sum_of_digits += digit  
    num = num // 10        


print("Sum of digits:", sum_of_digits)

#ques9. WAP to reverse a given no and print.
num = int(input("Enter a number: "))
original = num
is_negative = False
if num < 0:
    is_negative = True
    num = -num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if is_negative:
    reversed_num = -reversed_num

print("Reversed number:", reversed_num)

#ques10. WAP to find if the given no is palidrome or not.

num = int(input("Enter a number: "))
original = num

if num < 0:
    print("Not a palindrome")
else:
    
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10

    
    if original == reversed_num:
        print("Palindrome number")
    else:
        print("Not a palindrome")
