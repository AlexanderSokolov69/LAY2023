#!/usr/bin/env python3
# coding:utf-8

print("КАЛЬКУЛЯТОР 1.0")
print()
n1 = float(input("Для вычисления - введите первое число: "))
oper = input("Операция -- [ +, -, *, **, /, //, % ]: ")
n2 = float(input("Для вычисления - введите второе число: "))
print("Вычисление: ", n1, oper, n2, "=", eval(str(n1) + oper + str(n2)))
