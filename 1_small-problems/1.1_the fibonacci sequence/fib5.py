"Keep it simple, Fibonacci"

'''
There is an even more performant option. We can solve Fibonacci with an old-fashioned
iterative approach.
'''

def fib5(n: int) -> int:
    if n == 0: return n                 # special case
    last: int = 0                       # initially set to fib(0)
    next: int = 1                       # initially set to fib(1)
    for _ in range(1, n):               # loop n times
        last, next = next, last + next  # swap last and next
    return next


if __name__ == '__main__':
    print(fib5(10))
    print(fib5(20))


""""
With this approach, the body of the for loop will run a maximum of n - 1 times. In
other words, this is the most efficient version yet. Compare 19 runs of the for loop
body to 21,891 recursive calls of fib2() for the 20th Fibonacci number. That could
make a serious difference in a real-world application!
"""


'''
make a serious difference in a real-world application!
In the recursive solutions, we worked backward. In this iterative solution, we work
forward. Sometimes recursion is the most intuitive way to solve a problem. For example,
the meat of fib1() and fib2() is pretty much a mechanical translation of the
original Fibonacci formula. However, naive recursive solutions can also come with significant
performance costs. Remember, any problem that can be solved recursively
can also be solved iteratively.
'''
