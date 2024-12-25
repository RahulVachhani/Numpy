
# STATISTICAL OPERATION IN NUMPY 

# MEAN   --> AVERAGE


# MEDIAN  --> 
# The median is a measure of central tendency in statistics that represents the middle value of a dataset when it is arranged in ascending order. If the dataset has an odd number of elements, the median is the middle value. If the dataset has an even number of elements, the median is the average of the two middle values.


# STANDARD DERIVATION



import numpy as np


# MEAN OF ARRAY   

n1 = np.array([10,20,30,40,50])
mean1 = np.mean(n1)
print('Mean of n1 is :',mean1)

n2 = np.array([[1,2,3],[4,6,8]])
mean2 = np.mean(n2)
print(f'Mean of n2 is : {mean2}')

n2 = np.array([[1,2,3],[4,6,8]])
mean2 = np.mean(n2,axis=1)
print(f'Mean of n2 is : {mean2}')



# MEDIAN 

n3 = np.array([100,20,50])   # FIRST ARRANGE IN ASSENDING ORDER [20,50,100] THEN RETURN MIDDLE VALUE 
median1 = np.median(n3)
print(f'Median of n3 is : {median1}')


n4 = np.array([100,20,30,50])   #  FIRST ARRANGE IN ASSENDING ORDER [20,30,50,100] THEN RETURN RESULT OF THIS (30+50)/2   
median2 = np.median(n4)
print(f'Median of n4 is : {median2}')




# STANDARD DERIVATION

n5 = np.array([10,20,50,60])
std = np.std(n5)
print('Standard derivation of n5  is : ',std)