def weather_calculator(value, metric):
	if metric == 'f':
		return (value * 9/5) + 32
	if metric == 'c':
		return (value - 32) * 5/9
	raise ValueError("Invalid metric. Use 'f' or 'c'.")


metric = input("Enter f to convert Celsius to Fahrenheit or c to convert Fahrenheit to Celsius: ")
value = float(input("Enter the value to be converted: "))

print(weather_calculator(value, metric.lower()))
