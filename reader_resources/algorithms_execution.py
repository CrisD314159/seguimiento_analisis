"""
  This module executes the different sorting algorithms 
  for the article titles array
"""
import time
from sorting_algorithms.binary_insertion import BinaryInsertionSort
from sorting_algorithms.bitonic_sort import BitonicSort
from sorting_algorithms.bucket_sort import BucketSort
from sorting_algorithms.comb_sort import CombSort
from sorting_algorithms.gnome_sort import GnomeSort
from sorting_algorithms.heap_sort import HeapSort
from sorting_algorithms.pingeon_sort import PingeonSort
from sorting_algorithms.quick_sort import StringQuickSort
from sorting_algorithms.radix_sort import RadixSort
from sorting_algorithms.selection_sort import SelectionSort
from sorting_algorithms.tim_sort_algorithm import TimSort
from sorting_algorithms.tree_sort import TreeSort
from sorting_algorithms.bubble_sort import StringBubbleSort
from reader_resources.execution_time_plotter import ExecutionTimePlotter
from sorting_algorithms.bidirectional_bubble_sort import BidirectionalStringSort
from sorting_algorithms.shell_sort import ShellSort


class AlgorithmsExecution:
    """
    A class that executes the different sorting algorithms for the article titles array.
    """

    @staticmethod
    def run_binary(arr):
        """
        Run method for Binary Search algorithm.
        """
        try:

            arr_copy = arr[:]
            BinaryInsertionSort.sort_in_place(arr_copy)
            return "Binary"
        except RecursionError:
            print("Error executing the Binary insertion algorithm")
            return -1

    @staticmethod
    def run_bitonic(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            BitonicSort.sort(arr_copy)
            return "Bitonic"
        except RecursionError:
            print("Error on recusion Bitonic sort method")
            return -1
        except IndexError:
            print("Error executing the Bitonic Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_bucket(arr):
        """
        Run method for Bucket Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            bucket = BucketSort()
            bucket.sort(arr_copy)
            return "Bucket"
        except IndexError:
            print("Error executing the Bucket tree algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_comb(arr):
        """
        Run method for Comb Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            CombSort.comb_sort(arr_copy)
            return "Comb"
        except IndexError:
            print("Error executing the Comb Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_gnome(arr):
        """
        Run method for Gnome Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            gnome = GnomeSort()
            gnome.sort(arr_copy)
            return "Gnome"
        except IndexError:
            print("Error executing the Gnome Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_heap(arr):
        """
        Run method for Heap Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            HeapSort.heap_sort(arr_copy)
            return "Heap"
        except IndexError:
            print("Error executing the Heap Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_pingeon(arr):
        """
        Run method for Pingeon Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            PingeonSort.pigeonhole_sort(arr_copy)
            return "Pingeon"
        except IndexError:
            print("Error executing the Pingeon algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_quick(arr):
        """
        Run method for Bitonic Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            quicksort = StringQuickSort()
            quicksort.run_quick_sort(arr_copy)
            return "Quick"
        except RecursionError:
            print("Error executing the Quick Sort algorithm")
            return -1
        except IndexError:
            print("Error executing the Quick Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_radix(arr):
        """
        Run method for Radix Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            radix = RadixSort(arr=arr_copy)
            radix.sort()
            return "Radix"
        except IndexError:
            print("Error executing the Radix algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_selection(arr):
        """
        Run method for Selection Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            SelectionSort.selection_sort(arr_copy)
            return "Selection"
        except IndexError:
            print("Error executing the Selection Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_tim(arr):
        """
        Run method for Tim Sort algorithm.
        """
        try:
            arr_copy = arr[:]
            tim = TimSort()
            tim.run_tim_sort(arr_copy)
            return "Tim"
        except IndexError:
            print("Error executing the Tim algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_tree(arr):
        """
        Run method for Tree Sort algorithm.
        """
        try:

            arr_copy = arr[:]
            tree = TreeSort(arr_copy)
            tree.sort()
            return "Tree"
        except RecursionError:
            print("Error executing the Tree sort algorithm")
            return -1
        except IndexError:
            print("Error executing the Tree Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_bubble(arr):
        """
        Run method for Bubble sort
        """
        try:

            arr_copy = arr[:]
            bubble = StringBubbleSort()
            bubble.sort(arr=arr_copy)
            return "Bubble"
        except IndexError:
            print("Error executing the Tree Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_bubble_bidirectional(arr):
        """
        Run method for Bubble sort
        """
        try:

            arr_copy = arr[:]
            bubble = BidirectionalStringSort(strings=arr_copy)
            bubble.sort()
            return "Bubble Bi"
        except IndexError:
            print("Error executing the Tree Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def run_shell_sort(arr):
        """
        Run method for Bubble sort
        """
        try:

            arr_copy = arr[:]

            ShellSort.shellsort_strings(strings=arr_copy)
            return "Shell"
        except IndexError:
            print("Error executing the Tree Sort algorithm (Index out of range)")
            return -1

    @staticmethod
    def execute_algorithms(arr, plotter_name):
        """
        Execute all sorting algorithms.
        """

        # List that contains the algorithms to execute
        algorithms = [
            AlgorithmsExecution.run_binary,
            AlgorithmsExecution.run_bitonic,
            AlgorithmsExecution.run_bucket,
            AlgorithmsExecution.run_comb,
            AlgorithmsExecution.run_gnome,
            AlgorithmsExecution.run_heap,
            AlgorithmsExecution.run_pingeon,
            AlgorithmsExecution.run_quick,
            AlgorithmsExecution.run_radix,
            AlgorithmsExecution.run_selection,
            AlgorithmsExecution.run_tim,
            AlgorithmsExecution.run_bubble,
            AlgorithmsExecution.run_tree,
            AlgorithmsExecution.run_bubble_bidirectional,
            AlgorithmsExecution.run_shell_sort
        ]

        times = []  # list to store the execution times
        algorithms_names = []  # list to store the algorithms name

        for algorithm in algorithms:
            start = time.time()  # used to calculate the execution time
            name = algorithm(arr)
            end = time.time()  # used to calculate the execution time
            # Converts the execution to milisecs
            exec_time = (end - start) * 1000
            if name != -1:  # if returns a -1, that means there was an error in the execution
                print(
                    f"Algorithm {name} executed in {exec_time} ms for the variable {plotter_name}")
                algorithms_names.append(name)
                times.append(exec_time)

        plotter = ExecutionTimePlotter(
            algorithms=algorithms_names, times=times)
        plotter.plot_execution_times(plotter_name)
