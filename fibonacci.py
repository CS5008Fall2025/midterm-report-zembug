import time

# Function: fib_iterative
# Description: Computes the nth Fibonacci number using iteration.
#              Tracks the number of addition operations performed.
# Parameters: n (int) - The index of the Fibonacci number to compute.
# Returns: tuple - (Fibonacci number, operation count)
def fib_iterative(n):
    ops = 0 # initialize operation counter
    if n == 0:
        return 0, ops # base case
    if n == 1:
        return 1, ops # base case

    prev, curr = 0, 1 # initialize first two Fibonacci numbers
    for _ in range(2, n + 1): # loop from 2 to n
        prev, curr = curr, prev + curr # update Fibonacci numbers
        ops += 1 # count each addition
    return curr, ops # return nth Fibonacci number and operation count


# Function: fib_recursive
# Description: Computes the nth Fibonacci number using recursion.
#              Uses a mutable list to track the number of recursive calls.
# Parameters: n (int) - The index of the Fibonacci number to compute.
#   ops_counter (list) - A single-element list used to count operations.
# Returns: int - The nth Fibonacci number
def fib_recursive(n, ops_counter):
    ops_counter[0] += 1 # count each recursive call
    if n == 0 or n == 1:
        return n # base cases
    # recursive calls for F(n-1) and F(n-2)
    return fib_recursive(n - 1, ops_counter) + fib_recursive(n - 2, ops_counter)


# Function: fib_dynamic
# Description: Computes the nth Fibonacci number using bottom-up dynamic programming.
#              Stores intermediate results in a list and counts additions.
# Parameters: n (int) - The index of the Fibonacci number to compute.
# Returns:
#   tuple - (Fibonacci number, operation count)
def fib_dynamic(n):
    ops = 0 # initialize operation counter
    if n == 0:
        return 0, ops # base case
    if n == 1:
        return 1, ops # base case

    arr = [0] * (n + 1) # create list to store Fibonacci numbers
    arr[0], arr[1] = 0, 1 # initialize base cases
    for i in range(2, n + 1): # loop from 2 to n
        arr[i] = arr[i - 1] + arr[i - 2] # compute Fibonacci number
        ops += 1 # count each addition
    return arr[n], ops # return nth Fibonacci number and operation count


# Function: run_and_time
# Description: Runs a Fibonacci function, times its execution, and prints results.
# Parameters: label (str) - Method name ("iterative", "recursive", or "dynamic")
#   func (function) - The Fibonacci function to run
#   n (int) - The index of the Fibonacci number to compute
def run_and_time(label, func, n):
    start = time.process_time() # start timing
    if label == "recursive":
        ops_counter = [0] # use list to track operations in recursion
        result = func(n, ops_counter)
        ops = ops_counter[0] # get operation count
    else:
        result, ops = func(n) # get result and operation count
    end = time.process_time() # end timing
    runtime = end - start # calculate runtime
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

        