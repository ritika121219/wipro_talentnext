#cubes every no in the given list_1=[1,2,3,4,5,6,7,8,9]
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Using lambda function to cube each number
cubed_list = list(map(lambda x: x**3, list_1))

print(cubed_list)
