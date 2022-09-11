def convert(c):
	F=(9/5)*c+32
	return F
try:
    celsius=float(input("Enter the temp in celsius:"))
    Fah=convert(celsius)
    print(f"The temperature in fahrenheit {Fah}")
except:
    print("Enter the numric value")    
