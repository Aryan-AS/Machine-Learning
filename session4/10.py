list1 = ['campusxIs', 'bestFor', 'dataScientist']
#ASCI VALUE OF CAPITAL LETTERS = 65-90
for i in list1:
    for j in i:
        if "A"<j<="Z":
            list1.insert(list1.index(j)," ")
print(list1)