
# RANDOM MODULE IN NUMPY
# ITS USED TO WHEN WE HAVE TO WORK WITH RANDOM NUMBERS

from numpy import random


# THIS WILL RETURN RANDOM NUMBER BETWEEN 0 TO 4 
n = random.randint(5)

print(n)



# THIS WILL GIVE ARRAY OF RANDOM NUMBER WITH GIVEN SIZE 
n1 = random.randint(10,size=(3))  # 10 IS RANGE --> 0 TO 10
print(n1)


# THIS WILL RETURN RANDOM CHOICE FROM GIVEN ARRAY

arr = [10,20,30,40]
n2 = random.choice(arr)
print(n2)