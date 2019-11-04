richter = float(input("What was the recorded Richter scale magnitude?"))

if 8 <= richter <= 10:
    print ("Most of the structures have fallen.")
elif 7 <= richter < 8:
    print ("Many buildings have been destroyed")
elif 6 <= richter < 7:
    print ("Many of the buildings have been considerably damages, some will collapse.")
elif 4.5 <= richter < 6:
    print ("There is damage on poorly constructed buildings.")
else:
    print ("The number must be between 0 and 10. Try again.")
