amount_input = 0
namber_5=0
while amount_input < 10:
    namber = input('Введите число:')
    amount_input += 1
    for i in namber:
      if i == str(5):
        namber_5 += 1

print('Количество цифр 5:', namber_5)
