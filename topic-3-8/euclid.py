a = 48
b = 18
rep = 0
while b != 0:
    temp = a % b 
    a = b
    b = temp
    rep = rep + 1
print(a)
print(rep)