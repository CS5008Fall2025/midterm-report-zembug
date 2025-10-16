import time

# Iterative Fibonacci with operation counting
def fib_iterative(n):
    ops = 0
    if n == 0:
        return 0, ops
    if n == 1:
        return 1, ops

    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
        ops += 1
    return curr, ops

# Recursive Fibonacci with operation counting
def fib_recursive(n, ops_counter):
    ops_counter[0] += 1
    if n == 0 or n == 1:
        return n
    return fib_recursive(n - 1, ops_counter) + fib_recursive(n - 2, ops_counter)

# Dynamic Programming Fibonacci with operation counting
def fib_dynamic(n):
    ops = 0
    if n == 0:
        return 0, ops
    if n == 1:
        return 1, ops

    arr = [0] * (n + 1)
    arr[0], arr[1] = 0, 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]
        ops += 1
    return arr[n], ops

# Time and count wrapper
def run_and_time(label, func, n):
    start = time.process_time()
    if label == "recursive":
        ops_counter = [0]
        result = func(n, ops_counter)
        ops = ops_counter[0]
    else:
        result, ops = func(n)
    end = time.process_time()
    runtime = end - start
    print(f"{label.capitalize()} Fibonacci({n}) = {result}")
    print(f"Time: {runtime:.6f}, Ops: {ops}\n")

# Main runner
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python3 fibonacci_methods.py N")
        sys.exit(1)

    n = int(sys.argv[1])
    print(f"Running Fibonacci methods for n = {n}\n")

    run_and_time("iterative", fib_iterative, n)
    run_and_time("dynamic", fib_dynamic, n)

    if n <= 30:
        run_and_time("recursive", fib_recursive, n)
    else:
        print("Recursive method skipped for n > 30 due to performance.\n")

        