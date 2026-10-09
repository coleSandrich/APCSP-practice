#Z-score and Standard deviation calculator calculator
#my objective is to give the user both a Standard deviation and a Z-Score
#Z-scores are used in statistics to quantify how many standard deviations a data point is above the mean  
#Standard deviations describe entire data sets, not singular data points. They describe how far on average each data point in a data set is from the mean of the data set.
# the formula for zscore is z= (Datapoint - mean) / standardDeviation
#the formula for Standard devaition is S = sqrt( summation (each value of a dataset - Mean of dataset)^2 / (length of a dataset - 1))
#to create z score calculator, first we'll need to calculate mean and standard deviation. 
#I looked up how to do square root on python. That is the only external non-peer help I recieved on this code. I considered using the interger root code we made for while loop challenges, but I figured it wouldn't be precise enough for real statistics. 
import math
dataPoint = float(input())
dataSet = [0, 1, 1, 2, 3, 5, 8, 13, 21]
sum = 0
for i in range( 0, len(dataSet), 1):
    sum = sum + dataSet[i]
mean = sum / len(dataSet)
#I print tested mean here. It worked. 

for i in range (0, len(dataSet), 1):
   numerator = ((dataSet[i] - mean )*(dataSet[i] - mean))
radicand = (numerator / (len(dataSet) - 1 ))
standardDev = math.sqrt(radicand)
#I print tested standard deviation and got a value very close to what my TI-84 gave me, but not quite accurate


zScore = (dataPoint - mean) / standardDev 


#print(numerator)
print(standardDev)
print (zScore)

#the next step for me if I had more time would be to concatinate the user-inputted value into the dataSet