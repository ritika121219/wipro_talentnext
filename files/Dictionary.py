#ques1. WAP to add a key and value to dictionary.
student = {"name": "Alice", "age": 20}

student["grade"] = "A"
print("Updated dictionary:", student)

#ques2. WAP to concate the following dictionaries to create a new one.

dict1 = {'a': 100, 'b': 200}
dict2 = {'c': 300, 'd': 400}
dict3 = {'e': 500, 'f': 600}

merged_dict = {}

for d in (dict1, dict2, dict3):
    merged_dict.update(d)

print("Merged Dictionary:", merged_dict)


#ques3. WAP to check if given key already exists in a dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter key to check: ")


if key in my_dict:
    print(f"Key '{key}' exists in the dictionary with value: {my_dict[key]}")
else:
    print(f"Key '{key}' does not exist in the dictionary.")

#ques4. WAP to iterate over a dictionary using for loop and print the keys alone, values alone and both values.

my_dict = {'name': 'Alice', 'age': 25, 'city': 'Delhi'}


print("Keys:")
for key in my_dict:
    print(key)


print("\nValues:")
for value in my_dict.values():
    print(value)


print("\nKey-Value Pairs:")
for key, value in my_dict.items():
    print(f"{key}: {value}")


#ques5. WAP to prepare a dictonary where keys are no between 1 and 15 (both included) and the value are squaew of the keys.

square_dict = {x: x**2 for x in range(1, 16)}

print("Dictionary of squares from 1 to 15:")
print(square_dict)


#ques6. WAP to sum all the value in a dictionary,considering the value will be int type.
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

total = sum(my_dict.values())

print("Sum of all values in the dictionary:", total)
