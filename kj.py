def calculate_statistics(start, end):
    even_sum = 0
    odd_sum = 0
    multiple_of_9_sum = 0
    even_count = 0
    odd_count = 0
    multiple_of_9_count = 0

    for num in range(start, end+1):
        if num % 2 == 0:
            even_sum += num
            even_count += 1
        else:
            odd_sum += num
            odd_count += 1
        if num % 9 == 0:
            multiple_of_9_sum += num
            multiple_of_9_count += 1

    if even_count != 0:
        even_avg = even_sum / even_count
    else:
        even_avg = 0

    if odd_count != 0:
        odd_avg = odd_sum / odd_count
    else:
        odd_avg = 0

    if multiple_of_9_count != 0:
        multiple_of_9_avg = multiple_of_9_sum / multiple_of_9_count
    else:
        multiple_of_9_avg = 0

    return (even_sum, even_avg, odd_sum, odd_avg, multiple_of_9_sum, multiple_of_9_avg)

start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))

if start > end:
    print("Ошибка: начало диапазона больше конца диапазона")
else:
    even_sum, even_avg, odd_sum, odd_avg, multiple_of_9_sum, multiple_of_9_avg = calculate_statistics(start, end)
    print(f"Сумма четных чисел: {even_sum}, Среднее значение четных чисел: {even_avg}")
    print(f"Сумма нечетных чисел: {odd_sum}, Среднее значение нечетных чисел: {odd_avg}")
    print(f"Сумма чисел, кратных 9: {multiple_of_9_sum}, Среднее значение чисел, кратных 9: {multiple_of_9_avg}")
    #2
    def draw_vertical_line(length, symbol):
        for _ in range(length):
            print(symbol)


    length = int(input("Введите длину линии: "))
    symbol = input("Введите символ для заполнения линии: ")

    draw_vertical_line(length, symbol)
    #3


def check_number():
    while True:
        number = float(input("Введите число (для завершения введите '0'): "))
        if number > 0:
            print("Number is positive")
        elif number < 0:
            print("Number is negative")
        else:
            print("Number is equal to zero")

        if number == 0:
            print("Good bye!")
            break


check_number()
#4
def calculate_numbers():
    numbers = []
    while True:
        number = float(input("Введите число (для завершения введите '7'): "))
        if number == 7:
            break
        numbers.append(number)

    if numbers:
        print("Сумма введенных чисел:", sum(numbers))
        print("Максимальное значение:", max(numbers))
        print("Минимальное значение:", min(numbers))
    else:
        print("Вы не ввели ни одного числа.")

    print("Good bye!")

calculate_numbers()
