"""
Example file solving the pascal triangle using python.
Author: Albert Lionelle
Semester: Spring 2023
"""
from enum import Enum
from functools import lru_cache
import argparse
from typing import Callable
import sys
import time

STACK_LIMIT = 1000
sys.setrecursionlimit(100000)

OPS = 0


class PascalType(Enum):
    ITERATIVE_DP_TOGETHER = 4
    ALL = 3
    DP = 2
    RECURSIVE = 1
    ITERATIVE = 0


@lru_cache(maxsize=None)
def pascal_dp(n: int, i: int) -> int:
    """
    Solves the pascal triangle using simple recursion and built
    in memoization
    Args:
        n: the nth row
        i: the item in the row

    Returns:
        the addition of n-1, i + n-1, i-1
    """
    if n == i or i == 0:
        return 1
    global OPS
    OPS += 1
    return pascal_dp(n - 1, i) + pascal_dp(n - 1, i - 1)


def pascal_r(n: int, i: int) -> int:
    """
    Solves the pascal triangle using simple recursion
    Args:
        n (int): the nth row
        i (int): the item in the row

    Returns:
        the addition of n-1, i + n-1, i-1
    """
    if n == i or i == 0:
        return 1
    global OPS
    OPS += 1
    return pascal_r(n - 1, i) + pascal_r(n - 1, i - 1)


def recursive_pascal(n: int, func=pascal_r) -> list:
    """

    Args:
        func:
        n:
        print_it:

    Returns:

    """
    result = []
    #    if n > STACK_LIMIT:  # due to stack limit size, tabulate data first
    #        steps = n // STACK_LIMIT
    #        for step in range(1, steps):
    #            new_n = step * STACK_LIMIT
    #            for i in range(0, new_n + 1):
    #                func(new_n, i)
    n = n
    for i in range(0, n + 1):
        result.append(func(n, i))
    return result


def iterative_pascal(n: int) -> list:
    """
    Generates the nth row in the pascal triangle based on the
    method requested

    Args:
        n: the row to generate
        print_it:  print out all rows as being generated
        version:  the type/method of generation

    Returns:
        the nth row of the pascal triangle
    """
    global OPS
    arr = []
    for i in range(0, n):
        arr.append([])
        for j in range(0, i + 1):
            OPS += 1
            if i == j or j == 0:
                arr[i].append(1)
            else:
                arr[i].append(arr[i - 1][j - 1] + arr[i - 1][j])
    return arr[n - 1]


def pascal_dp_full(n: int) -> list:
    """
    Solves the pascal triangle using simple recursion and built
    in memoization
    Args:
        n: the nth row

    Returns:
        the nth row of the pascal triangle
    """
    return recursive_pascal(n, func=pascal_dp)


def pascal_r_full(n: int) -> list:
    """
    Solves the pascal triangle using simple recursion
    Args:
        n (int): the nth row

    Returns:
        the nth row of the pascal triangle
    """
    return recursive_pascal(n, func=pascal_r)


def run_and_time(func: Callable, n: int, print_it: bool = False):
    """
    Runs the pascal triangle generation, prints the row if requested
    and returns both the time and OPS used.

    Args:
        n (int): _description_
        algo (PascalType): _description_
        print (bool): _description_
    """
    global OPS
    OPS = 0  # reset it
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    if print_it:
        print(result)
    return end - start, OPS


def main(n: int, algo: PascalType, print_it: bool):
    """
    Prints the string the Nth row/ generates the nth row of the pascal triangle.

    Args:
        algo:
        print_type:
        n: the nth row to generate
    """
    if algo == PascalType.RECURSIVE:
        print("Recursive Version")
        time, ops = run_and_time(pascal_r_full, n, print_it)
        print(f"Time: {time}({ops})")
    elif algo == PascalType.DP:
        print("Dynamic Programming Version")
        time, ops = run_and_time(pascal_dp_full, n, print_it)
        print(f"Time: {time}({ops})")
    elif algo == PascalType.ITERATIVE_DP_TOGETHER:
        time, ops = run_and_time(iterative_pascal, n)
        time2, ops2 = run_and_time(pascal_dp_full, n)
        print(f"{time:0.6f},{ops},{time2:0.6f},{ops2},-,-")
    elif algo == PascalType.ALL:
        time, ops = run_and_time(iterative_pascal, n)
        time2, ops2 = run_and_time(pascal_dp_full, n)
        time3, ops3 = run_and_time(pascal_r_full, n)
        print(f"{time:0.6f},{ops},{time2:0.6f},{ops2},{time3:0.6f},{ops3}")
    else:
        print("Iterative Version")
        time, ops = run_and_time(iterative_pascal, n, print_it)
        print(f"Time: {time}({ops})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pascal Triangle")
    parser.add_argument("n", type=int, help="The nth row to generate")
    parser.add_argument(
        "--print", action="store_true", default=False, help="Print the nth row"
    )
    parser.add_argument(
        "algo",
        type=int,
        choices=[0, 1, 2, 3, 4],
        default=PascalType.ITERATIVE.value,
        help="The type of algorithm to use: 0 = iterative, 1 = recursive, 2 = dp, 3 = all, 4 = iterative and dp together",
    )

    args = parser.parse_args()
    algo = PascalType(args.algo)
    main(args.n, algo, args.print)
