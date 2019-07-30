"""
Runner.py
--------------
This file produces a file which includes all the situations.

Written by: Mattan Yerushalmi.
"""
import numpy as np
from scipy.special import comb
from AllCourses import AllCourses
from Matcher import Matcher
from Strategy import Strategy
from Main import UPLOAD_COURSES_LIST_FROM_FILE, NUM_OF_STRATEGIES, NUM_OF_STUDENTS, CLASS_SIZE, DATA_TEXT_FILE, \
    PRINT_EVERYTHING

"""
Constants:
"""
# List of all courses.
ALL_COURSES = AllCourses(UPLOAD_COURSES_LIST_FROM_FILE).get_list_of_courses()

# Just for checking progress when debugging:
# should be : (num of students + num of strategies) choose
NUM_OF_TEST_CASES = comb(NUM_OF_STUDENTS + NUM_OF_STRATEGIES, NUM_OF_STRATEGIES - 1, exact=True)


"""
Methods:
"""


def cake_factory(cur_index, cake, cakes):
    """
    The recursive student division generator.
    :param cur_index: used in the recursive call
    :param cake: a list of divisions
    :param cakes: the list of lists
    :return: a list of lists of divisions
    """
    if cur_index == NUM_OF_STRATEGIES - 1:
        cake[cur_index] = NUM_OF_STUDENTS - sum([cake[j] for j in range(cur_index)])
        cakes.append(cake.copy())
        return cakes

    for i in range(NUM_OF_STUDENTS + 1 - sum([cake[j] for j in range(cur_index)])):
        cake[cur_index] = i
        cakes = cake_factory(cur_index + 1, cake, cakes)
    return cakes


def get_cakes_the_one_against_all_situation():
    """
    returns the cakes which is needed only for the case which we tested first
    which is: all students vote same, what should one do in order to make his
    position better.

    Gill did this shit!  #ZadaTech
    """
    cakes = [[100, 0, 0, 0, 0], [0, 100, 0, 0, 0], [0, 0, 100, 0, 0], [0, 0, 0, 100, 0], [0, 0, 0, 0, 100]
         , [99, 1, 0, 0, 0], [99, 0, 1, 0, 0], [99, 0, 0, 1, 0], [99, 0, 0, 0, 1], [1, 99, 0, 0, 0], [0, 99, 1, 0, 0],
              [0, 99, 0, 1, 0], [0, 99, 0, 0, 1], [1, 0, 99, 0, 0], [0, 1, 99, 0, 0], [0, 0, 99, 1, 0],
             [0, 0, 99, 0, 1], [1, 0, 0, 99, 0], [0, 1, 0, 99, 0], [0, 0, 1, 99, 0], [0, 0, 0, 99, 1],
              [1, 0, 0, 0, 99], [0, 1, 0, 0, 99], [0, 0, 1, 0, 99], [0, 0, 0, 1, 99]]
    return cakes


def get_cakes_for_all_situations():
    """
    :return: The list of list generated in the factory. This is the initial call to the recursive function.
    """
    return cake_factory(0, [0 for i in range(NUM_OF_STRATEGIES)], [])


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

    # Satisfactions_tuples is a collection of tuples like:
    # (sum of satisfactions scores for the i'th strategy, number of students from the i'th strategy)
    satisfactions_tuples = [[0, 0] for i in range(NUM_OF_STRATEGIES)]
    SUM, COUNT = 0, 1

    # The satisfaction rates of all students.
    individuals_satisfaction = []

    # Going over all students calculating the satisfactions.
    for student in students:
        # Single student satisfactions:
        student_satisfaction = student.evaluate_satisfaction()
        # Update & Adding the value to the right places.
        satisfactions_tuples[student.get_strategy_by_value()][SUM] += student_satisfaction
        satisfactions_tuples[student.get_strategy_by_value()][COUNT] += 1
        individuals_satisfaction.append(student_satisfaction)

    # Parameters describes the whole picture of satisfaction: median and average.
    median = calculate_median_of_list(individuals_satisfaction)
    avg = calculate_average_of_list(individuals_satisfaction)

    satisfactions = []
    for i in range(len(satisfactions_tuples)):
        if satisfactions_tuples[i][COUNT] != 0:
            satisfactions.append(satisfactions_tuples[i][SUM] / satisfactions_tuples[i][COUNT])
        else:  # to avoid div-by-zero
            satisfactions.append(0)

    satisfactions.append(median)
    satisfactions.append(avg)
    return satisfactions


def get_results():
    """
    :return: a list of lists containing
    [num_students_in_str_1, ..., num_students_in_str_n, avg_satisfaction_of_str_1, ..., avg_satisfaction_of_str_n,
    overall_avg_satisfaction]
    """
    cakes = get_cakes_for_all_situations()
    cakes_counter = 0  # just to check progress

    for cake in cakes:
        # just to check progress :
        if PRINT_EVERYTHING and cakes_counter % 10000 == 0:
            print("   Num of lines in file: " + str(cakes_counter) + "/" + str(
                NUM_OF_TEST_CASES) + ", progress rate: " + str(
                100 * round(float(cakes_counter / NUM_OF_TEST_CASES), 2)))

        strategy_dict = get_strategy_dict(cake)
        matcher = Matcher(ALL_COURSES, strategy_dict, CLASS_SIZE).match()
        cake += get_satisfactions(matcher)

        cakes_counter += 1  # just to check progress ..

    return cakes


def main_runner():
    """
    runs the entire file's methods.
    Produces the file with the data.
    """
    f = open(DATA_TEXT_FILE, "w+")
    for item in get_results():
        write_to_file = str(item).strip('[]')
        write_to_file += "\n"
        f.write(write_to_file)
    f.close()


# --- Helper methods ---- #

def calculate_median_of_list(satisfactions):
    """
    This method receives a list of float and calculates the median.
    :return float (the median number)
    """
    satisfactions_array = np.array(satisfactions)
    median = np.median(satisfactions_array)
    return median


def calculate_average_of_list(satisfactions):
    """
    This method receives a list of float and calculates the average.
    :return float (the average number)
    """
    satisfactions_array = np.array(satisfactions)
    avg = np.average(satisfactions_array)
    return avg

