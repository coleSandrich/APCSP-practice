value = 9875
passes = 0
while value >= 10:
    temp = value
    digitSum = 0
    passes = passes + 1
#I used a temporary variable to protect value, technically I don't think it's neccecary in this code.
    while temp > 0:
        digitSum += (temp % 10) #check out this cool notation Nikhil taught me instead of digitSum = (digitSum + (tem % 10))
        temp //= 10
    value = digitSum
print (value)
print (passes)