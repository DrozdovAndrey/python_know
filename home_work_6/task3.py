import task2
from random import randint as rnd


def generate_boards():
    count = 0
    queen_in_boards = []
    while count < 4:
        random_queen = []
        for i in range(0, 8):
            random_queen.append((i + 1, rnd(1, 8)))
        if task2.check_queens(random_queen):
            queen_in_boards.append(random_queen)
            count += 1
    return queen_in_boards


board_list = generate_boards()
if len(board_list) != 4:
    print("Вы собрали не то количество комбинаций")
else:
    print("Отлично!")


# milliseconds = int(str(round(time.time() * 1000))[-1])
# print(milliseconds)
