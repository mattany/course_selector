"""
Strategy.py
--------------
This file includes the strategy each student has.
Strategy is defined by a function, then defined to distribution of
all the points student can distribute over the courses.

Written by: Linoy Palas (July 8th)
"""

import numpy as np
import enum


class Strategy(enum.Enum):
    Const = "Constant"
    Quad = "Quadratic"
    Exp = "Exp"
    Linear = "Linear"


def strategy_factory(strategy, num_of_courses, points_to_share):
    """
    This func is a factory of the strategies.
    :param strategy: a strategy type (enum).
    :param num_of_courses: the number of courses.
    :param points_to_share: the number of points to distribute between courses.
    :return: array where in the i'th coord there is the number of points for the
    i'th course in priority.
    """
    if strategy == Strategy.Const:
        return constant(num_of_courses, points_to_share)

    elif strategy == Strategy.Quad:
        return quadratic(num_of_courses, points_to_share)

    elif strategy == Strategy.Exp:
        return exp(num_of_courses, points_to_share)

    elif strategy == Strategy.Linear:
        return linear(num_of_courses, points_to_share)

    else:
        raise Exception("No such type!")


def linear(num_of_courses, points_to_share):
    vector_of_points_to_return = [0] * (num_of_courses + 1)
    vector_of_points = [0] * (num_of_courses + 1)  # this list holds the score based on position
    for i in range(1, len(vector_of_points_to_return)):  # lst is the list
        vector_of_points[i] = i
    sum_of_score = sum(vector_of_points)  # this will be the sum of all the scores will used for

    for i in range(1, len(vector_of_points_to_return)):
        # Normalization of the vector
        vector_of_points_to_return[i] = vector_of_points[i] * points_to_share / sum_of_score

    # to have it in descending order:
    vector_of_points_to_return.reverse()

    return vector_of_points_to_return


def exp(num_of_courses, points_to_share):
    vector_of_points_to_return = [0] * (num_of_courses + 1)
    vector_of_points = [0] * (num_of_courses + 1)  # this list holds the score based on position
    for i in range(1, len(vector_of_points_to_return)):  # lst is the list
        vector_of_points[i] = np.math.exp(i)

    sum_of_score = sum(vector_of_points)  # this will be the sum of all the scores will used for

    for i in range(1, len(vector_of_points_to_return)):
        vector_of_points_to_return[i] = round(vector_of_points[i] * points_to_share / sum_of_score)

    # to have it in descending order:
    vector_of_points_to_return.reverse()

    return vector_of_points_to_return


def quadratic(num_of_courses, points_to_share):
    vector_of_points_to_return = [0] * (num_of_courses + 1)
    vector_of_points = [0] * (num_of_courses + 1)  # this list holds the score based on position
    for i in range(1, len(vector_of_points_to_return)):  # lst is the list
        vector_of_points[i] = i * i
    sum_of_score = sum(vector_of_points)  # this will be the sum of all the scores will used for

    for i in range(1, len(vector_of_points_to_return)):
        vector_of_points_to_return[i] = round(vector_of_points[i] * points_to_share / sum_of_score)

    # to have it in descending order:
    vector_of_points_to_return.reverse()

    return vector_of_points_to_return


def constant(num_of_courses, points_to_share):
    vector_of_points_to_return = [0] * (num_of_courses + 1)
    vector_of_points = [0] * (num_of_courses + 1)  # this list holds the score based on position
    for i in range(1, len(vector_of_points_to_return)):  # lst is the list
        vector_of_points[i] = 1
    sum_of_score = sum(vector_of_points)  # this will be the sum of all the scores will used for

    for i in range(1, len(vector_of_points_to_return)):
        vector_of_points_to_return[i] = round(vector_of_points[i] * points_to_share / sum_of_score)

    # to have it in descending order:
    vector_of_points_to_return.reverse()

    return vector_of_points_to_return






# for testing :

# if __name__ == '__main__':
#     import matplotlib.pyplot as plt
#     # Create an object with a number of desirable courses and points.
#     # In this case for example- 5 courses and 100 points divided (change it if you want as your wish)
#     strategy = Strategies(5, 100)
#     # a vector that returned from the function according to the desired point distribution (exp, const, lin,quadratic):
#     vector_score_by_function = strategy.linear()
#
#     # a list that simply contains numbers from 1 to the number of courses so that we can see in the graph the ratio:
#     vector_of_courses = list(range(1, strategy.courses+1))
#
#     # plot the graph
#     print(vector_of_courses)
#     print(vector_score_by_function)
#     plt.plot(vector_of_courses, vector_score_by_function[:strategy.courses])
#     plt.show()
