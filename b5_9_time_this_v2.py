class Sekundomer:
    """класс-секундомер для вычисления времени работы функции"""
    def __init__(self, func = f(), num_runs = 10):
        self.func = func
        self.num_runs = num_runs

    def __call__(self):
        """
        Функция измерения времени выполнения кода, num_runs - количество прогонов
        """
        import time  ### Импортируем time, нужный для нашей функции
        #self.func
        #self.func

        avg_time = 0
        for num_run in range(self.num_runs):
            t0 = time.time()
            ### вызываем функцию
            self.func

            t1 = time.time()
            avg_time += (t1 - t0)
            print("Выполнение прогона №%i заняло %.5f секунд" % ((num_run+1), (t1 - t0)))
        avg_time /= self.num_runs
        print("Среднее время выполнения %.5f секунд" % avg_time)


def f():
    for j in range(1000000):
        pass


test = Sekundomer(testf(), 15)
test()

