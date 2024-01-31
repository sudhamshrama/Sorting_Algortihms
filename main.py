import time
import random
import matplotlib.pyplot as plt

from insertion_sort import insertion_sort
from selection_sort import selection_sort
from bubble_sort import bubble_sort

def benchmark_sorting_algorithm(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr)
    end_time = time.time()
    return end_time - start_time

def benchmark_sorting_algorithm_with_various_input_sizes(sort_func):
    input_sizes = [5, 10, 20, 50, 100, 200, 500, 1000]  # Add more as needed
    runtimes = []

    for size in input_sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        runtime = benchmark_sorting_algorithm(sort_func, arr)
        runtimes.append(runtime)
    
    return input_sizes, runtimes

def plot_benchmarks(input_sizes, runtimes, algorithm_name):
    plt.plot(input_sizes, runtimes, marker='o', linestyle='-')
    plt.title(f'{algorithm_name} Sorting Algorithm Runtime')
    plt.xlabel('Input Size')
    plt.ylabel('Runtime (s)')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    algorithms = {
        'Insertion Sort': insertion_sort,
        'Selection Sort': selection_sort,
        'Bubble Sort': bubble_sort
    }

    for algo_name, algo_func in algorithms.items():
        input_sizes, runtimes = benchmark_sorting_algorithm_with_various_input_sizes(algo_func)
        plot_benchmarks(input_sizes, runtimes, algo_name)
