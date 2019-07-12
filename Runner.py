import math

from itertools import *
import numpy as np
from AllCourses import AllCourses
from Matcher import Matcher
from Strategy import Strategy
import time

all_courses = AllCourses().get_list_of_courses()
num_of_students = 100
CLASS_SIZE = 30
num_of_strategies = len(Strategy)


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


def get_median(sats):
    sats_array = np.array(sats)
    median =  np.median(sats_array)
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
    sats_tuples = [[0, 0] for i in range(len(Strategy))]  # sum of satisfactions, count
    individual_sats = []
    for student in students:
        sat = student.evaluate_satisfaction()
        sats_tuples[student._strategy.value][0] += sat
        individual_sats.append(sat)
        sats_tuples[student._strategy.value][1] += 1
    median = get_median(individual_sats)
    sats = [sats_tuples[i][0] / sats_tuples[i][1] if sats_tuples[i][1] != 0 else 0 for i in range(len(sats_tuples))]
    sats.append(median)
    # sats.append(sum(sats_tuples[i][0] for i in range(len(sats_tuples))) / num_of_students)
    return sats


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
        matcher = Matcher(all_courses, strategy_dict, CLASS_SIZE).match()
        cake += get_satisfactions(matcher)
    return cakes


if __name__ == "__main__":
    # print(str(get_strategy_dict([0, 1, 5, 1])))
    t1_start = time.perf_counter()                    #todo delete timers
    t2_start = time.process_time()
    f = open("combinations_2.txt", "w+")
    for item in get_results():
        f.write('%s\n' % item)
    f.close()
    t1_stop = time.perf_counter()
    t2_stop = time.process_time()
    print("--------------------------------------------------")
    print("Elapsed time: %.1f [min]" % ((t1_stop - t1_start) / 60))
    print("CPU process time: %.1f [min]" % ((t2_stop - t2_start) / 60))
    print("--------------------------------------------------")
