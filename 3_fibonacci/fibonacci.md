# Fibonacci

"In mathematics, the Fibonacci sequence is a sequence in which each number is
the sum of the two preceding ones. Numbers that are part of the Fibonacci
sequence are known as Fibonacci numbers. The sequence
commonly starts from 0 and 1." [[wikipedia]](https://en.wikipedia.org/wiki/Fibonacci_sequence).

```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ....
```

The Fibonacci numbers may be defined by the recurrence relation:

```
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2)
```
where `F(k)` is `k`th number in the fibonacci sequence and `n > 1`.

## 1. The naive one

Write a program that calculates the `n`th number of the Fibonacci sequence.
You can get `n` from `stdin` or as an argument.
The program must return the correct result for `0 <= n <= 35`.
The program should take less than 10 seconds to return a result for `n <= 35`.

* Desired output for `n = 0`:
  ```
  0
  ```

* Desired output for `n = 1`:
  ```
  1
  ```

* Desired output for `n = 20`:
  ```
  6765
  ```

## 2. Iterate on the design

Optimize the previous program to take less than 1 second for `n <= 20000`.
The program must return the correct result for `0 <= n <= 20000`.

* Desired output for `n = 0`:
  ```
  0
  ```

* Desired output for `n = 1`:
  ```
  1
  ```

* Desired output for `n = 20`:
  ```
  6765
  ```

* Desired output for `n = 100`:
  ```
  354224848179261915075
  ```
