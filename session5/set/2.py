Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
a = set(Str1)
print(a)
meow = set()
count = 0
for i in a:
    if i not in meow:
        if i=="a" or i =="e" or i =="i" or i =="o" or i =="u" or i=="A" or i =="E" or i =="I" or i =="O" or i =="U":
            meow.add(i)
            count = count + 1

print(count)
