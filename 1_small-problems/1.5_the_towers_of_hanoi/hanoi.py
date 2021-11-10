from typing import TypeVar, Generic, List
T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    def push(self, item: T) -> None:
        self._container.append(item)
    def pop(self) -> T:
        return self._container.pop()
    def __repr__(self) -> str:
        return repr(self._container)


''''
NOTE As was described in the introduction, this book utilizes type hints
throughout. The import of Generic from the typing module enables Stack to
be generic over a particular type in type hints. The arbitrary type T is defined
in T = TypeVar('T'). T can be any type. When a type hint is later used for a
Stack to solve the Hanoi problem, it is type-hinted as type Stack[int], which
means T is filled in with type int. In other words, the stack is a stack of integers.
'''


"""
Stacks are perfect stand-ins for the towers in The Towers of Hanoi. When we want to
put a disc onto a tower, we can just push it. When we want to move a disc from one
tower to another, we can pop it from the first and push it onto the second.
"""


num_disks: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_disks + 1):
    tower_a.push(i)


'''
We will codify it as a function called hanoi() that is responsible
for moving discs from one tower to another, given a third temporary tower.
'''
def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_disks)
    print(tower_a)
    print(tower_b)
    print(tower_c)
