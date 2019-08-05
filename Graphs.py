"""
Graphs.py
--------------
In this file the graphs are created.
It first creates the text file and then convers it to excel file.
Then, insert the data to Pandas DataFrame.
And then we use the library matplotlib.pyplot to create beautiful graphs.

Written by: Linoy Palas (July 30th).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from Strategy import Strategy, strategy_factory

import pandas as pd
import numpy as np

columns_names = ["Num of students - Const", "Num of students - SquaredPow", "Num of students - Exp",
                 "Num of students - Linear",
                 "Num of students - Random", "Avg Rate of students - Const", "Avg Rate of students - SquaredPow",
                 "Avg Rate of students - Exp", "Avg Rate of students - Linear", "Avg Rate of students - Random",
                 "Median(all students)", "Average(all students)"]

strategy = ["Const", "SquaredPow", "Exp", "Linear", "Random"]

num_of_strategies = 5

data_frame_L1 = pd.read_csv("rare_data_L1.txt", names=columns_names)
data_frame_BORDA = pd.read_csv("rare_data_borda.txt", names=columns_names)


def all_strategies_comparing():
    """
    This method plots graph which compares all strategies.
    such that:
    X - number of students
    Y - satisfaction rate

    :return: plots the graph.
    """
    # iterate over rows with iterrows()
    counter = 0
    list_of_rate_per_row = []
    list_of_num = [0, 0, 0, 0, 0]  # exp, const, random, linear, squaredpow
    for index, row in data_frame_BORDA.iterrows():
        counter += 1
        # access data using column names
        rows_of_Avg = [row['Avg Rate of students - Exp'], row['Avg Rate of students - Const'],
                       row['Avg Rate of students - Random'], row['Avg Rate of students - Linear'],
                       row['Avg Rate of students - SquaredPow']]
        list_of_rate_per_row.append(rows_of_Avg)
        a = rows_of_Avg.index(max(rows_of_Avg))  # update the list of num
        list_of_num[a] += 1

    avr = [sum(i) for i in zip(*list_of_rate_per_row)]  # sum all the Avg rate per function

    new_list = [0, 0, 0, 0, 0]
    for i in range(len(avr)):
        new_list[i] = avr[i] / counter


def one_compare_to_all(data_frame, statergy_for_all):
    x = data_frame.loc[data_frame['Num of students - ' + statergy_for_all] == 99]
    z = data_frame.loc[data_frame['Num of students - ' + statergy_for_all] == 100]
    satisfaction = []

    for i in range(len(strategy)):
        if strategy[i] != statergy_for_all:
            y = x.loc[x['Num of students - ' + strategy[i]] == 1]
            val = y["Avg Rate of students - " + strategy[i]].values[0]
            satisfaction.append(val)
        else:
            satisfaction.append(z["Avg Rate of students - " + statergy_for_all].values[0])

    return strategy, satisfaction


def one_compare_to_all_graph_draw(statergy_for_all):
    """
    This method plots graph which compares all strategies.
    such that:
    X - number of students
    Y - satisfaction rate

    :return: plots the graph.
    """
    strategy, satisfaction_rate_L1 = one_compare_to_all(data_frame_L1, statergy_for_all)
    strategy, satisfaction_rate_Borda = one_compare_to_all(data_frame_BORDA, statergy_for_all)

    y = np.arange(len(strategy))

    plt.bar(y, satisfaction_rate_L1, width=-0.27, align='edge', alpha=0.4, color="y")
    plt.bar(y, satisfaction_rate_Borda, width=0.27, align='edge', alpha=0.4, color="r")

    plt.xticks(y, strategy)
    plt.axis([-1, 5, 0, 1])

    plt.ylabel('Satisfaction Rate of one student')
    plt.xlabel('Voting method of one student')
    plt.title("Given that all the students voted " + statergy_for_all +
              ", \nwhat will be the satisfaction rate for one student in each voting method ")

    L1_patch = mpatches.Patch(alpha=0.4, color="y", label='Norm_L1')
    Borda_patch = mpatches.Patch(alpha=0.4, color="r", label='Borda Count')
    plt.legend(handles=[Borda_patch, L1_patch])
    plt.show()


def all_strategy_graph(points_to_share, num_of_courses):
    for item in Strategy:
        if item != Strategy.Random:
            vector_score_by_function = strategy_factory(item, num_of_courses, points_to_share)

            # a list that simply contains numbers from 1 to the
            # number of _courses so that we can see in the graph the ratio:
            vector_of_courses = list(range(1, num_of_courses + 1))

            # plot the graph
            plt.plot(vector_of_courses, vector_score_by_function[:num_of_courses])
            red_patch = mpatches.Patch(label=item)
            plt.legend(handles=[red_patch])

    plt.legend(strategy)
    plt.ylabel('The number of points per course')
    plt.xlabel('Courses Priorities')
    plt.title('Distributing points for each course according to priorities')
    plt.show()


def random_graph(points_to_share, num_of_courses, num_of_iter):
    array_of_random_iteration = []
    for item in Strategy:
        if item == Strategy.Random:
            for i in range(num_of_iter):
                vector_score_by_function = strategy_factory(item, num_of_courses, points_to_share)
                array_of_random_iteration.append(vector_score_by_function)

                # a list that simply contains numbers from 1 to the number
                # of _courses so that we can see in the graph the ratio:
                vector_of_courses = list(range(1, num_of_courses + 1))
                plt.scatter(vector_of_courses, vector_score_by_function[:num_of_courses])

    a = np.array(array_of_random_iteration)
    x = a.mean(axis=0)
    plt.plot(vector_of_courses, x[:num_of_courses], color='b', alpha=0.5, linewidth=2, label="Expectation graph")
    plt.legend()
    plt.ylabel('The number of points per course')
    plt.xlabel('Courses Priorities')
    plt.title("Random function - Distributing points for each course \n"
              "according to priorities")
    plt.show()


def total_rate():
    """
    This method plots graph which compares all strategies.
    such that:
    X - number of students
    Y - satisfaction rate

    :return: plots the graph.
    """
    strategy = ["Exp", "Const", "Random", "Linear", "SquaredPow"]

    satisfaction_rate_L1 = [0.676122174675254, 0.47299009521687535, 0.3862981522286899, 0.2632839615687161,
                            0.5295739158043188]
    satisfaction_rate_Borda = [0.29197772238232267, 0.37524408420913274, 0.33437755594792395, 0.26326856560948564,
                               0.438566671707302]

    y = np.arange(len(strategy))
    plt.bar(y, satisfaction_rate_L1, width=-0.27, align='edge', alpha=0.4, color="salmon")
    plt.bar(y, satisfaction_rate_Borda, width=0.27, align='edge', alpha=0.4, color="mediumaquamarine")

    plt.xticks(y, strategy)
    plt.axis([-1, 5, 0, 1])

    plt.ylabel('Average satisfaction Rate ')
    plt.xlabel('Voting method')
    plt.title("The average satisfaction rate per Voting method \n across all possible situations")
    L1_patch = mpatches.Patch(alpha=0.4, color="salmon", label='Norm_L1')
    Borda_patch = mpatches.Patch(alpha=0.4, color="mediumaquamarine", label='Borda Count')
    plt.legend(handles=[Borda_patch, L1_patch])
    plt.show()


def total_count():
    satisfaction_rate_L1 = [3779242, 552193, 21680, 36470, 208541]
    satisfaction_rate_Board = [82299, 1516096, 168078, 392043, 2439610]

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    explode = (0.05, 0.05, 0.05, 0.05, 0.05)  # only "explode" the 2nd slice (i.e. 'Hogs')
    labels = ["Exp", "Const", "Random", "Linear", "SquaredPow"]
    colors = ['#41b6c4', '#a1dab4', 'khaki', '#2c7fb8', '#253494']  # green
    patches, text = plt.pie(satisfaction_rate_L1, explode=explode, colors=colors, shadow=True, startangle=40)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.title("Number of times the strategy has led to maximum satisfaction \n (BORDA_COUNT)")
    plt.show()
