# question 4
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
#Adding 'Twitter' to it_companies
b = {'Twitter'}
it_companies.update(b)
print('after adding Twitter to it_companies:', it_companies)

#Inserting multiple IT companies at once to the set it_companies
C={'CVS Pharmacy', 'wells ford','cap gemini', 'infosys'}
it_companies.update(C)
print('updated it_companies:', it_companies)

#Removing wells ford from the set it_companies
it_companies.remove('wells ford')
print('after removing wells ford from the set it_companies :', it_companies)

# difference between remove and discard
it_companies.discard('TCS')
print('discarding TCS:',it_companies )
# By using discard function even though  the value is not present in the given input it gives the output without error
#it_companies.remove('TCS')
#print('removing TCS:',it_companies)

# Remove function removes the element if present in the list 
# and throws an error if we remove an item and the value is not present

# join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print('Joining A and B:', C)

#Intersection of A and B
D = A.intersection(B)
print('Intersection of A and B:', D)
# Is A subset of B
E= A.issubset(B)
print('subsets of A in B:', E)
#Are A and B disjoint sets
F= A.isdisjoint(B)
print('Are A and B disjoint sets:', F)
#Join A with B and B with A
G= A.union(B)
print('Joining A with B:', G)
H= B.union(A)
print('Joining B with A:',H)

#What is the symmetric difference between A and B
I= A.symmetric_difference(B)
print('the symmetric difference between A and B:', I)
# it prints out the values which are different in A and B

#Delete the sets completely
del A
del B
#print(A)
#print(B)
#By using delete function it deletes the sets completely

#Convert the ages to a set and compare the length of the list and the set.
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_len=len(age)
print('length of list:', age_len)
age_set=set(age)
print(age_set)
age_setlen=len(age_set)
print('length of set:', age_setlen)
# list can contain duplicate elements but set has no duplicates(unique and ordered)