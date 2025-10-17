from fibonacci import fib_iterative, fib_dynamic, fib_recursive

def test_fibonacci_methods():
    test_values = [0, 1, 2, 5, 10, 20, 30]
    print("Running tests for Fibonacci methods...\n")
    
    # Test each method and compare results
    for n in test_values:
        iter_result, _ = fib_iterative(n)
        dyn_result, _ = fib_dynamic(n)
        rec_result = fib_recursive(n, [0]) if n <= 30 else iter_result  # Skip slow recursion

        print(f"n = {n}")
        print(f"  Iterative: {iter_result}")
        print(f"  Dynamic:   {dyn_result}")
        if n <= 30:
            print(f"  Recursive: {rec_result}")
        else:
            print("  Recursive: Skipped (n > 30)")

        if iter_result == dyn_result == rec_result:
            print("  ✅ All methods match\n")
        else:
            print("  ❌ Mismatch detected!\n")

if __name__ == "__main__":
    test_fibonacci_methods()
