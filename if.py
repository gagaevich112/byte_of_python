number = 23
guess = int(input('Введите целое число:'))

if guess == number:
    print('Поздравляю, вы угадали') # новый блок
    print('(Хотя и не получили ни чего!)') # здесь заканчивается блок
elif guess < number:
    print('агаданное число немного больше')
else:
    print('Нет больше этого ')

print('Завершено')