from numpy import *
def func(x, a=8, b=8.6):
    return exp(-a * x) + exp(b * x)
import xlrd, xlwt
from xlutils.copy import copy
book = xlrd.open_workbook('test.xls')
sheet = book.sheet_by_index(0)
write_book = copy(book)
sheet1 = write_book.get_sheet(0)
sheet1.write(0,0,'Метод дихотомии')
sheet1.write(1,0,'Номер итерации')
sheet1.write(1,1,'Интервал локализации')
sheet1.write(1,3,'Колличество вызовов функции')
def dichotomy(func, a_start, b_start, eps):
    a = a_start
    b = b_start
    local_interval = [[a, b]]
    sheet1.write(2, 0, 0)
    sheet1.write(2, 1, a_start)
    sheet1.write(2, 2, b_start)
    sheet1.write(2, 3, 0)
    delta = eps / 2.0
    interval_length = b - a
    iters = 0
    func_calcs = 0
    while interval_length > eps:
        c = (a + b - delta) / 2.0
        d = (a + b + delta) / 2.0
        if func(c) > func(d):
            a = c
        else:
            b = d
        interval_length = b - a
        func_calcs += 2
        iters += 1
        local_interval.append([a, b])
        sheet1.write(iters + 2, 0, iters)
        sheet1.write(iters + 2, 1, a)
        sheet1.write(iters + 2, 2, b)
        sheet1.write(iters + 2, 3, func_calcs )
    return {'x_min' : (a + b) / 2.0, 'func_min' : func((a + b)/2.0), 'func_calcs' : func_calcs, 'localization_interval' : local_interval}
print(dichotomy(func,-1,1,0.00000001))
write_book.save("test.xls")