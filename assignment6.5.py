text = "X-DSPAM-Confidence:    0.8475";
string = text.find(" ")
s = float(text[19:])
print s