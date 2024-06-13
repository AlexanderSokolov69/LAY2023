#!/usr/bin/env python3
# coding:utf-8
class Table:
    def __init__(self, rows, cols):
        self.__table = [[0] * cols for _ in range(rows)]
        self.__rows = rows
        self.__cols = cols

    def get_value(self, row, col):
        if row not in range(self.__rows) or col not in range(self.__cols):
            return
        return self.__table[row][col]

    def set_value(self, row, col, value):
        self.__table[row][col] = value

    def n_rows(self):
        return self.__rows

    def n_cols(self):
        return self.__cols

    def delete_row(self, row):
        del self.__table[row]
        self.__rows -= 1

    def delete_col(self, col):
        for row in self.__table:
            del row[col]
        self.__cols -= 1

    def add_row(self, row):
        self.__table.insert(row, [0] * self.__cols)
        self.__rows += 1

    def add_col(self, col):
        for row in self.__table:
            row.insert(col, 0)
        self.__cols += 1
