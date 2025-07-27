#ques1. WAP to count the no of upper and lower letter in astring.
text = input("Enter a string: ")

upper_count = 0
lower_count = 0

for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)


#ques2. WAP that will check whether a given string is palindrome or not.
text = input("Enter a string: ")

text = text.lower()

text = text.replace(" ", "")
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#ques3. given a string return new string made of n copies of the first 2 char of the original string where n is length of the string. the string length will be >= 2.if the input is "wipro" the the output should be "wiwiwiwiwi".

text = input("Enter a string (length >= 2): ")

if len(text) >= 2:
    first_two = text[:2]
    result = first_two * len(text)
    print("Result:", result)
else:
    print("Error: String length must be at least 2.")


#ques4. given a string, if the first or last character is'x, return the string without those 'x'charcter, else return the string unchanged. if the input is "xHix",then output is "Hi".

text = input("Enter a string: ")

if text.startswith('x'):
    text = text[1:]
if text.endswith('x'):
    text = text[:-1]

print("Result:", text)


#ques5. given a string and an int n, return a string made of n repetitions of the last n charcter of the string. you may assume that n is between 0 and the length of the string inclusive. for example if the input and "wipro" and 3, then the output should be "propropro".

text = input("Enter a string: ")
n = int(input("Enter a number (0 to length of string): "))
if 0 <= n <= len(text):
    last_part = text[-n:]  
    result = last_part * n 
    print("Result:", result)
else:
    print("Invalid value for n.")
