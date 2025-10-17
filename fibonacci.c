# include <stdio.h>
# include <stdlib.h>
# include <time.h>
# include <inttypes.h>
#include <stdint.h>
typedef uint64_t ull;

void help() {
    printf("Usage: ./fibonacci N TYPE\n");
    printf("TYPE: 1 = iterative, 2 = recursive, 3 = dynamic programming, 4 = all methods\n");
    printf("Example: ./fibonacci 25 4\n");
}



// Recursive Fibonacci function with operation counting
ull fib_recursive(int n, ull* ops) {
    (*ops)++; // count each function call
    if (n == 0 || n == 1) 
        return n;
    return fib_recursive(n - 1, ops) + fib_recursive(n - 2, ops); 
}

// Iterative Fibonacci function with operation counting
ull fib_iterative(int n, ull* ops) {
    *ops = 0; // Reset operation counter
    if (n == 0) return 0;
    if (n == 1) return 1;

    ull prev = 0;
    ull curr = 1;
    ull next;

    for (int i = 2; i <= n; i++) {
        next = prev + curr;
        prev = curr;
        curr = next;
        (*ops)++; // count each addition
    }
    return curr; // Return the nth Fibonacci number
}

// Dynamic Programming Fibonacci function with operation counting
ull fib_dynamic(int n, ull* ops) {
    *ops = 0; // Reset operation counter
    if (n == 0) return 0;
    if (n == 1) return 1;

    ull* arr = (ull*)malloc((n + 1) * sizeof(ull));
    arr[0] = 0;
    arr[1] = 1;

    for (int i = 2; i <= n; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
        (*ops)++; // count each addition
    }

    ull result = arr[n];
    free(arr); // Free allocated memory
    return result; // Return the nth Fibonacci number
}


int main(int argc, char* argv[]) {
    if (argc < 3) {
        printf("At least two arguments needed!\n");
        help();
        return 1;
    }

    int n = atoi(argv[1]);
    int type = atoi(argv[2]);

    if (n < 0) {
        printf("n must be a non-negative integer.\n");
        return 1;
    }

    ull ops = 0;
    clock_t start, end;
    double runtime;
    ull result;

    switch (type) {
        case 1: // Iterative
            start = clock();
            result = fib_iterative(n, &ops);
            end = clock();
            runtime = (double)(end - start) / CLOCKS_PER_SEC;
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

        case 4: {
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

                printf("%.6f,%" PRIu64 ",%.6f,%" PRIu64 ",%.6f,%" PRIu64 "\n",
                    runtime_iter, ops_iter,
                    runtime_dp, ops_dp,
                    runtime_rec, ops_rec);
            } else {
                printf("%.6f,%" PRIu64 ",%.6f,%" PRIu64 ",-,-\n",
                   runtime_iter, ops_iter,
                   runtime_dp, ops_dp);
                }
            break;
        }

        default:
            printf("Type not supported.\n");
            help();
            return 1;

    }

}

