"""
  This module is used to plot the execution time of the algorithms.
"""

import matplotlib.pyplot as plt


class ExecutionTimePlotter:
    """
    A class that plots the execution time of the algorithms.
    """

    def __init__(self, algorithms, times):
        self.algorithms = algorithms
        self.execution_times = times

    def plot_execution_times(self, title):
        """
        Plot the execution times of the algorithms.
        Uses the algoritms names and execution times lists
        received in the class constructor to plot bar graphs
        """
        plt.bar(self.algorithms, self.execution_times)
        plt.xlabel('Algoritmos')
        plt.ylabel('Tiempo de ejecución (ms)')
        plt.title(
            f"Tiempo de ejecución de los algoritmos para la variable: {title}")
        plt.show()
