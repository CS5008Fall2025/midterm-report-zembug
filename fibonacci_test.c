#include <stdio.h>
#include <stdint.h>
#include <inttypes.h>
#include "fibonacci.c"

int main() {
    int test_values[] = {0, 1, 5, 10, 20, 30, 40};
    int num_tests = sizeof(test_values) / sizeof(test_values[0]);

    printf("Testing Fibonacci methods:\n\n");

    for (int i = 0; i < num_tests; i++) {
        int n = test_values[i];
        uint64_t ops = 0;

        printf("n = %d\n", n);

        // Iterative
        ops = 0;
        uint64_t iter_result = fib_iterative(n, &ops);
        printf("  Iterative: %" PRIu64 " (Ops: %" PRIu64 ")\n", iter_result, ops);

        // Dynamic Programming
        ops = 0;
        uint64_t dp_result = fib_dynamic(n, &ops);
        printf("  Dynamic:   %" PRIu64 " (Ops: %" PRIu64 ")\n", dp_result, ops);

        // Recursive (only for small n)
        if (n <= 30) {
            ops = 0;
            uint64_t rec_result = fib_recursive(n, &ops);
            printf("  Recursive: %" PRIu64 " (Ops: %" PRIu64 ")\n", rec_result, ops);
        } else {
            printf("  Recursive: Skipped (n > 30)\n");
        }

        printf("\n");
    }

    return 0;
}
