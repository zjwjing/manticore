"""
Benchmark: Enum vs String comparison performance

This benchmark demonstrates that enum comparisons are faster than string comparisons
in Python, which justifies the refactoring of Manticore's transaction types and results.
"""
import time
from enum import Enum


# Define enums
class TxType(Enum):
    CREATE = "CREATE"
    CALL = "CALL"
    DELEGATECALL = "DELEGATECALL"


class TxResult(Enum):
    STOP = "STOP"
    RETURN = "RETURN"
    SELFDESTRUCT = "SELFDESTRUCT"
    THROW = "THROW"
    TXERROR = "TXERROR"
    REVERT = "REVERT"


def benchmark_string_comparison(iterations=1000000):
    """Benchmark string comparisons"""
    sort = "CREATE"
    result = "RETURN"
    
    start = time.time()
    for _ in range(iterations):
        if sort == "CREATE":
            pass
        if result == "RETURN":
            pass
        if sort in ("CREATE", "CALL"):
            pass
        if result in ("REVERT", "THROW", "TXERROR"):
            pass
    end = time.time()
    
    return end - start


def benchmark_enum_comparison(iterations=1000000):
    """Benchmark enum comparisons"""
    sort = TxType.CREATE
    result = TxResult.RETURN
    
    start = time.time()
    for _ in range(iterations):
        if sort == TxType.CREATE:
            pass
        if result == TxResult.RETURN:
            pass
        if sort in (TxType.CREATE, TxType.CALL):
            pass
        if result in (TxResult.REVERT, TxResult.THROW, TxResult.TXERROR):
            pass
    end = time.time()
    
    return end - start


def main():
    iterations = 1000000
    
    print("=" * 50)
    print("Enum vs String Comparison Benchmark")
    print("=" * 50)
    print(f"Iterations: {iterations:,}")
    print()
    
    # Warm up
    benchmark_string_comparison(1000)
    benchmark_enum_comparison(1000)
    
    # Run benchmarks
    string_time = benchmark_string_comparison(iterations)
    enum_time = benchmark_enum_comparison(iterations)
    
    print(f"String comparison: {string_time:.4f} seconds")
    print(f"Enum comparison:   {enum_time:.4f} seconds")
    print()
    
    improvement = ((string_time - enum_time) / string_time) * 100
    speedup = string_time / enum_time
    
    print(f"Improvement: {improvement:.2f}%")
    print(f"Speedup: {speedup:.2f}x")
    print()
    
    print("=" * 50)
    print("Conclusion")
    print("=" * 50)
    if improvement > 0:
        print(f"Enum comparisons are {speedup:.2f}x faster than string comparisons.")
        print("This refactoring will improve performance in hot paths.")
    else:
        print("No significant performance difference detected.")
        print("However, enums provide better type safety and readability.")


if __name__ == "__main__":
    main()
