"Memoization to the rescue"

'''
Memoization is a technique in which you store the results of computational tasks when
they are completed so that when you need them again, you can look them up instead
of needing to compute them a second (or millionth) time.
'''

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}                 # our base cases


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)             # memoization
    return memo[n]


if __name__ == "__main__":
    print(fib3(5))
    print(fib3(50))


""""
A call to fib3(20) will result in just 39 calls of fib3() as opposed to the 21,891 of
fib2() resulting from the call fib2(20). memo is prefilled with the earlier base cases of
0 and 1, saving fib3() from the complexity of another if statement.
"""
