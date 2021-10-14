# TASK 1.1 посчитать количество слов в ней

words = 'hello my teacher hello my friends'
words_new = words.split()
print(len(words_new))

# TASK 1.2 превратить в заголовок ('the best' -> 'The Best')

words = 'hello my teacher hello my friends'
print(words.title())

# TASK 1.3 заменить все гласные на звездочки (hello -> h*ll*)

words = 'hello my teacher hello my friends AND LAST TEST'
for x in words:
    if x in "aeiuyoAEIUYO":
        words = words.replace(x,'*')
        
print(words)

# TASK 1.4 выбросить из нее все слова короче 4 букв

words = 'hello my teacher hello my friends'
words_new = words.split()
words_finish = []

for word in words_new:
    if len(word)>4:
        words_finish.append(word)

print(words_finish)