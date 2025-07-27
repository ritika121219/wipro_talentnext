#ques1. WAP to create a list of 5 int and display the list items.Access individual elemnets through index.

numbers = [10, 20, 30, 40, 50]
print("Full list:", numbers)

print("Element at index 0:", numbers[0])
print("Element at index 1:", numbers[1])
print("Element at index 2:", numbers[2])
print("Element at index 3:", numbers[3])
print("Element at index 4:", numbers[4])

#ques2. WAP to reverse the order of items in the list.

numbers = [10, 20, 30, 40]
numbers.reverse()

print("Reversed list:", numbers)


#ques.3 WAP to append a new item to the end of the list.

numbers = [10, 20, 30, 40, 50]
numbers.append(60)

print("Updated list after appending:", numbers)

#ques.4 WAP to print the no of occurences of the specified element in a list
numbers = [10, 20, 30, 20, 40, 20, 50]
target = int(input("Enter the number to count: "))
count = numbers.count(target)


print(f"The number {target} appears {count} time(s) in the list.")

#ques5. WAP to append rhe items of list1 and list2 in the front.

list1 = [40, 50, 60]
list2 = [10, 20, 30]
combined_list = list2 + list1

print("Combined list (list2 in front of list1):", combined_list)

#ques6. WAP to insert a new item before the second element in an existing list.

numbers = [10, 20, 30, 40, 50]
new_item = 15

numbers.insert(1, new_item)
print("Updated list:", numbers)

#ques7. WAP to remove the item from specified index in a list.

numbers = [10, 20, 30, 40, 50]
index = int(input("Enter the index of the item to remove: "))

if 0 <= index < len(numbers):
    removed_item = numbers.pop(index)
    print(f"Removed item: {removed_item}")
    print("Updated list:", numbers)
else:
    print("Invalid index! Index must be between 0 and", len(numbers)-1)

#ques8. WAP to remove the first occurence of a specified element from a list.

numbers = [10, 20, 30, 20, 40, 50]
element = int(input("Enter the element to remove: "))

if element in numbers:
    numbers.remove(element)
    print(f"First occurrence of {element} removed.")
    print("Updated list:", numbers)
else:
    print(f"{element} not found in the list.")
