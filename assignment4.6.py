def computepay(h,r):
	if h > 40:
    	p = ((h - 40) * r * 1.5) + (40 * r)
        return p
    
hrs = raw_input("Enter Hours:")
h = float(hrs)

rate = raw_input("Enter Rate:")
r = float(rate)

p = computepay(h,r)
        
print p