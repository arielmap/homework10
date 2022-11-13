import datetime
import time



def logger(function):
    def wrapper(*args):
        log_msg = f'{datetime.datetime.now():%d.%m.%Y %H:%M:%S}\t'
        log_msg += 'функция f = (n + 1) ^ n \t'
        log_msg += f"n: {', '.join(map(str, args))}\t"
        res = function(*args)
        log_msg += f'результат: {res}\n'
        with open('log_file.log', 'a', encoding='utf-8') as lf:
            lf.write(log_msg)
        return res
    return wrapper


def timer(function):
    def wrapper(*args):
        start = time.time_ns()
        res = function(*args,)
        finish = time.time_ns()
        print(finish - start)
        return res
    return wrapper


@logger
@timer
def function(n):
    res = (1 + n) ** n
    return res


function(1)
function(2)
function(3)
function(4)
function(5)
function(6)
function(7)
function(8)
function(9)
function(10)
