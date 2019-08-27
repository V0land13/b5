class Sekundomer:
    """класс-секундомер для вычисления времени работы функции"""
    def __init__(self, num_runs = 10, func):
        self.num_runs = num_runs
        self.func = func

    def __call__(self):
        """
        Создает функцию измерения времени выполнения кода, num_runs - количество прогонов
        """
        import time  ### Импортируем time, нужный для нашей функции
        lala = self.func
        #self.func

        def my_decorator(lala): # декоратор, вызывается только в момент декорирования
            def wrapped(): #Обертка, вызывается каждый раз как вызываем функцию
                avg_time = 0
                for num_run in range(self.num_runs):
                    t0 = time.time()
                    ### вызываем функцию
                    func()

                    t1 = time.time()
                    avg_time += (t1 - t0)
                    print("Выполнение прогона №%i заняло %.5f секунд" % ((num_run+1), (t1 - t0)))
                avg_time /= num_runs
                print("Среднее время выполнения %.5f секунд" % avg_time)
            return wrapped
        return my_decorator

test = Sekundomer(15)

@test
def f():
    for j in range(1000000):
        pass

f()

