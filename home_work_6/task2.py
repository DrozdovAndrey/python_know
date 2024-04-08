__all__ = ['check_queens']
#
# def is_attacking(q1, q2):
#     '''Функция, проверяющую, бьют ли ферзи друг друга'''
#     pass
#
# def check_queens(queens):
#     '''Функция, которая проверяет все возможные пары ферзей'''
#
#     len_queens = len(queens)
#     if len_queens == 1:
#         return True
#     chess_table = create_table(len_queens)
#     for i in queens:
#         # if chess_table[i[0] - 1][i[1] - 1] == 0:
#         chess_table[i[0] - 1][i[1] - 1] = 1
#         # else:
#         #     return False
#     if check_row(chess_table) and check_column(chess_table) and check_diagonal(chess_table):
#         return True
#     else:
#         return False
#
#
# def create_table(len_queens):
#     return [([0 for _ in range(len_queens)]) for _ in range(len_queens)]
#
#
# def check_row(chess_table):
#     flag = True
#     for i in chess_table:
#         if sum(i) > 1:
#             return False
#     return flag
#
#
# def check_column(chess_table):
#     len_table = len(chess_table)
#     reversed_table = create_table(len_table)
#     for row in range(len_table):
#         for colomn in range(len_table):
#             reversed_table[colomn][row] = chess_table[row][colomn]
#     return check_row(reversed_table)
#
#
# def check_diagonal(chess_table):
#     len_mtr = len(chess_table)
#     b = len_mtr * 2 - 1
#     all_diag = [[] for _ in range(b * 2)]
#     for i in range(len_mtr):
#         for j in range(len_mtr):
#             all_diag[i + j].append(chess_table[j][i])
#             all_diag[i + j + b].append(chess_table[~j][i])
#     return check_row(all_diag)
#
#



# Решение из задачи
from itertools import combinations

def is_attacking(q1, q2):
    # Проверяем, бьют ли ферзи друг друга
    return q1[0] == q2[0] or q1[1] == q2[1] or abs(q1[0] - q2[0]) == abs(q1[1] - q2[1])

def check_queens(queens):
    # Проверяем все возможные пары ферзей
    for q1, q2 in combinations(queens, 2):
        if is_attacking(q1, q2):
            return False
    return True
