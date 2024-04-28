def count_fibonac(a, b):
    fib = [0, 1]
    while fib[-1] <= b: # строим последовательность до б
        fib.append(fib[-1] + fib[-2])
    
    count = 0
    for num in fib:
        if a <= num <= b: # проверяем сколько чисел в промежутке
            count += 1
    
    return count

a = 1234567890 
b = 9876543210
print(count_fibonac(a, b))
