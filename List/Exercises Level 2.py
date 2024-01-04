# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

# Sort the list and find the min and max age
ages.sort()
print(ages)
print("Min Age:", ages[0])
print("Max Age:", ages[-1])

# Add the min age and the max age again to the list
ages.extend([ages[0], ages[-1]])
print(ages)

# Find the median age (one middle item or two middle items divided by two)
middle_age = int((len(ages)/2)) 
print(int(ages[middle_age])/2)
print(middle_age)

# Find the average age (sum of all items divided by their number )
print(sum(ages) / len(ages))
print(ages)

# Find the range of the ages (max minus min)
print(max(ages) - min(ages))
print(ages)

# Compare the value of (min - average) and (max - average), use _abs()_ method
min_average_diff = abs(ages[0] - (sum(ages) / len(ages)))
max_average_diff = abs(ages[-1] - (sum(ages) / len(ages)))
print(min_average_diff)
print(max_average_diff)


# Find the middle country(ies) in the [countries list]
country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid = (len(country)) // 2
print(country[mid])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
mid = len(country) // 2
one = country[:mid + len(country) % 2]
second = country[mid + len(country) % 2:]
print(one)
print(second)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first_country, second_country, third_country, *scandic_countries = country

print( first_country)
print( second_country)
print( third_country)
print( scandic_countries)