from numpy import *
def my_func(x, a=8, b=8.6):
    return exp(-a * x) + exp(b * x)
def passive_search(func, a_start, b_start, eps):
    x_values = []
    func_values= []
    min = a_start
    min_func = func(min)
    func_calcs = 1
    iters = 0
    for i in arange(a_start, b_start, eps):
        y = func(i)
        func_calcs += 1
        if y < min_func:
            min_func = y
            min = i
        iters += 1
    return {'x_min' : min, 'func_min' : min_func, 'fun_calcs' : func_calcs }
print(passive_search(my_func,-1,1,0.000001))

