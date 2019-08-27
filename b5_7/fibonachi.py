stop_fibo = 4000000

def fibo_generate(stop):
    """
    Генерирует последовательность фибоначи, начиная с 1 и 2 и заканчивая ближайшим до stop
    """
    generated_fibo = [1, 2]
    
    i = 1
    flag = True
    while flag != False:
        next_fibo = generated_fibo[i-1] + generated_fibo[i]
        if next_fibo < stop:
            generated_fibo.append(next_fibo)
            i += 1
        else:
            flag = False
    return generated_fibo

print(fibo_generate(stop_fibo))

def summa_chetnykh(list):
    """
    принимает на вход список чисел(list) и суммирует в нем все четные, на выходе дает полученную сумму
    """
    summa_chetnykh_result = 0;
    for num in list:
        if num % 2 == 0:
            summa_chetnykh_result += num
    return summa_chetnykh_result

print(summa_chetnykh(fibo_generate(stop_fibo)))