#ques1. WAP to print the 4th element from first and 4th element from last in a tupple.
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)

if len(my_tuple) >= 4:
    fourth_from_start = my_tuple[3]       
    fourth_from_end = my_tuple[-4]  
    print("4th element from start:", fourth_from_start)
    print("4th element from end:", fourth_from_end)
else:
    print("The tuple does not have enough elements.")


#ques2. WAP to check whether an element exists in a tuple or not.
my_tuple = (10, 20, 30, 40, 50)

element = int(input("Enter the element to search: "))

if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")


#ques3. WAP to convert a list into tuple.

my_list = [10, 20, 30, 40, 50]

my_tuple = tuple(my_list)

print("Original List:", my_list)
print("Converted Tuple:", my_tuple)


#ques4. WAP to find the index of an item in atuple.
my_tuple = (10, 20, 30, 40, 50)


item = int(input("Enter the item to find its index: "))

if item in my_tuple:
    index = my_tuple.index(item)
    print(f"Index of {item} is: {index}")
else:
    print(f"{item} not found in the tuple.")


#ques5. WAP to replace last value of tuples in a list to 100.
tuple_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]


updated_list = [t[:-1] + (100,) for t in tuple_list]


print("Updated List of Tuples:", updated_list)
