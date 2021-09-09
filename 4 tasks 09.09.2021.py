#TASK 0 (Найти максимальный элемент в списке чисел)
number=[1,5,10,15,20,25,105,999]
max=1
for x in number:
    if(x>max):
        max=x
print('Максимальное число списка:',max)

#TASK 1 (Найти самое длинное слово из списка)
words = ['тест','текст','рекордддддд','номер','телефон','андройд','айфон','дом']
l = 0
for word in words:
    if len(word)>l:
        result=word
        l=len(word)
print('Самое длинное слово в списке:',result)

#TASK 2 (Список слов, короче 5 букв)
resultlist=[]
for word in words:
    if len(word)<5:
        resultlist.append(word)
print('Список слов короче 5 букв:',resultlist)

#TASK 3 (Разделить на 2 списка: список слов,начинающихся на гласную и на согласную)
vowels=[]
consonants=[]
for word in words:
    if word[0] in ['а','о','у','э','ы','я','ё','е','ю','и']:
        vowels.append(word)
    else:
        consonants.append(word)
print('Гласный список:',vowels)
print('Согласный список',consonants)
