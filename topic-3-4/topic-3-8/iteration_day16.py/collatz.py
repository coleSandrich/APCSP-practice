n = int(input())
count = 0
peak = 0
while (n != 1) and n < 1000000 and count < 1000 :
    if (n % 2 == 0):
       n = n // 2
    else: 
        n = (3*n) + 1
    count = int(count) + 1
    if n > peak:
        peak = n
else:
    if n != 1:
        print ("LIMIT REACHED")

if n == 1:
    print("REACHED 1")
print (count)
print(peak)

