import random

base_string = input("Your string: ")

i = 1
while i <= 5:

result = random.choices(base_string, k=5)
print("".join(result))

i += 1