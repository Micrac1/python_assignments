def fibonacci_naive(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

def fibonacci_iterative(n: int) -> int:
    a = 0
    b = 1
    for i in range(0, n):
        tmp = b
        b = a + b
        a = tmp
    return a

print(fibonacci_naive(35))
print(fibonacci_iterative(35))
print(fibonacci_iterative(20000))
