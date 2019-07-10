"""
Satisfaction.py
--------------
This file includes the satisfaction measurer of each student has.
Satisfaction measurer receives the pre-assignments preferences of student
and the assignments of the student to _courses, and : EVALUATE the student's satisfaction level.

Written by: Omer Liberman (July 3rd).
"""


def borda_count_evaluation(pre_assignment_preferences, post_assignment_results):
    """
    Formula:
    if student got the i'th course in his ranking, the satisfaction rank receives:
    SATISFACTION(c_i) = (#COURSES + 1) - i
    TOT_SATISFACTION = sum[SATISFACTION(c_i) for i in range(#COURSES)] / sum[ i for i in range(#COURSES) ]

    Example:
    if each student evaluates 10 _courses : c1, c2, ..., c10
    and the student got _courses 1, 3, 8
    the student satisfaction measurement for each _courses is : 10, 8, 3
    the total is - 10 + 8 + 3 = 21
    and then we want to normalize this : 21 / ( 1 + 2 + ... + 10) = 21 / 55 = 0.38
    So, the student satisfaction measure is 0.38

    :param pre_assignment_preferences: dictionary. shape: {course1 : rank}
    :param post_assignment_results: array which describes the _courses the student got
    after _courses assignment process.
    :return: number which describes level of satisfaction.
    """

    courses_ranks = list(pre_assignment_preferences.items())
    courses_ranks.sort(key=lambda x: x[1], reverse=True)

    tot = 0
    for i in range(len(courses_ranks)):
        if courses_ranks[i][0] in post_assignment_results:
            tot += len(courses_ranks) - i

    to_norm = sum([(i+1) for i in range(len(courses_ranks))])

    return tot / to_norm


def investment_evaluation(pre_assignment_preferences, post_assignment_results):
    """
    Formula:
    if student got the i'th course in his ranking, the satisfaction rank receives:
    SATISFACTION(c_i) = #(points given to the i'th course by the student)
    TOT_SATISFACTION = sum[SATISFACTION(c_i) for i in range(#COURSES)] / sum[ points students shared ]

    Example:
    if each student evaluates 10 _courses : c1, c2, ..., c10
    and the student got _courses 1, 3, 8 with ranks 60, 17, 2 (he had a total of 100 to distribute)
    the total is - 60 + 17 + 2 = 79
    and then we want to normalize this : 79 / 100 = 0.79
    So, the student satisfaction measure is 0.79

    :param pre_assignment_preferences: dictionary. shape: {course1 : rank}
    :param post_assignment_results: array which describes the _courses the student got
    after _courses assignment process.
    :return: number which describes level of satisfaction.
    """

    courses_ranks = list(pre_assignment_preferences.items())
    courses_ranks.sort(key=lambda x: x[1], reverse=True)

    tot = 0
    for i in range(len(courses_ranks)):
        if courses_ranks[i][0] in post_assignment_results:
            tot += courses_ranks[i][1]

    to_norm = sum([courses_ranks[i][1] for i in range(len(courses_ranks))])

    return tot / to_norm


# # Testing:
# def main():
#     pre = {"c1":3, "c2":1, "c3":11}
#     post = ["c3"]
#
#     print(borda_count_evaluation(pre, post))
#     print(investment_evaluation(pre, post))
#
# main()
