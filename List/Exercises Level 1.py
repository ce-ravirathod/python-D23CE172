# Declare an empty list
a=[]

# add items to list
a.append('hello world !!!')

# Display list
print(a)

# Declare a list with more than 5 items
b=[1,'Ravi',3.14,'Rathod',5]

#  Find the length of your list
print(len(b))

# Get the first item, the middle item and the last item of the list
print(b[0])
print(b[int(len(b)/2)])
print(b[len(b)-1])

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
c=['ravi',19,5.5,'unmarride','jamnagar']
print(c)

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

# Print the list using _print()_
print(it_companies)

# Print the number of companies in the list
print(len(it_companies))

# Print the first, middle and last company
print(it_companies[0])
print(it_companies[int(len(it_companies)/2)])
print(it_companies[len(it_companies)-1])

# Print the list after modifying one of the companies
it_companies[0]="Meta"
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Instagram')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(4,'Dell')
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1]=it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;&nbsp; '
s='#;&nbsp;'
s.join(it_companies)
print(it_companies)
print(s.join(it_companies))

#Check if a certain company exists in the it_companies list.
find='Meta'
if find in it_companies: 
    print("find") 
else: 
    print("not find")

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[:3])

#  Slice out the last 3 companies from the list
print(it_companies[-3:])

# Slice out the middle IT company or companies from the list
print(it_companies[int(len(it_companies)/2)])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(int(len(it_companies)/2))
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies


# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack=front_end[:]
print(full_stack)
full_stack.insert(full_stack.index('Redux')+1,'Python')
full_stack.insert(full_stack.index('Redux')+2,'SQL')
print(full_stack)