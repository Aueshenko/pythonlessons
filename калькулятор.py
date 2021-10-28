def calculation(number1, number2, operation):
    if operation == '+':
        return int(number1) + int(number2)
    elif operation == '-':
        return int(number1) - int(number2)
    elif operation == '*':
        return int(number1) * int(number2)
    elif operation == '/':
        return int(number1) / int(number2)

number1 = ''
number2 = ''
operation = ''
result = 0

while True:
    
    work = input()

    for x in work:
        if x.isdigit() and operation == '':
            number1 += x
        elif x.isdigit() and operation != '':
            number2 += x
        elif x in ['+','-','*','/']:
            operation = x
        elif x == '_' and operation == '':
            number1 = result
        elif x == '_' and operation != '':
            number2 = result
        
    result = calculation(number1, number2, operation)
    print('> ', result)
    number1 = ''
    number2 = ''
    operation = ''
