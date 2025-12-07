import time

def execute_with_timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"Execution time for {func.__name__}: {elapsed_time:.2f} s")
        return result
    return wrapper