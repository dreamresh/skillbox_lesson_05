print('Задача 6. Защита от дурака')

# Мы участвуем в разработке приложения для математиков, где можно будет делать всё,
# начиная от простейших вычислений и заканчивая построением сложных графиков.
# В этом приложении реализована установка диапазона чисел,
# и нам необходимо написать этакую «защиту от дурака».
# 
# 
# Напишите программу,
# которая получает на вход число и проверяет, двузначное оно или нет.
# Выведите соответствующее сообщение. Числа −42 и −99 тоже считаются двузначными.
# Сделайте это, используя не более одного оператора if-elsе. Не используйте elif.

numbers = int(input('Введите двузначное число: '))
if numbers < -99 or numbers > -10 and numbers < 10 or numbers > 99:
    print('Ошибка: число', numbers, 'не является двузначным.')
else: #если вывод не требуется, то можно и без неё обойтись
    print('Двузначное число:', numbers)