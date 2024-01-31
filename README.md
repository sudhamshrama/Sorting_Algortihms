# Sorting Algorithms
### Arguing Selection Sort Correctness
Selection sort works by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning. It does this through multiple iterations until the entire array is sorted. The algorithm selects the smallest (or largest, depending on sorting order) element from the unsorted portion and swaps it with the element at the current position.

The correctness of selection sort can be argued through its invariant: At the start of each iteration, the elements to the left of the current position are sorted. This invariant holds true throughout the algorithm's execution. Additionally, at each step, the algorithm chooses the smallest element from the unsorted part and moves it to its correct position, thus maintaining the sortedness of the array.

## Benchmarking
For benchmarking, you can run main.py with Python and observe the plotted runtime graphs for each sorting algorithm. Adjust the input sizes and add more as needed to cover a wider range of scenarios. Make sure to have matplotlib installed to generate the plots.

### Steps to run benchmarks
* 1. Clone the repository (or download the code)
* 2. Change directory to the cloned directory
* 3. Make sure you have python and pip installed (preferably in a virtual environment)
* 4. run pip install -r requirements.txt
 
### when everything is Fine..!
Run the main.py for executing all the sortings and main2.py to compare all the three sortings.
