#Дано несколько сумм, нужно найти числа, которые их образуют.
#Пример:
# Входные данные:
# 3 3 4 5
# Выходные данные:
# 1 2 3
#Объяснение:
#Есть три числа: 1, 2, 3. 
#Их суммы: 1+2=3, 1+3=4, 2+3=5. 
#Поэтому числа будут 1, 2, 3.

def find_n_integers(sum_set:list, n):
    sum_set.sort()
    result = [0] * n

    def backtrack(index, start):
        if index == n:
            return True
        for i in range(start, len(sum_set)):
            result[index] = sum_set[i] - sum_set[start]
            if index >= 2 and result[index] <= result[index - 2]:
                continue
            if index >= 3 and result[index] != result[index - 1] and result[index] != result[index - 2]:
                continue
            if backtrack(index + 1, i + 1):
                return True
        return False

    if backtrack(0, 0):
        return result
    else:
        return None

# Пример использования
sum_set = [1269, 1160, 1663]
n = 3
result = find_n_integers(sum_set, n)
if result:
    print(f"Найденные {n} целых числа: {result}")
else:
    print(f"Невозможно найти {n} целых чисел по заданному набору сумм.")
