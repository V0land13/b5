"""
Класс который принимает как аргументы функцию и колличество прогонов,
при запуске считает среднее время выполнения функции
"""
class Sekundomer:
    """класс-секундомер для вычисления времени работы функции"""
    def __init__(self, func, num_runs = 10):
        self.func = func
        self.num_runs = num_runs

    def __call__(self):
        """
        Функция измерения времени выполнения кода, num_runs - количество прогонов
        """
        import time  ### Импортируем time, нужный для нашей функции
        gg = self.func   ### Созание функции из функции полученой в аргументе
        avg_time = 0
        for num_run in range(self.num_runs):
            t0 = time.time()
            ### вызываем функцию
            gg()
            t1 = time.time()
            avg_time += (t1 - t0)
            print("Выполнение прогона №%i заняло %.5f секунд" % ((num_run+1), (t1 - t0)))
        avg_time /= self.num_runs
        print("Среднее время выполнения %.5f секунд" % avg_time)


def f():
    for j in range(1000000):
        pass

def testf():
    print("тестовая функция выполнение")
    return "тестровая функция результат"

test = Sekundomer(f, 15)
test()

