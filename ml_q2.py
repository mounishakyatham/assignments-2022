
# QUESTION 2
# Dictionary with data values
dog={}
#  adding name,color,breed,legs,age to the dictionary called dog
dog['name'] = 'messi'
dog['color'] = 'black and tan'
dog['breed'] = 'german shepherd'
dog['legs'] = 4
dog['age'] = 9
print('information of dog:' , dog)
# i have created a dictionary called dog and assigned the name,color,breed,legs,age to the dictionary

#Create a student dictionary and add first_name, last_name, gender, age, marital status,
#skills, country, city and address as keys for the dictionary
student_dict={}
student_dict={'first_name': 'Mounisha' , 'last_name': 'Kyatham' , 'gender': 'Female' , 'age':24 , 'marital status': 'NotMarried',
'skills': ['python','java'] , 'country': 'USA' , 'city': 'Overlandpark' , 'address': 'ranchapartments' , 'zipcode': 66223}
print('Biodata of student:' , student_dict )
# I created a student dictionary and initialized the values to first_name, last_name, gender, age, marital status,
#skills, country, city and address as keys for the dictionary

# To get the length of the student dictionary i have used len() function
print('lenght of student dictionary:' , len(student_dict))


# Get the value of skills and check the data type, it should be a list
print('student skills:' , student_dict['skills'])
print('type of skills:' , type(student_dict['skills']))
# To know the type of skills i have used type() function

#Modify the skills values by adding one skill
student_dict['skills'].append('devops')
print(' after adding one more skill to skills:', student_dict['skills'] )
# added skill called devops to the skills

# Get the dictionary keys as a list
print('student_dictionary keys as a list:' , list(student_dict.keys()))

#Get the dictionary values as a list
print('student_dictionary values as a list:' , list(student_dict.values()))
# To display the student dictionary keys and values as a list i have used list(student_dict.keys())) and list(student_dict.values()))
