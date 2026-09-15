clock_value = 45
remaining = clock_value

bit_1 = remaining % 2
remaining = remaining //2
bit_2 = remaining % 2
remaining = remaining // 2
bit_4 = remaining % 2
remaining = remaining // 2
bit_8 = remaining % 2
remaining = remaining // 2
bit_16 = remaining % 2
remaining = remaining // 2
bit_32 = remaining % 2

print(bit_32, bit_16, bit_8, bit_4, bit_2, bit_1)

seconds = 59
next_seconds = (seconds + 1) % 60
print(next_seconds)


clock_values = [13, 42]
labels = ["hours", "minutes"]

clock_values.append(17)
labels.append("seconds")

selected_index = 2

clock_value = clock_values[selected_index]
label = labels[selected_index]

bit_list = [0,0,0,0,0,0]

remaining = clock_value

bit_list[5] = remaining % 2
remaining = remaining // 2
bit_list[4] = remaining % 2
remaining = remaining // 2
bit_list[3] = remaining % 2
remaining = remaining // 2
bit_list[2]= remaining % 2
remaining = remaining // 2
bit_list[1] = remaining % 2
remaining = remaining // 2
bit_list[0] = remaining % 2

bit_text = str(bit_list[0]) + str(bit_list[1]) + str(bit_list[2]) + str(bit_list[3]) + str(bit_list[4]) + str(bit_list[5])
print(bit_text)
check_value = bit_list[0] * 32 + bit_list[1] * 16 + bit_list[2] * 8 + bit_list[3] * 4 + bit_list[4] * 2 + bit_list[5] * 1  # How do you make this from bit_list?
print(clock_value == check_value) # should print True
"seconds: 17 -> 010001"