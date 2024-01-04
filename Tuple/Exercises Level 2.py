# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "broccoli", "spinach")
animal_product = ("meat", "milk", "eggs")
food_stuff_tp = fruits + vegetables + animal_product
print( food_stuff_tp)

# Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt=list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle=int(len(food_stuff_lt)/2)
print(food_stuff_lt[middle])

# Slice out the first three items and the last three items from food_staff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# Delete the food_staff_tp tuple completely
del food_stuff_tp


#Check if an item exists in  tuple:
#- Check if 'Estonia' is a nordic country
#- Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

if 'Estonia' in nordic_countries:
    print('Estonia is a nordic country.')
else:
    print('Estonia is not a nordic country.')
if 'Iceland' in nordic_countries:
 print('Iceland is a nordic country.')
else:
 print('Iceland is not a nordic country.')