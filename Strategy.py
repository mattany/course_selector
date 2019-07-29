"""
Strategy.py
--------------
This file includes the _points_distribution each student has.
Strategy is defined by a function, then defined to distribution of
all the points student can distribute over the _courses.

Written by: Linoy Palas (July 8th)
"""

import numpy as np
import random as rand
import enum

# --------
# IMPORTANT : If you want to add another strategy - you should add it both to the
# enum class and to the factory.
# --------


class Strategy(enum.Enum):
    # Uniform distribution over the courses.
    Const = 0
    # Using the func f(x) = x^2.
    SquaredPow = 1
    # Using the func f(x) = e^x.
    Exp = 2
    # Using the func f(x) = x.
    Linear = 3
    # Randomize points distribution.
    Random = 4


def strategy_factory(strategy, num_of_courses, points_to_share):
    """
    This func is a factory of the strategies.
    :param strategy: a _points_distribution type (enum).
    :param num_of_courses: the number of _courses.
    :param points_to_share: the number of points to distribute between _courses.
    :return: array where in the i'th coord there is the number of points for the
    i'th course in priority.
    """
    if strategy == Strategy.Const:
        return constant(num_of_courses, points_to_share)

    elif strategy == Strategy.SquaredPow:
        return power(num_of_courses, points_to_share)

    elif strategy == Strategy.Exp:
        return exp(num_of_courses, points_to_share)

    elif strategy == Strategy.Linear:
        return linear(num_of_courses, points_to_share)

    elif strategy == Strategy.Random:
        return random_selection(num_of_courses, points_to_share)

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
        vector_of_points_to_return[i] = round(vector_of_points[i] * points_to_share / sum_of_score, 3)

    # to have it in descending order:
    vector_of_points_to_return.reverse()

    return vector_of_points_to_return


def power(num_of_courses, points_to_share, power_by=2):
    vector_of_points_to_return = [0] * (num_of_courses + 1)
    vector_of_points = [0] * (num_of_courses + 1)  # this list holds the score based on position
    for i in range(1, len(vector_of_points_to_return)):  # lst is the list
        vector_of_points[i] = i ** power_by
    sum_of_score = sum(vector_of_points)  # this will be the sum of all the scores will used for

    for i in range(1, len(vector_of_points_to_return)):
        vector_of_points_to_return[i] = round(vector_of_points[i] * points_to_share / sum_of_score, 3)

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
        vector_of_points_to_return[i] = round(vector_of_points[i] * points_to_share / sum_of_score, 3)

    # to have it in descending order:
    vector_of_points_to_return.reverse()

    return vector_of_points_to_return


def random_selection(num_of_courses, points_to_share):
    vector_of_points_to_return = [0] * (num_of_courses + 1)
    vector_of_points = [0] * (num_of_courses + 1)  # this list holds the score based on position
    for i in range(1, len(vector_of_points_to_return)):  # lst is the list
        vector_of_points[i] = rand.uniform(0, 1)
    sum_of_score = sum(vector_of_points)  # this will be the sum of all the scores will used for

    for i in range(1, len(vector_of_points_to_return)):
        vector_of_points_to_return[i] = round(vector_of_points[i] * points_to_share / sum_of_score, 3)

    vector_of_points_to_return.sort(reverse=True)

    return vector_of_points_to_return


# for testing :

# if __name__ == '__main__':
    # import matplotlib.pyplot as plt
    # # Create an object with a number of desirable _courses and points.
    # # In this case for example- 5 _courses and 100 points divided (change it if you want as your wish)
    # _points_distribution = Strategies(5, 100)
    # # a vector that returned from the function according to the desired point distribution (exp, const, lin,quadratic):
    # vector_score_by_function = _points_distribution.linear()
    #
    # # a list that simply contains numbers from 1 to the number of _courses so that we can see in the graph the ratio:
    # vector_of_courses = list(range(1, _points_distribution._courses+1))
    #
    # # plot the graph
    # print(vector_of_courses)
    # print(vector_score_by_function)
    # plt.plot(vector_of_courses, vector_score_by_function[:_points_distribution._courses])
    # plt.show()

    # r = random_selection(8, 100)
    # print(r)

