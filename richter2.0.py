testing = True

while testing is True:
    richter = float(input("What was the recorded Richter scale magnitude? Type -99 to end"))
    if 8 <= richter <= 10:
        print ("Most of the structures have fallen.")
        continue
    elif 7 <= richter < 8:
        print ("Many buildings have been destroyed")
        continue
    elif 6 <= richter < 7:
        print ("Many of the buildings have been considerably damages, some will collapse.")
        continue
    elif 4.5 <= richter < 6:
        print ("There is damage on poorly constructed buildings.")
        continue
    elif richter == -99:
        print ("Goodbye.")
        testing is False
        break
    else:
        print ("The number must be between 0 and 10. Try again.")
        continue
    
