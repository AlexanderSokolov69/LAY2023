#!/usr/bin/env python3
# coding:utf-8
def lunar_sensor(data):
    try:
        return sum(map(float, data))
    except Exception:
        return None


data = ['400', '59.', '0', '86', 'g ', '4.81518', '9', '97.0']
print(lunar_sensor(data))
