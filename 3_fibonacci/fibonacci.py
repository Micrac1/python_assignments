n = 20000

fibonacci = [0, 1]
for i in range(1, n):
    fibonacci.append(fibonacci[i] + fibonacci[i-1])
print(fibonacci[n]) 

fib1 = 0
fib2 = 1
for i in range (1, n):
        fib = fib1 + fib2
        fib1 = fib2
        fib2 = fib

print(fib) 