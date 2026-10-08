value = 314159
 = 0
while value >= 10:
    temp = value
    digitSum = 0

    while temp > 0:
        digitSum += (temp % 10)
        temp //=10