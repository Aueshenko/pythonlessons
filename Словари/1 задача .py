#TASK Дано 2 списка: ключи и значения. Создать из них словарь.

keys = ['Russia','France','Belarus','Ukraine','Usa']
values = ['Moscow','Paris','Minsk','Kiev','Washington']
keys_values = dict(zip(keys, values))
print(keys_values)