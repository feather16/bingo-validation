import copy
import numpy as np
import time

N = 5

def transpose(table):
    return np.array(table).T.tolist()

# ビンゴ
def score(table) -> int:
    N = len(table)
    table_t = transpose(table)
    ret = 0
    for i in range(N):
        if all(table[i]): ret += 1
        if all(table_t[i]): ret += 1
    if all(table[j][j] for j in range(N)): ret += 1
    if all(table[j][N - 1 - j] for j in range(N)): ret += 1
    return ret

# リーチ
def chance(table) -> int:
    N = len(table)
    table_t = transpose(table)
    indices = set()
    for i in range(N):
        if table[i].count(True) == N - 1: indices.add((i, table[i].index(False)))
        if table_t[i].count(True) == N - 1: indices.add((table_t[i].index(False), i))
    if [table[j][j] for j in range(N)].count(True) == N - 1:
        j = [table[j][j] for j in range(N)].index(False)
        indices.add((j, j))
    if [table[j][N - 1 - j] for j in range(N)].count(True) == N - 1:
        j = [table[j][N - 1 - j] for j in range(N)].index(False)
        indices.add((j, j))
    return len(indices)
 
max_chance = 0
max_tables = []
start_t = time.time()
for i in range(2 ** (N ** 2)):
    table = []
    for j in range(N):
        table.append([])
        for k in range(N):
            table[j].append((i >> (k + N * j)) % 2 == 1)
    if score(table) == 0:
        chance_value = chance(table)
        if chance_value > max_chance:
            max_tables = [copy.copy(table)]
            max_chance = chance_value
        elif chance_value == max_chance:
            max_tables.append(copy.copy(table))
print(f'time = {time.time() - start_t}')

print(f'max_chance = {max_chance}')
def print_table(table):
    print('+' + ('-' * (2 * N - 1)) + '+')
    for row in table:
        print('|' + (' '.join(['o' if b else 'x' for b in row])) + '|')
    print('+' + ('-' * (2 * N - 1)) + '+')
for table in max_tables:
    print_table(table)
