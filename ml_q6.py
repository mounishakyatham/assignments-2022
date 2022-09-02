
#Question 6
#“I am a teacher and I love to inspire and teach people”

sentence = "I am a teacher and I love to inspire and teach people"
a = len(set(sentence.split(' ')))
# How many unique words have been used in the sentence
print('number of unique elements:', a)
#First i have collected the individual words into a list by using split() method. 
# Then, I converted it to set to get unique elements and used len() to find out the 
# number of unique words