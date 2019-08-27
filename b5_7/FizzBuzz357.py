"""
Покажите вывод функции для чисел от 1 до 100.
"""

def fizzbuzz(number):
    """
    Функцию, которая принимает на вход число, а в ответ выводит:
    FizzBuzz, если число делится на 3 и 5 и 7 ;
    Buzz, если число делится на 3 или 5 или 7;
    Fizz, если число делится и на 3 и 5 или на 5 и 7 или на 3 и 7.
    """
    if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
        return "FizzBuzz"
    
    elif number % 3 == 0 and number % 5 == 0:
        return "Fizz"
    elif number % 5 == 0 and number % 7 == 0:
        return "Fizz"
    elif number % 3 == 0 and number % 7 == 0:
        return "Fizz"
    
    elif number % 3 == 0:
        return "Buzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 7 == 0:
        return "Buzz"
    """
    Если надо добавить вывод когда не делится ни на то ни на другое
    else:
        return "И не Fizz, и не Buzz, и даже, не FizzBuzz"
    """
    
def sumFizzBuzz():   
    diapazon = int(input("Веди до куда перебирать: "))
    sumFizzBuzz = 0
    for i in range(1,diapazon,1):
        #print(i)
        if fizzbuzz(i):
            sumFizzBuzz += i
            #print("при числе {} сумма равна {}".format(i,sumFizzBuzz))
    print(sumFizzBuzz)
    return(sumFizzBuzz)

sumFizzBuzz()