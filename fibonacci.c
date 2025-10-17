# include <stdio.h>
# include <stdlib.h>
# include <time.h>
# include <inttypes.h>
#include <stdint.h>
typedef uint64_t ull;

void help() { // print usage instructions
    printf("Usage: ./fibonacci N TYPE\n");
    printf("TYPE: 1 = iterative, 2 = recursive, 3 = dynamic programming, 4 = all methods\n");
    printf("Example: ./fibonacci 25 4\n");
}

/**
 * Computes the nth Fibonacci number using a recursive approach.
 * Tracks the number of recursive calls as operations.
 * @param n    The index of the Fibonacci number to compute (n ≥ 0)
 * @param ops  Pointer to an operation counter (will be updated during recursion)
 * @return     The nth Fibonacci number
 */
ull fib_recursive(int n, ull* ops) {
    (*ops)++; // count each function call
    if (n == 0 || n == 1)  // base cases
        return n;
    return fib_recursive(n - 1, ops) + fib_recursive(n - 2, ops); // recursive case
}

/**
 * Computes the nth Fibonacci number using an iterative approach.
 * Tracks the number of addition operations performed.
 * @param n    The index of the Fibonacci number to compute (n ≥ 0)
 * @param ops  Pointer to an operation counter (will be updated during execution)
 * @return     The nth Fibonacci number
 */
ull fib_iterative(int n, ull* ops) {
    *ops = 0; // reset operation counter
    if (n == 0) return 0; // base case
    if (n == 1) return 1; // base case

    ull prev = 0; // stores F(n-2)
    ull curr = 1; // stores F(n-1)
    ull next; // will store F(n) in each iteration

    for (int i = 2; i <= n; i++) { // loop to compute F(2) thru F(n)
        next = prev + curr; // calculate next Fibonacci number: F(n) = F(n-1) + F(n-2)
        prev = curr; // shift previous values: F(n-2) becomes F(n-1)
        curr = next; // Update current value: F(n-1) becomes F(n)
        (*ops)++; // count each addition as one operation
    }
    return curr; // return the nth Fibonacci number
}

/**
 * Computes the nth Fibonacci number using bottom-up dynamic programming.
 * Stores intermediate results in a heap-allocated array and counts additions.
 * @param n    The index of the Fibonacci number to compute (n ≥ 0)
 * @param ops  Pointer to an operation counter (will be updated during execution)
 * @return     The nth Fibonacci number
 */
ull fib_dynamic(int n, ull* ops) {
    *ops = 0; // Reset operation counter
    if (n == 0) return 0; // base case
    if (n == 1) return 1; // base case

    ull* arr = (ull*)malloc((n + 1) * sizeof(ull)); // allocate space for Fibonacci values
    arr[0] = 0; // initialize base case F(0)
    arr[1] = 1; // initialize base case F(1)

    for (int i = 2; i <= n; i++) { // fill the array with Fibonacci values up to F(n)
        arr[i] = arr[i - 1] + arr[i - 2]; // F(n) = F(n-1) + F(n-2)
        (*ops)++; // count each addition
    }

    ull result = arr[n]; // store the result before freeing memory
    free(arr); // free allocated memory
    return result; // return the nth Fibonacci number
}


int main(int argc, char* argv[]) { 
    if (argc < 3) { // check for enough arguments
        printf("At least two arguments needed!\n");
        help(); // show usage instructions
        return 1; // exit if not enough arguments
    }

    // parse input arguments, convert to integers
    int n = atoi(argv[1]); 
    int type = atoi(argv[2]); 

    if (n < 0) { // check for negative input
        printf("n must be a non-negative integer.\n");
        return 1; // exit if n is negative
    }

    // declare variables for operation count, timing, result
    ull ops = 0;
    clock_t start, end;
    double runtime;
    ull result;

    switch (type) {
        case 1: // Iterative
            start = clock(); // start timing
            result = fib_iterative(n, &ops); // run Fibonacci iteratively
            end = clock(); // end timing
            runtime = (double)(end - start) / CLOCKS_PER_SEC; // calculate runtime
            printf("Iterative Fibonacci(%d) = %" PRIu64 "\n", n, result);
            printf("Time: %.6f, Ops: %" PRIu64 "\n", runtime, ops);
            break;

        case 2: // Recursive
            start = clock();
            result = fib_recursive(n, &ops);
            end = clock();
            runtime = (double)(end - start) / CLOCKS_PER_SEC;
            printf("Recursive Fibonacci(%d) = %" PRIu64 "\n", n, result);
            printf("Time: %.6f, Ops: %" PRIu64 "\n", runtime, ops);
            break;

        case 3: // Dynamic Programming
            start = clock();
            result = fib_dynamic(n, &ops);
            end = clock();
            runtime = (double)(end - start) / CLOCKS_PER_SEC;
            printf("Dynamic Programming Fibonacci(%d) = %" PRIu64 "\n", n, result);
            printf("Time: %.6f, Ops: %" PRIu64 "\n", runtime, ops);
            break;

        case 4: { // run all methods and print CSV-style output
            uint64_t ops_iter = 0, ops_dp = 0, ops_rec = 0;
            double runtime_iter, runtime_dp, runtime_rec;
            ull result;

            // Iterative
            clock_t start = clock();
            result = fib_iterative(n, &ops_iter);
            clock_t end = clock();
            runtime_iter = (double)(end - start) / CLOCKS_PER_SEC;

            // Dynamic Programming
            start = clock();
            result = fib_dynamic(n, &ops_dp);
            end = clock();
            runtime_dp = (double)(end - start) / CLOCKS_PER_SEC;

            // Recursive (only if n <= 40)
            if (n <= 40) {
                start = clock();
                result = fib_recursive(n, &ops_rec);
                end = clock();
                runtime_rec = (double)(end - start) / CLOCKS_PER_SEC;

                // print all results in CSV format, time and ops for each method
                printf("%.6f,%" PRIu64 ",%.6f,%" PRIu64 ",%.6f,%" PRIu64 "\n",
                    runtime_iter, ops_iter,
                    runtime_dp, ops_dp,
                    runtime_rec, ops_rec);
            } else {
                // skip recursive for large n, print placeholders
                printf("%.6f,%" PRIu64 ",%.6f,%" PRIu64 ",-,-\n",
                   runtime_iter, ops_iter,
                   runtime_dp, ops_dp);
                }
            break;
        }

        default: // invalid type
            printf("Type not supported.\n");
            help(); // show usage instructions
            return 1;

    }

}

