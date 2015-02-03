largest = -1
smallest = None
while True:
    num = raw_input("Enter a number: ")
    try: 
        istr = int(num)
    except: 
        istr == "done"
        print "Invalid input"
    num2 = []
    num2.append(istr)
    
    for n in num2:
		if smallest is None:
			smallest = n
		if n < smallest:
			smallest = n
    for n in num2:
        if n > largest:
            largest = n

    if num == "done" : break

    

print "Maximum is", largest
print "Minimum is", smallest