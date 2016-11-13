# -*- coding: utf-8 -*-

import math


def quadratic(a, b, c):
    s = b * b - 4 * a * c
    if s < 0:
        return
    elif s > 0:
        x1 = (- b + math.sqrt(s)) / (2 * a)
        x2 = (- b - math.sqrt(s)) / (2 * a)
        return x1,x2
    else:
        x = (- b + math.sqrt(s)) / (2 * a)
        return x
a = int(input('Please input a = '))
b = int(input('Please input b = '))
c = int(input('Please input c = '))
if a == 0:
    print('变成一元一次方程组辣')
else:
    print('方程 %sx**2+%sx+%s=0的解为：%s '%(a,b,c,quadratic(a,b,c)))