# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    x = line.find('0')
    y = line[20:]
    y = float(y)
    count += 1
    sum += float(y)
average = sum/count    
print "Average spam confidence:", average

