Sample_String = 'CampusX is an Online Mentorship Program fOr EnginEering studentS.'

def casecalculator(Sample_String):
 sum1=0
 sum2=0
 for i in Sample_String:
    if i.isupper():
        sum1 = sum1 + 1
    if i.islower():
        sum2 = sum2+1
 print("The upper case strings are",sum1)
 print("The lower case strings are",sum2)

casecalculator(Sample_String)
