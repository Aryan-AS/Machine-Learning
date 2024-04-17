a = int(input("Enter the x1 coordinate"))
b = int(input("Enter the x2 coordinate"))
c = int(input("Enter the y1 coordinate"))
d = int(input("Enter the y2 coordinate"))

calc = pow(pow((b-a),2) + pow((d-c),2),0.5)
print(calc)