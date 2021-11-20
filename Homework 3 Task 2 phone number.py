# Python program to check if given mobile number is valid 
import re

def isValid(s):
	
	# 1) Begins with 0 or 46
	# 2) Then contains 7 
	# 3) Then contains 8 digits
	Pattern = re.compile("(0|46)?[7][0-9]{8}")
	return Pattern.match(s)

# Phone number
s = "0730507051"
if (isValid(s)):
	print ("Valid Number")	
else :
	print ("Invalid Number")


