s1 = str(input("Enter the string"))
s2 = str(input("Enter the string"))
s3 = []
for i in s1.split():
    for j in s2.split():
        if (i!=j):
            s3.append(j)
print(s3)

