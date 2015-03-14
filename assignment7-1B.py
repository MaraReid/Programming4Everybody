# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
inp = fh.read()
inp = inp.strip()
print inp.upper()