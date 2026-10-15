charges = [62, 28, 85, 14, 47]
lowestCharge = charges[0]
lowBatteryCount = 0
moreThanEighty = False
max = 0
total = 0

for i in charges:
    if  i < lowestCharge:
        lowestCharge = i
    if i > max:
        max = i #max value test failed initially. I discovered it was an indentation error. fixed.
    total += i
    if i < 30:
        lowBatteryCount += 1
    if i >= 80:
        moreThanEighty = True
mean = total / len(charges)
print (lowestCharge, lowBatteryCount, moreThanEighty, max, total, mean)

    