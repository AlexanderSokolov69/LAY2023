#!/usr/bin/env python3
# coding:utf-8
verdict = ""
while verdict != "OK":
    pass1, pass2 = input(), input()
    if len(pass1) < 8:
        print("Короткий!")
    elif "123" in pass1:
        print("Простой!")
    elif pass1 != pass2:
        print("Различаются.")
    else:
        verdict = "OK"
print(verdict)

