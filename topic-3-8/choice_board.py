#Z-score calculator
#Z scores are used in statistics to quantify how many standard deviations a data point is above the mean  
# the formula is z= (Datapoint - mean) / standardDeviation
#to create z score calculator, first we'll need to calculate mean and standard deviation. For mean, I'll write program. 
#I looked up how to do square root on python, and it turns out I need to import math. I considered using the interger root code we made for while loop challenges, but I figured it wouldn't be precise enough for real statistics.
import math
dataPoint = float(input())
dataSet = [0, 1, 1, 2, 3, 5, 8, 13, 21]
sum = 0
for i in range( 0, len(dataSet), 1):
    sum = sum + dataSet[i]
mean = sum / len(dataSet)
#print(mean) #to test to make sure it works. it prints 6.0 which is correct

#standardDev = 6.9821
for i in range (0, len(dataSet), 1):
   numerator = ((dataSet[i] - mean )*(dataSet[i]-mean))
radicand = (numerator / (len(dataSet) - 1 ))
standardDev2 = math.sqrt(radicand)

zScore = (dataPoint - mean) / standardDev2 
#print(Zscore)
#extension: I am gonna try to make a standard deviation calculator to integrate in my Z-score calculation
#the formula for Standard devaition is S = sqrt( summation (each values of a dataset - Mean of dataset)^2 / (length of a dataset - 1))
#print(numerator)
print(standardDev2)
print (zScore)