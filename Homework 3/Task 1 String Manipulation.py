inputString = "Hello World"

l = len(inputString)
newString = ""

# looping through the string
for i in range(0, len(inputString)):
	if l < 2:
		break
	else:
		if i in (0, 1, l-2, l-1):
			newString = newString + inputString[i]
		else:
			continue

# Printing New String
print("Input string : " + inputString)
print("New String : " + newString)


inputString = "my"

l = len(inputString)
newString = ""

# looping through the string
for i in range(0, len(inputString)):
	if l < 2:
		break
	else:
		if i in (0, 1, l-2, l-1):
			newString = newString + inputString[i]
		else:
			continue

# Printing New String
print("Input string : " + inputString)
print("New String : " + newString)


inputString = "x"

l = len(inputString)
newString = ""

# looping through the string
for i in range(0, len(inputString)):
	if l < 2:
		break
	else:
		if i in (0, 1, l-2, l-1):
			newString = newString + inputString[i]
		else:
			continue

# Printing New String
print("Input string : " + inputString)
print("New String : " + newString)