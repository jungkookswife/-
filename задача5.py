'''
Десять математиков летели на воздушном шаре над Тихим океаном. Когда они пересекали экватор, они решили отметить это событие и открыли бутылку шампанского. К сожалению, пробка пробила дыру в воздушном шаре. Водород начал вытекать, а шар — снижаться. Скоро он упадёт в океан, и все воздухоплаватели будут съедены голодными акулами.
Но пока ещё не всё потеряно. Один из воздухоплавателей может выпрыгнуть, пожертвовав собой, чтобы его друзья смогли пожить чуть дольше. Осталась только одна проблема — кто будет этим человеком. Есть честный способ решить этот вопрос. Сначала каждый из математиков напишет целое число ai, не меньшее 1 и не большее 10 000. После чего они найдут волшебное число N, равное количеству положительных делителей произведения a1*a2*…*a10. Например, количество положительных целых делителей числа 6 равно 4 (делители 1, 2, 3, 6). Герой (математик, который будет выброшен) определится последней цифрой числа N. Ваша задача — найти эту цифру.
Исходные данные
Ввод содержит десять целых чисел, каждое число в отдельной строке.
Результат
Выведите одну цифру от 0 до 9 — последнюю цифру N.
'''

import sys

# чтение входных данных
numbers = []
for _ in range(10):
    numbers.append(int(sys.stdin.readline()))

# вычисление произведения чисел
product = 1
for num in numbers:
    product *= num

# подсчет количества делителей
divisors = 0
for i in range(1, product+1):
    if product % i == 0:
        divisors += 1

# нахождение последней цифры делителей
last_digit = divisors % 10

# вывод результата
print(last_digit)
