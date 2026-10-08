n = 17
lower = 0
upper = 1001
while (upper - lower) > 1:
    midPoint = (lower +upper ) // 2
    if (midPoint*midPoint) <= n:
        lower = midPoint
    else:
        upper = midPoint
print(lower)