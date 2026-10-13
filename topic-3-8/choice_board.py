#Z-score and Standard deviation calculator 
#my objective is to give the user Standard Deviation and Z-Score
#Z-scores are used in statistics to quantify how many standard deviations a data point is above the mean  
#Standard deviations describe entire data sets, not singular data points. They describe how far on average each data point in a data set is from the mean of the data set.
# the formula for zscore is z= (Datapoint - mean) / standardDeviation
#the formula for Standard devaition is S = sqrt( summation (each value of a dataset - Mean of dataset)^2 / (length of a dataset - 1))
#my add-on will Identify statistical outliers, and max/min value
 
import math
dataPoint = float(input())
dataSet = [0, 1, 1, 2, 3, 5, 8, 13, 21]
#dataSet.append(dataPoint)


minValue = dataSet[0]
for i in range(0, len(dataSet), 1):
 if dataSet[i] < minValue:
    minValue = dataSet[i]
print(minValue)

maxValue = dataSet[0]
for i in range(0, len(dataSet), 1):
 if dataSet[i] > maxValue:
    maxValue = dataSet[i]
print(maxValue)



Quartile1 = float((dataSet[2] + dataSet[3]) / 2)
Quartile3 = float((dataSet[6] + dataSet[7]) / 2)
IQR = Quartile3 - Quartile1 
for i in range(0, len(dataSet), 1):
    if (dataSet[i] < (Quartile1- 1.5*float(IQR))) or (dataSet[i] > (Quartile3 + 1.5*float(IQR))):
        print( "OUTLIERS:", dataSet[i] )
else:
    print("NO OUTLIERS")
    


sum = 0
for i in range( 0, len(dataSet), 1):
    sum += dataSet[i]
mean = sum / len(dataSet)

numerator = 0
for i in range (0, len(dataSet), 1):
   numerator += ((dataSet[i] - mean )*(dataSet[i] - mean))
radicand = (numerator / (len(dataSet) - 1 ))
standardDev = math.sqrt(radicand)



zScore = (dataPoint - mean) / standardDev 


#print(numerator)
print(standardDev)
print (zScore)

#the next step for me if I had more time would be to append the user-inputted value into the dataSet