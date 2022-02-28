print('Задача 9. Прогрессивный налог 2')

# Мы уже писали программу, вычисляющую сумму налога по прогрессивной шкале
# в зависимости от полученного заработка:
# 13% на доход до 10 000, 20% 
# на доход от 10 000 до 50 000, 30% на доход выше 50 000.
 
# Однако во многих странах,
# использующих такую шкалу, эта сумма вычисляется более сложным способом: 
# налоговая ставка 30% на доход выше 50 000 означает,
# что 30% уплачивается не со всей суммы,
# а лишь с той ее части, которая превосходит 50 000.

# Аналогично, ставка 20% на доход от 10 000 до 50 000
# обязывает уплатить 20% лишь с той части суммы,
# которая превосходит 10 000, но не превосходит 50 000.
 
# Так, например,
# с дохода 100 000 придется заплатить такой налог:
# 30% * (100 000 − 50 000) + 20% * (50 000 − 10 000) + 13% * 10 000 = 15 000 + 8 000 + 1 300  = 24 300.

# А с дохода 30 000 — такой:
# 20% * (30 000 − 10 000) + 13% * 10 000 = 4 000 + 1 300 =  5 300.

# Напишите программу,
# которая спрашивает у пользователя его доход
# и высчитывает сумму налога для него по вышеописанным правилам.

#получить сумму дохода
profit = int(input('Введите сумму дохода за год: '))

if profit <= 0:
    tax = 'Нет налога.'
else:
    if 0 < profit <= 10000:
        tax = profit / 100 * 13
        print('Размер 13%-ного налога равен:', tax, 'руб.')
    elif 10000 < profit <= 50000:
        tax = ((profit - 10000) / 100 * 20) + 1300
        print('Размер 20%-ного налога равен:', tax, 'руб.')
    else:
        tax = ((profit - 50000) / 100 * 30) + 9300
        print('Размер 30%-ного налога равен:', tax, 'руб.')