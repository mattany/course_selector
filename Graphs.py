"""
Graphs.py
--------------
In this file the graphs are created.
It first creates the text file and then convers it to excel file.
Then, insert the data to Pandas DataFrame.
And then we use the library matplotlib.pyplot to create beautiful graphs.

Written by:
"""

from Main import NUM_OF_STRATEGIES, DATA_EXCEL_FILE
import matplotlib.pyplot as plt
import pandas as pd

num_of_strategies = NUM_OF_STRATEGIES
data_frame = pd.read_csv(DATA_EXCEL_FILE)
columns = data_frame.columns


def single_strategy_compare_to_itself(strategy_number):
    """
    This method plots graph which compares single strategy to itself
    such that:
    X - number of students
    Y - satisfaction rate

    :param strategy_number: as defined in Strategy.py.
    :return: plots the graph.
    """
    #TODO

    return 0


def two_strategies_comparing(first_strategy, second_strategy):
    """
    This method plots graph which compares two strategies.
    such that:
    X - number of students
    Y - satisfaction rate

    :return: plots the graph.
    """
    # TODO

    return 0


def all_strategies_comparing():
    """
    This method plots graph which compares all strategies.
    such that:
    X - number of students
    Y - satisfaction rate

    :return: plots the graph.
    """
    # TODO

    return 0








