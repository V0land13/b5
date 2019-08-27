def time_this(num_runs):
    """
    Функция измерения времени выполнения кода, num_runs - количество прогонов
    """
    import time  ### Импортируем time, нужный для нашей функции
    def my_decorator(func): # декоратор, вызывается только в момент декорирования
        def wrapped(): #Обертка, вызывается каждый раз как вызываем функцию
            avg_time = 0
            for num_run in range(num_runs):
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


@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass


f()

