import time
import random
import pandas as pd
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
    plt.plot(input_sizes, runtimes, marker='o', linestyle='-', label=algorithm_name)
    plt.title('Sorting Algorithm Runtimes')
    plt.xlabel('Input Size')
    plt.ylabel('Runtime (s)')
    plt.grid(True)
    plt.legend()

def create_comparison_table(input_sizes, insertion_runtimes, selection_runtimes, bubble_runtimes):
    comparison_dict = {
        'Input Size': input_sizes,
        'Insertion Sort Runtime (s)': insertion_runtimes,
        'Selection Sort Runtime (s)': selection_runtimes,
        'Bubble Sort Runtime (s)': bubble_runtimes
    }
    return comparison_dict

if __name__ == "__main__":
    input_sizes, insertion_runtimes = benchmark_sorting_algorithm_with_various_input_sizes(insertion_sort)
    _, selection_runtimes = benchmark_sorting_algorithm_with_various_input_sizes(selection_sort)
    _, bubble_runtimes = benchmark_sorting_algorithm_with_various_input_sizes(bubble_sort)

    plot_benchmarks(input_sizes, insertion_runtimes, 'Insertion Sort')
    plot_benchmarks(input_sizes, selection_runtimes, 'Selection Sort')
    plot_benchmarks(input_sizes, bubble_runtimes, 'Bubble Sort')

    plt.show()

    comparison_table = create_comparison_table(input_sizes, insertion_runtimes, selection_runtimes, bubble_runtimes)
    print("Comparison Table:")
    print(pd.DataFrame(comparison_table))
