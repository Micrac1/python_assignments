n = int(input('n = '))

# 1. Naivne riesenie O(n^2)
def fibonacci_recursive(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(n))

# 2. Matove povodne riesenie
def fibonacci_mato(n):
    fibonacci = [0, 1]
    for i in range(1, n):
        fibonacci.append(fibonacci[i] + fibonacci[i-1])
    return fibonacci[len(fibonacci)-1]

# 2. Iterativne riesenie O(n)
def fibonacci_iterative(n):
    fib1 = 0
    fib2 = 1
    for i in range (1, n):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
        """
        # Fetacke riesenie
        fib2 = fib2 + fib1
        fib1 = fib2 - fib1
        """
    return fib2

"""
def fibonacci(n):
    fib1 = 0
    fib2 = 1
    fib = 0 # v pythone nemusi byt, ale v realnom programovacom jazyku musi byt definovane MIMO for loopu (po for loope premenna neexistuje)
    for i in range (1, n):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib
    return fib
"""

# print(fibonacci_iterative(n)) 

"""
// Kod v c
int fibonacci(int n){
    int fib1 = 0;
    int fib2 = 1;
    int fib;
    for (int i = 0; i < n; i++){
        fib = fib1 + fib2;
        fib1 = fib2;
        fib2 = fib;
    }
    return fib;
}
"""
