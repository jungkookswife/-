'''
Входные данные содержат N положительных целых чисел. Эти числа не обязательно отличаются друг от друга (может получиться так, что два или более из них будут равны). Ваша задача – выбрать несколько заданных чисел (1 ≤ несколько ≤ N) таким образом, чтобы сумма выбранных чисел была кратна N, т.е. равнялась N · k для некоторого целого k.
Исходные данные
Первая строка входа содержит целое число N (1 ≤ N ≤ 10000). Каждая из следующих N строк содержит по одному целому числу из заданного набора. Каждое из этих чисел положительное и не превышает 15000.
Результат
Если целевой набор чисел не может быть найден, выведите единственное число 0. В противном случае, выведите количество выбранных чисел в первой строке, а далее сами выбранные числа (каждое в отдельной строке) в произвольном порядке.
Если существует более одного набора чисел с требуемыми свойствами, можно вывести любой из них.
'''

def find_sum_numbers():
    N = int(input())  # считываем количество чисел
    numbers = []  # создаем список для хранения чисел
    for _ in range(N):
        num = int(input())  # считываем очередное число
        numbers.append(num)  # добавляем его в список

    # создаем список для хранения выбранных чисел
    selected_numbers = []

    # перебираем все возможные комбинации чисел (с использованием битовых масок)
    for i in range(1, 2 ** N):
        subset_sum = 0  # сумма выбранных чисел в текущей комбинации
        subset = []  # выбранные числа в текущей комбинации

        # проверяем каждый бит текущей маски
        for j in range(N):
            if i & (1 << j):
                subset_sum += numbers[j]
                subset.append(numbers[j])

        # если сумма выбранных чисел кратна N, возвращаем эту комбинацию
        if subset_sum % N == 0:
            return len(subset), subset

    # если не найдено ни одной комбинации, возвращаем 0
    return 0


# вызываем функцию и выводим результат
result = find_sum_numbers()
print(result[0])
if result[0] > 0:
    for num in result[1]:
        print(num)
