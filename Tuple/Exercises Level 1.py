# Create an empty tuple
tuple = ()
print(tuple)

# Create a tuple containing names of your sisters and your brothers 
sister = ("Anjana" , "Puspa" , "Kinjal")
brother = ("Jagdish" , "Ashish" , "Anil")
print(sister)
print(brother)

# Join brothers and sisters tuples and assign it to 
siblings=sister+brother
print(siblings)

# How many siblings do you have
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father=("MuljiBhai")
mother=("SangitaBen")
family_member=(father,mother,*siblings)
print(family_member)

# Unpack siblings and parents from family_members
Father, Mother, *Siblings = family_members
print(Father)
print(Mother)
print(Siblings)