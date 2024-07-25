"""input a number
Convert it to Celsius, and also into Fahrenheit
Fahrenheit = 9/5C + 32 Celsius
Celsius = 5/9 (F-32) Fahrenheit"""

n = float(input("Enter your Number: "))

f = ((9/5)*(n+ 32)) 
c= ((5/9)*(n-32))
print(c, "Celsius\n",f, "and Fahrenheit")
