# question1
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# sorting ages
ages.sort()
print('after sorting the ages:' , ages)

# printing minimum value in the given string
Minimum=min(ages)
print("Minimum value in the string: ", Minimum)

# printing maximum value in the given string
Maximum=max(ages)
print("Maximum value in the string: ", Maximum)

# adding min and max value again to the list
ages.append(19)
ages.append(26)
print('adding min and max values again to the list:' , ages)
# calculating median value
import statistics
# Store it in another variable.
median = statistics.median(ages)
# Print the median (middle value) of the given list items.
print("The median of the given list items", ages, " = ", median)

# finding the average of the given list
sumofages = sum(ages)
count = len(ages)
average = sumofages / count
print("The average of all the ages is:", average)

# finding the range
range = Maximum - Minimum
print('the range of the given ages:' , range)

# First i took the ages as input and sorted them , finded out the minimum age and maximum age from the input, to the given input i have added
#i have added the min and max ages again to the input list by using append method. Next i have caluclated the median value by Importing 
#statistics , average and range values are calculated by using formula.x


