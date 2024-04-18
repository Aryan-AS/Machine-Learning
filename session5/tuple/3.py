t1 = (1,2,3,0)
t2 = (1,1,2,3)
for i,j in zip(t1,t2):
    if i == j:
        print("t1 and t2 are the same")
        break
    else:
        print("t1 and t2 are not same")
        break



