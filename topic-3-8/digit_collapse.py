value = 9875
passes = 0
while value >= 10:
    temp = value
    digitSum = 0
    passes = passes + 1

    while temp > 0:
        digitSum += (temp % 10)
        temp //=10
    value = digitSum
print (value)
print (passes)