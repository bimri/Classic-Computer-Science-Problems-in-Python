"A first recursive attempt"

def fib1(n: int) -> int:
    """
    Return the nth Fibonacci number.
    """
    return fib1(n - 1) + fib1(n - 2)  


"""
The Fibonacci sequence is a sequence of numbers such that any number, except
for the first and second, is the sum of the previous two:
0, 1, 1, 2, 3, 5, 8, 13, 21...

The value of the first Fibonacci number in the sequence is 0. The value of the
fourth Fibonacci number is 2. It follows that to get the value of any Fibonacci number,
n, in the sequence, one can use the formula
fib(n) = fib(n - 1) + fib(n - 2)
"""

# if __name__ == "__main__":
    # print(fib1(5))                    # RecursionError: maximum recursion depth exceeded
 