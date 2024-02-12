# A) Create a list and apply methods (append, extend, remove, reverse), arrange
# created list in ascending and descending order.
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

my_list.append(5)
print("Append :",my_list)

my_list.extend([5, 8, 9])
print("extend :",my_list)

my_list.remove(5)
print("remove :",my_list)

my_list.reverse()
print("reverse :",my_list)

my_list.sort()
print("List in ascending order:", my_list)

my_list.sort(reverse=True)
print("List in descending order:", my_list)


# B) List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana",
# "orange"]]
# From above list get word “orange” and “Python” & repeat this list five times without
# using loops.
my_list = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]

word1 = my_list[8][2]
print("Word 1:", word1)

word2 = my_list[4][0].capitalize()
print("Word 2:", word2)

new_list = [my_list] * 5
print("Repeated list:", new_list)


# C) Create a list and copy it using slice function
original_list = [1, 2, 3, 4, 5]

copied_list = original_list[:]

print("Original List:", original_list)
print("Copied List:", copied_list)


# D) Create a tuple and apply different type of mathematical operation on it (Sum,
# Maximum, minimum etc.).
my_tuple = (1, 2, 3, 4, 5)

sum_tuple = sum(my_tuple)
print("Sum of Tuple:", sum_tuple)

max_tuple = max(my_tuple)
print("Maximum value in Tuple:", max_tuple)

min_tuple = min(my_tuple)
print("Minimum value in Tuple:", min_tuple)