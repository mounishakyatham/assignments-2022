#question9
#Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
#kilograms in a separate list using Loop. N: No of students (Read input from user)
#Ex: L1: [150, 155, 145, 148]
#Output: [68.03, 70.3, 65.77, 67.13]

weightsInLBS = []
N = int(input("total number of students:")) 

for i in range(0, N): 
    print("enter weight in lbs for student", (i+1) , ":")
    # the line below takes input from the user
    weight = int(input()) 
    # adding the user entered weights to weightsInLBS 
    weightsInLBS.append(weight)
    print("student weights in LBS : ", weightsInLBS) 
    # converting each student weight in weightsInLBS from lbs to kilograms
    weightsInKGS = [item/2.205 for item in weightsInLBS] 
    print("student weights in KGS : ", weightsInKGS) 
