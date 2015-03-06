# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
sum = 0

#iterate through file to find specific string 
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	count = 0
	
	#search for numbers 
	num = line.find('0')
	for n in line:
		count += 1
	
	#select number string only
	set = line[num:]
	sum += float(set.strip())
	
	average = sum/count	

print "Average spam confidence:" , average    