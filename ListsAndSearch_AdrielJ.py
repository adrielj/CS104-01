names  = [ ]
for x in range (0,10):
    aname = input ("enter first name: ")
    names.append(aname)

searching = True

while searching is True:
    print (names)
    search = input("enter search name:")
    if search in names:
        print(search, "! Your name was found")
        answer = str(input("would you like to search for another name? "))
        if answer == "no":
            print ("okay! goodbye.")
            break
        elif answer == "yes":
            continue
    else:
        print (search, "? Sorry, that name was not found")
        answer = str(input("Would you like to search for another name? "))
        if answer == "no":
            print ("okay! goodbye.")
            break
        elif answer == "yes":
            continue
    
