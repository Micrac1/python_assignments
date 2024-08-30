def fizz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 3 == 0:
            print('Fizz')
        else:
            print(i)

def buzz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def fizzbuzz(n: int) -> None:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizz(7)
buzz(10)
fizzbuzz(18)
