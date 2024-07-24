summa = int(input('Введите сумму всех продуктов:'))
skidka = input('Есть ли у вас дисконтная карта?')
prossent = 0.4
if skidka == 'Да':
    print(summa * prossent)
else:
    print(summa)