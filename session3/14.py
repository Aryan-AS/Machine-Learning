s = str(input("Enter the string"))
sum = 0
total = 0
for i in s:
    if i == "0" or "1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9"or "0":
    # if i.isdigit():
        sum = sum + int(i)
        total = total + 1
average = sum/total

print(sum)
print(average)

