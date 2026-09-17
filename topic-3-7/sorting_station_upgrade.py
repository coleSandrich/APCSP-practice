#Cole Sandrich 9/17
label = input()

shape = str(label[0 : 4])
color = str(label[4 : 7])
size = int(label[7 : 10])
mass = int(label[10 : 14])
condition = str(label[14])


destination = "E"
if condition == "D" or (size > 50 or mass > 2000):
    destination = "inspect"
else:
    if color == "RED" and (size > 10):
       destination = "B"
       
    elif shape == "BALL":
        destination = "A"
    if color == ("BLU" or "GRN") and (shape == "CUBE") and (size < 10):
        destination = "C"
    elif shape == "CUBE":
        destination = "D"
print(destination)

if destination == "inspect":
    print("HOLD")
elif shape == "CONE" or (mass > 1000):
    print("CRATE")
elif shape == "BALL":
    print("PADDED")
else:
    print("BOX")

