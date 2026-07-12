def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    
    if operator == '-':
        return num1 - num2
    
    if operator == '*':
        return num1 * num2
    
    if operator == '**':
        return num1 ** num2
    
    if operator == '%':
        return num1 % num2
    
    if operator == '/':
        if num2 != 0:
            return num1 / num2
        return ZeroDivisionError
    
    if operator == '//':
        if num2 != 0:
            return num1 // num2
        return ZeroDivisionError
    
    # If the user enters a letter for a number or the wrong operator,
    # return the error for the entered value
    return ValueError
    

fnum = float(input("Enter your first number: "))
snum = float(input("Enter your second number: "))
operator = input("Enter one of these opereators: +, -, *, **, %, // or /: ")

print(calculate(fnum, snum, operator))