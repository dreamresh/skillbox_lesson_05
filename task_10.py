print('Задача 10. Почта')

# Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед,
# а в 10:00 и 18:00 приезжают машины с посылками,
# и тогда все сотрудники на два часа заняты их разгрузкой.
# Во время обеда, разумеется, посылки никто не выдаёт,
# как и в моменты, когда разгружаются машины.

# Напишите программу,
# которая получает на вход время в часах — число от 0 до 23 — и пишет,
# можно ли в этот час получить посылку.
# Используйте только один условный оператор if-else, без elif и прочего.

# Решите задание двумя способами:

# первый — при выполнении условия выводится сообщение:
# «Можно получить посылку»,
print('Когда условия выполняются')
hours = int(input('Укажите час, в который желаете забрать посылку: '))
if (8 <= hours < 10) or (12 <= hours < 14) or (15 <= hours < 18) or (20 <= hours < 22):
    print('Можно получить посылку.')
else:
    print('Посылку получить нельзя.')
print('Всего хорошего.')

# второй —  при выполнении условия выводится сообщение:
# «Посылку получить нельзя».
print('Когда условия не выполняются')
hours = int(input('Укажите час, в который желаете забрать посылку: '))
if (hours < 8) or (10 <= hours < 12) or (14 <= hours < 15) or (18 <= hours < 20) or (22 <= hours):
    print('Посылку получить нельзя.')
else:
    print('Можно получить посылку.')
print('Всего хорошего.')