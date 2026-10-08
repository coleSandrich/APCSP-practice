#Z-score calculator
#Z scores are used in statistics to quantify how many standard deviations a data point is above the mean  
# the formula is z= (Datapoint - mean) / standardDeviation
#to create z score calculator, first we'll need to calculate mean and standard deviation. For mean, I'll write program. 
#for standard deviation, the formula is too complicated to program myself at this stage in my coding career, so I'll let myself use a Standard deviation value from a TI-84
dataPoint = float(input())
dataSet = [0, 1, 1, 2, 3, 5, 8, 13, 21]
standardDev = 6.9821
sum = 0
for i in range( 0, len(dataSet), 1):
    sum = sum + dataSet[i]
mean = sum / len(dataSet)
#print(mean) to test to make sure it works. it prints 6.0 which is correct
Zscore = (dataPoint - mean) / standardDev 

print(Zscore)

