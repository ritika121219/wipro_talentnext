#ques1. WAP to accept two no as command line arguments and display their sum.
import sys

if len(sys.argv) != 3:
    print("Usage: python sum_args.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    total = num1 + num2
    print("The sum is:", total)


#ques2. WAP to accpet a welcome message through command line arguments and display the file name along with the welcome message.
import sys

if len(sys.argv) < 2:
    print("Usage: python welcome_message.py <your welcome message>")
else:
    
    filename = sys.argv[0]
    message = " ".join(sys.argv[1:]) 
    print(f"File Name: {filename}")
    print(f"Welcome Message: {message}")


#ques3. WAP to accept 10 no through command line arguments and calc the sum of prime no among them.
import sys

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if len(sys.argv) != 11:
    print("Usage: python sum_primes.py <10 integers>")
else:
    nums = list(map(int, sys.argv[1:]))  
    prime_sum = sum(num for num in nums if is_prime(num))
    print("Sum of prime numbers:", prime_sum)
