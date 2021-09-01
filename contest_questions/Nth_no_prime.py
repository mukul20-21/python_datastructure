import math
num = int(input("Enter the number:"))
try:
	result = math.factorial(num)
	print(result)
except:
	print("factorial is not print for negative number")