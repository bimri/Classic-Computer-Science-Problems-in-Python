"Utilizing base cases"

''''
In the case of the Fibonacci function, we have natural base cases in the form of the
special first two sequence values, 0 and 1. Neither 0 nor 1 is the sum of the previous
two numbers in the sequence. Instead, they are the special first two values. Let’s try
specifying them as base cases.
'''

def fib2(n: int) -> int:
    if n < 2:                               # base case
        return n
    return fib2(n-1) + fib2(n-2)            # recursive case


"""
NOTE The fib2() version of the Fibonacci function returns 0 as the zeroth
number (fib2(0)), rather than the first number, as in our original proposition.
In a programming context, this kind of makes sense because we are used
to sequences starting with a zeroth element.
"""

if __name__ == "__main__":
    print(fib2(5))
    print(fib2(10))
 