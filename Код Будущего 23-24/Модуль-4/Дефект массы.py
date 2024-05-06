#!/usr/bin/env python3
# coding:utf-8
def mass_defect(pp, pn, el):
    return pp * P + pn * N - nuclears[el]


nuclears = {'H1': 1.00783,
            'H2': 2.0141,
            'He3': 3.01602}
P, N = 1.00728, 1.00866
print(mass_defect(2, 1, 'He3'))