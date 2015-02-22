grade = raw_input("Please enter your score:")
g = float(grade)
if g >= 0.9:
	print "A"
elif g <0.9 >= 0.8:
	print "B"
elif g < 0.8 >= 0.7:
    	print "C"
elif g < 0.7 >= 0.6:
    	print "D"
else:
    	print "F"