#Калькулятор с возможностью счета в одну строку + память результата прошлой операции

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
help_number = ['1','2','3','4','5','6','7','8','9','0']
a = 1

while a == 1:
    
    work = input()

    for x in work:
        if x in help_number and operation == '':
            number1 += x
        elif x in help_number and operation != '':
            number2 += x
        elif x in ['+','-','*','/']:
            operation = x
        elif x == '_' and operation == '':
            number1 = result
        elif x == '_' and operation != '':
            number2 = result
        
    result = calculation(number1,number2,operation)
    print('> ', result)
    number1 = ''
    number2 = ''
    operation = ''

    
    