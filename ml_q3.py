# question 3 
 #Create a tuple containing names of your sisters and your brothers
 
a_tuple = ("snehika", "likitha")
# printing name of sisters
print('name of sisters:', a_tuple)
b_tuple= ('purushotham','nitish',)
# printing name of brothers
print("name of brothers:", b_tuple)
#Joining brothers and sisters tuples and assigning it to siblings
siblings= a_tuple + b_tuple
print('name of siblings:', siblings)
# added brothers and sisters to the variable called siblings by using AND operator

# How many siblings do you have?
num=len(siblings)
print('number of siblings:', num)
# Calculating the number of siblings by using len() function

#Modify the siblings tuple and add the name of your father and mother and assign it to
#family_members
# as tuples are immutable we are converting it into list, modifying and then converting it into tuple again  
family_members=list(siblings)

#adding the name of my father and mother and assigning it to family_members
parents=['gangareddy', 'laxmi']
family_members = tuple(family_members + parents)
print('name of the family members:', family_members)