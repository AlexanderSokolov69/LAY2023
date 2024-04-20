#!/usr/bin/env python3
# coding:utf-8
BLACK = 2
WHITE = 1


# Удобная функция для вычисления цвета противника
def opponent(color):
    if color == WHITE:
        return BLACK
    return WHITE


class Figure:
    def __init__(self, color):
        self.color = color

    def char(self):
        return ' '

    def get_color(self):
        return self.color

    def can_move(self, board, row, col, row1, col1):
        if row == row1 and col == col1:
            return False
        return 0 <= row1 < 8 and 0 <= col1 < 8

    def __repr__(self):
        return f"<{self.char()}-{'w' if self.get_color() == WHITE else 'b'}>"


class Pawn(Figure):
    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if col != col1:
            return False

        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1:
            if board.field[row1][col1]:
                return False
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        if board.field[row1][col1] and self.get_color() != board.field[row1][col1].get_color():
            direction = 1 if (self.color == WHITE) else -1
            return row + direction == row1 and (col + 1 == col1 or col - 1 == col1)
        return False


class Rook(Figure):
    def char(self):
        return 'R'

    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Knight(Figure):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        r = abs(row - row)
        c = abs(col - col)
        if r != 0 and c != 0 and r + c == 3:
            return True
        return False

    def char(self):
        return 'N'


class Bishop(Figure):
    def char(self):
        return 'B'

    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        r = abs(row - row)
        c = abs(col - col)
        if r == c:
            return True
        return False


class Queen(Figure):
    def char(self):
        return 'Q'

    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if not ((row - row1 == 0) or (col - col1 == 0) or (
                abs(row - row1) == abs(col - col1))):
            return False
        curr_row = row
        curr_col = col
        while not (curr_row == row1 and curr_col == col1):
            if row1 > curr_row:
                curr_row += 1
            elif row1 < curr_row:
                curr_row -= 1
            if col1 > curr_col:
                curr_col += 1
            elif col1 < curr_col:
                curr_col -= 1
            if board.field[curr_row][curr_col]:
                if curr_col == col1 and curr_row == row1 \
                        and self.get_color() != board.field[curr_row][curr_col].get_color():
                    return True
                return False
        return True


class King(Figure):
    def char(self):
        return 'K'

    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        # Невозможно сделать ход в клетку, которая не лежит в том же ряду
        # или столбце клеток.
        if abs(row - row) > 1 or abs(col - col) > 1:
            return False

        return True


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        self.bild()

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row1, col1, color):
        for row in range(8):
            for col in range(8):
                piece = self.field[row][col]
                if piece:
                    if piece.get_color() == color:
                        if piece.can_move(row1, col1):
                            return True
        return False

    def get_piece(self, row, col):
        return self.field[row][col]

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        figs = {'Q': Queen, 'R': Rook, 'B': Bishop, 'N': Knight}
        if self.field[row][col]:
            if self.get_piece(row, col).char() != 'P':
                return False
            color = self.field[row][col].get_color()
            if self.field[row][col].can_move(self, row, col, row1, col1):
                self.field[row][col] = None
                self.field[row1][col1] = figs[char](color)
                return True
            if self.field[row][col].can_attack(self, row, col, row1, col1):
                self.field[row][col] = None
                self.field[row1][col1] = figs[char](color)
                return True
        return False

    def bild(self):
        self.field.clear()
        for row in range(8):
            self.field.append([None] * 8)
        return


if __name__ == '__main__':
    board = Board()
    board.field = [([None] * 8) for i in range(8)]
    board.field[6][0] = Pawn(WHITE)
    board.field[6][1] = Pawn(WHITE)
    board.field[6][7] = Pawn(WHITE)

    board.field[2][1] = Pawn(BLACK)
    board.field[2][4] = Pawn(BLACK)

    print('before:')
    for row in range(7, -1, -1):
        for col in range(8):
            char = board.cell(row, col)[1]
            print(char.replace(' ', '-'), end='')
        print()
    print()

    print(board.move_and_promote_pawn(6, 0, 7, 0, 'Q'))
    print(board.move_piece(2, 1, 1, 1))

    print(board.move_and_promote_pawn(6, 1, 7, 1, 'N'))
    print(board.move_piece(2, 4, 1, 4))

    print(board.move_piece(7, 1, 6, 3))
    print(board.move_and_promote_pawn(1, 1, 0, 1, 'R'))

    print(board.move_piece(6, 3, 7, 5))
    print(board.move_and_promote_pawn(1, 4, 0, 4, 'Q'))

    print(board.move_and_promote_pawn(6, 7, 7, 7, 'Q'))

    print(board.get_piece(7, 0).get_color())
    print(board.get_piece(7, 5).get_color())
