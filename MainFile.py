import datetime


def fib(n):
    """Функция возвращает n-ый элемент ряда Фиббоначи"""
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return fib(n-1) + fib(n-2)


array = []
n = 0
summa = 0

print("Начался подсчет суммы четных элементов ряда Фиббоначи, меньших 4 млн.")

start = datetime.datetime.now()

while True:
    n = n + 1
    a = fib(n)
    if a >= 4*10**6:
        break
    if (a % 2) == 0:
        summa = summa + a

finish = datetime.datetime.now()
ellapsed_time = finish - start

print("Расчет закончен и занял", ellapsed_time.seconds, "секунд.")
print("Сумма = ", summa)


# Начался подсчет суммы четных элементов ряда Фиббоначи, меньших 4 млн.
# Расчет закончен и занял 5 секунд.
# Сумма =  4613732
#
# Process finished with exit code 0
