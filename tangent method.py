from numpy import *
def my_func(x, a=8, b=8.6):
    return exp(-a * x) + exp(b * x)
import xlrd, xlwt
from xlutils.copy import copy
book = xlrd.open_workbook('test.xls')
sheet = book.sheet_by_index(0)
write_book = copy(book)
sheet1 = write_book.get_sheet(0)
sheet1.write(0,29,'Метод касательных')
sheet1.write(1,29,'Номер итерации')
sheet1.write(1,30,'a')
sheet1.write(1,31,'b')
sheet1.write(1,32,"f'(a)")
sheet1.write(1,33,"f'(b)")
sheet1.write(1,34,'Колличество вызовов функции')
def deriv(x):
    return -8*exp(-8*x) + 8.6*exp(8.6*x)
def tangential(func, a_start, b_start, eps):
    func_calcs = 0
    iters = 0
    x_values = []
    func_values = []
    a, b = a_start, b_start
    local_interval = [[a, b]]
    sheet1.write(2, 29, 0)
    sheet1.write(2, 30, a)
    sheet1.write(2, 31, b)
    sheet1.write(2, 32, deriv(a))
    sheet1.write(2, 33, deriv(b))
    sheet1.write(2, 34, 0)
    while b - a > eps:
        deriv_a = deriv(a)
        deriv_b = deriv(b)
        func_a = func(a)
        func_b = func(b)
        x_values.append([a, b])
        func_values.append([func_a, func_b])
        c = (func_b - func_a + deriv_a * a - deriv_b * b) / (deriv_a - deriv_b)
        deriv_c = deriv(c)
        func_calcs += 2
        if deriv_c > 0:
            b = c
        elif deriv_c < 0:
            a = c
        elif deriv_c == 0:
            a = c
            b = c
            break

        local_interval.append([a,b])
        func_values.append([func_a, func_b])
        iters += 1
        sheet1.write(iters + 2, 29, iters)
        sheet1.write(iters + 2, 30, a)
        sheet1.write(iters + 2, 31, b)
        sheet1.write(iters + 2, 32, deriv(a))
        sheet1.write(iters + 2, 33, deriv(b))
        sheet1.write(iters + 2, 34, func_calcs)
    return {'x_min': (a + b) / 2.0, 'func_min': func((a + b) / 2.0),
            'func_calсs': func_calcs, 'localization_interval': local_interval}
print(tangential(my_func,-1,1,0.0000001))
write_book.save("test.xls")