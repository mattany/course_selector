"""
Runner.py
--------------
This file produces a file which includes all the situations.

Written by: Mattan Yerushalmi.
"""

# ------- IMPORTS ------- #
import math
import numpy as np
from AllCourses import AllCourses
from Matcher import Matcher
from Strategy import Strategy

# ------- CONSTANTS ------- #

"""
The file where the data is exported to.
"""
OUTPUT_TEXT_FILE = "combinations_2.txt"

"""
List of all courses.
"""
ALL_COURSES = AllCourses().get_list_of_courses()

"""
- Number of students 
- The number of tactics (strategies) which students can take in order
  to distribute their points over the available courses.
"""
num_of_students = 100
num_of_strategies = len(Strategy)

"""
Size of class (num of students can be in single course.
"""
CLASS_SIZE = 30


# ------- METHODS ------- #

def cake_factory(cur_index, cake, cakes):
    """
    The recursive student division generator.
    :param cur_index: used in the recursive call
    :param cake: a list of divisions
    :param cakes: the list of lists
    :return: a list of lists of divisions
    """
    if cur_index == num_of_strategies - 1:
        cake[cur_index] = num_of_students - sum([cake[j] for j in range(cur_index)])
        cakes.append(cake.copy())
        return cakes

    for i in range(num_of_students + 1 - sum([cake[j] for j in range(
            cur_index)])):
        cake[cur_index] = i
        cakes = cake_factory(cur_index + 1, cake, cakes)

    return cakes


def get_median(satisfactions):
    satisfactions_array = np.array(satisfactions)
    median = np.median(satisfactions_array)
    return median


def get_cakes():
    """
    :return: The list of list generated in the factory. This is the initial call to the recursive function.
    """
    return cake_factory(0, [0 for i in range(num_of_strategies)], [])


def get_strategy_dict(dist):
    """
    :param dist: distribution (a single cake)
    :return: dictionary of {strategy : number of students in the strategy}
    """
    return dict(zip([i for i in Strategy], dist))


def get_satisfactions(students):
    """
    :param students: A list of students (student objects)
    :return: A list of the average satisfactions for each strategy (ordered according to the enum),
    and the average overall satisfaction at the end.
    """
    satisfactions_tuples = [[0, 0] for i in range(num_of_strategies)]  # sum of satisfactions, count
    individual_satisfaction = []
    for student in students:
        sat = student.evaluate_satisfaction()
        satisfactions_tuples[student.get_strategy_by_value()][0] += sat
        individual_satisfaction.append(sat)
        satisfactions_tuples[student.get_strategy_by_value()][1] += 1
    median = get_median(individual_satisfaction)
    satisfactions = [satisfactions_tuples[i][0] / satisfactions_tuples[i][1] if satisfactions_tuples[i][1] != 0 else 0
                     for i in
                     range(len(satisfactions_tuples))]
    satisfactions.append(median)
    return satisfactions


def get_results():
    """
    :return: a list of lists containing
    [num_students_in_str_1, ..., num_students_in_str_n, avg_satisfaction_of_str_1, ..., avg_satisfaction_of_str_n,
    overall_avg_satisfaction]
    """
    cakes = get_cakes()
    one_percent = math.floor(len(cakes) / 100)  # TODO delete - prints
    percents = [(one_percent * i, i) for i in range(100)]  # TODO delete - prints
    for cake in cakes:
        if len(percents) > 0 and cakes[percents[0][0]] == cake:  # TODO delete - prints
            print(percents[0][1])  # TODO delete - prints
            percents.pop(0)  # TODO delete - prints
        strategy_dict = get_strategy_dict(cake)
        matcher = Matcher(ALL_COURSES, strategy_dict, CLASS_SIZE).match()
        cake += get_satisfactions(matcher)
    return cakes


if __name__ == "__main__":
    import time
    t1_start = time.perf_counter()  # todo delete timers
    t2_start = time.process_time()
    f = open(OUTPUT_TEXT_FILE, "w+")
    for item in get_results():
        f.write('%s\n' % item)
    f.close()
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print("--------------------------------------------------")
    print("Elapsed time: %.1f [min]" % ((t1_stop - t1_start) / 60))
    print("CPU process time: %.1f [min]" % ((t2_stop - t2_start) / 60))
    print("--------------------------------------------------")
