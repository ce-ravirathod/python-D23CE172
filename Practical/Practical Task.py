# String

# 1 Reverse the given string (You can take any string)
string = "hello world"
reversed_string = string[::-1]
print(reversed_string)

# 2 Replace some character of the string with another character without using a loop.
original_string = "Hello, World!"
new_string = original_string.replace("o", "x")
print(new_string) 

# 3 Find whether the character in the given string or not.
string = "Hello, World!"
position = string.find("o")
print(position)

# 4 Create tuple,list and set and convert them into the different string !
my_tuple = (1, 2, 3)
my_list = [1, 2, 3]
my_set = {1, 2, 3}
string_tuple = str(my_tuple)
string_list = str(my_list)
string_set = str(my_set)
print(type(string_tuple),string_tuple)
print(type(string_list),string_list)
print(type(string_set),string_set)

# 5 Convert all the string characters to the upper and the lower case and split it with the different methods.
text = "Hello, World!"
upper_case = text.upper()
lower_case = text.lower()
print(upper_case)
print(lower_case)
print(text.split(","))

# 6 Perform the following operations to the tuple and the list -> Find max, min, len, sum.
my_tuple1 = (1, 2, 3, 4)
my_list1 = [1, 2, 3, 4]

tuplemax=max(my_tuple1)
tuplemin=min(my_tuple1)
tuplelen=len(my_tuple1)
tuplesum=sum(my_tuple1)

listmax=max(my_list1)
listmin=min(my_list1)
listlen=len(my_list1)
listsum=sum(my_list1)

print("List_Max :",listmax)
print("List_Min :",listmin)
print("List_Len :",listlen)
print("List_Sum :",listsum)

print("Tuple_Max :",tuplemax)
print("Tuple_min :",tuplemin)
print("Tuple_Len :",tuplelen)
print("Tuple_Sum :",tuplesum)

# 7 Copy one list to the another list without using the copy command.
original_list = [1, 2, 3]
new_list = original_list
print(new_list)

# 8. Perform below task as instructed
# 	-> Create a dictionary named student with keys: 'name', 'age', and 'grade'. Assign 	values accordingly.
# 	   Access Dictionary Values:
# 	-> Print the 'age' of the student from the dictionary created in Exercise 1.
# 	   Modify Dictionary Values:
# 	-> Update the 'grade' of the student to a new value.
# 	-> Check if the key 'gender' is present in the student dictionary. Print a message 	based on the result.

student = {'name': 'John', 'age': 20, 'grade': 'A'}
print(student['age']) 

student['grade'] = 'B'
print(student['grade']) 

if 'gender' in student:
    print("The key 'gender' is present in the student dictionary.")
else:
    print("The key 'gender' is not present in the student dictionary.")

# 9. Perform below task as instructed
# 	-> Create two sets: set1 with elements (1, 2, 3) and set2 with elements (3, 4, 5).
# 	Union of Sets:
# 	-> Find the union of set1 and set2 and print the result.
# 	Intersection of Sets:
# 	-> Find the intersection of set1 and set2 and print the result.
# 	Difference of Sets:
# 	-> Find the elements that are in set1 but not in set2 and print the result.
# 	Check Subset:
# 	-> Check if set1 is a subset of set2. Print a message based on the result.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print("Union :",union_set)

intersection_set = set1.intersection(set2)
print("Inter_Section :",intersection_set)

difference_set = set1.difference(set2)
print("Different Set_1 to Set_2 :",difference_set)

if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

# 10. Perform below task as instructed
# 	Create a dictionary where keys are subjects ('math', 'science') and values are sets of students who take those subjects.
# 	Update Set Values:
# 	Add a new student to the 'math' subject in the dictionary from Exercise 11.
# 	Remove Set Values:
# 	Remove a student from the 'science' subject in the dictionary from Exercise 11.
# 	Check Common Students:
# 	Find and print the students who take both 'math' and 'science'.
# 	Nested Dictionary:
# 	Create a nested dictionary where each key represents a country, and the value is another dictionary containing cities and their populations.
students = {'math': {'John', 'Anil;', 'Ravi'}, 'science': {'Parv', 'Ravi', 'David'}}
print(students)

students['math'].add('Parv')
print(students)

students['science'].remove('David')
print(students)

common_students = students['math'].intersection(students['science'])
print(common_students)

countries = {'USA': {'New York': 8398748, 'Los Angeles': 3990456, 'Chicago': 2705994}, 'China': {'Shanghai': 24183300, 'Beijing': 21707000, 'Guangzhou': 14043500}}
print(countries)

# 11. Create two lists, one containing elements at even indices and the other containing elements at odd indices from the original list.
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_indices_list = original_list[::2]
odd_indices_list = original_list[1::2]
print(even_indices_list, odd_indices_list)

# 12. Use tuple packing and unpacking to swap the values of two variables without using a temporary variable.
a = 5
b = 10
a, b = b, a
print(a, b)

# 13. Check if a given list is a palindrome using slicing.
my_list = [1, 2, 3, 2, 1]
is_palindrome = my_list == my_list[::-1]
print(is_palindrome) 

# 14. oncatenate two tuples without using the + operator.

import itertools

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple(itertools.chain(tuple1, tuple2))
print(concatenated_tuple) 
# lst1=list(tuple1)
# lst2=list(tuple2)
# lst1.append(lst2)
# print(tuple(lst1))