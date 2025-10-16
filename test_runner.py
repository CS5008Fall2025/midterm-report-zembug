import subprocess
import sys
import csv
import argparse

# Default executable and settings
EXEC = "./fibonacci"  # or "python3 fibonacci_methods.py"
TIMEOUT = 60
OUT_DEFAULT = "fibonacci_run.csv"
OUT_FILE_TIME = "timings_"
OUT_FILE_OPS = "ops_"
CSV_HEADER = "N,Iterative,Dynamic Programming,Recursive"

class RecursionTimeoutError(Exception):
    pass

def run_single(n: int, typ: int) -> dict:
    """Run a single Fibonacci method and collect timing and ops"""
    try:
        # Python script doesn't use 'typ', so skip it
        if "python" in EXEC:
            command = f"{EXEC} {n}"
        else:
            command = f"{EXEC} {n} {typ}"

        results = subprocess.run(
            command.split(), timeout=TIMEOUT, capture_output=True, text=True
        )
    except subprocess.TimeoutExpired:
        raise RecursionTimeoutError(f"Timeout of {TIMEOUT} seconds reached for n={n}, type={typ}")

    if results.returncode != 0:
        raise Exception(f"Error running n={n}, type={typ}: {results.stderr}")

    timings = []
    operations = []

    if "python" in EXEC:
        # Parse Python output
        lines = results.stdout.strip().splitlines()
        for i, line in enumerate(lines):
            if line.startswith("Time:"):
                time_val = line.split(":")[1].split(",")[0].strip()
                ops_val = line.split("Ops:")[1].strip()
                timings.append(time_val)
                operations.append(ops_val)
    else:
        # Parse C output
        results_line = results.stdout.strip().split(",")
        for i in range(0, len(results_line), 2):
            timings.append(results_line[i])
            operations.append(results_line[i + 1])

    return {"timings": timings, "operations": operations}

def save_to_csv(values: list, out_file: str, step: int):
    with open(out_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(CSV_HEADER.split(","))
        for i, row in enumerate(values):
            row = [i * step + 1] + row
            # Pad row to ensure 4 columns
            while len(row) < 4:
                row.append("-")
            writer.writerow(row)


def main(n, step=1, out_file=OUT_DEFAULT):
    run_type = 4  # type 4 = run all methods
    results = {"timings": [], "operations": []}

    # Determine mode: C or Python
    mode = "python" if "python" in EXEC else "c"
    time_file = OUT_FILE_TIME + f"{mode}_{out_file}"
    ops_file = OUT_FILE_OPS + f"{mode}_{out_file}"

    for i in range(1, n + 1, step):
        try:
            result = run_single(i, run_type)
            results["timings"].append(result["timings"])
            results["operations"].append(result["operations"])
        except RecursionTimeoutError:
            run_type = 4  # fallback: skip recursive
            result = run_single(i, run_type)
            results["timings"].append(result["timings"] + ["-"])
            results["operations"].append(result["operations"] + ["-"])
        except Exception as e:
            print(e, file=sys.stderr)
            break

    save_to_csv(results["operations"], ops_file, step)
    save_to_csv(results["timings"], time_file, step)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Fibonacci benchmarking")
    parser.add_argument("n", type=int, help="Max value of n to test")
    parser.add_argument("--step", type=int, default=1, help="Step size")
    parser.add_argument("--out", type=str, default=OUT_DEFAULT, help="Output file base name")
    parser.add_argument("--timeout", type=int, default=TIMEOUT, help="Timeout per run")
    parser.add_argument("--exec", type=str, default=EXEC, help="Executable to run")
    args = parser.parse_args()

    TIMEOUT = args.timeout
    EXEC = args.exec
    main(args.n, args.step, args.out)
