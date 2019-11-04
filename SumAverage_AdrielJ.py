#Sum/Average Program
#Adriel Juarez
#s1288772

import statistics

numberlist  = [ ]
for x in range (0,20):
    number = int(input("Type in a number."))
    numberlist.append(number)

print ("The sum of your numbers is", (sum(numberlist)))
print ("The average of your numbers is", (statistics.mean(numberlist)))



    
