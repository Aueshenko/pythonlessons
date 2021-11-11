file = open("C:\Games\data.txt", "rt")
data = file.read()
words = data.split()
print('Количество слов в документе: ', len(words))

file2 = open("C:\Games\data.txt", "rt")
data = file2.read().replace(" ","")
number_letters = len(data)
print('Количество букв в документе: ', number_letters)

file3 = open("C:\Games\data.txt", "rt")
i=0
for line in file3:
    i += 1
print('Количество строк в документе: ', i)
