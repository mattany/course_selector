"""
Student.py
--------------
This file includes the class of single student.
Each student has:
1) list of courses (coursesList.py)
2) points distribution between the courses (strategy.py)
3) satisfaction function which indicated the level of satisfaction (satisfaction.py)
4) courses and scores (dictionary)

Written by: Omer Liberman (July 5th).
"""

from Satisfaction import borda_count_evaluation, investment_evaluation
from CoursesList import select_courses_randomly, select_courses_uniformly
from Strategy import strategy_factory


class Student:
    DEF_NUM_OF_POINTS = 100

    def __init__(self, strategy, courses_list, points=DEF_NUM_OF_POINTS, satisfaction_func=borda_count_evaluation,
                 random_courses=False):
        """
        :param strategy: the strategy of points distribution between courses.
        :param courses_list: the list of courses which the student select from.
        :param points: the number of points to distribute between the courses.
        :param satisfaction_func: the func which measure satisfaction of assignment.
        :param random_courses: boolean. determines weather all student have same preferences or not.
        """
        self.strategy = strategy_factory(strategy, len(courses_list), points)  # array of the points distribution
        self.satisfaction_func = satisfaction_func
        self.courses_and_scores = None

        if random_courses:
            self.courses = select_courses_randomly(len(courses_list), courses_list)
        else:
            self.courses = select_courses_uniformly(len(courses_list), courses_list)

    def fit_courses_and_scores(self):
        """
        Fits the courses to the strategy.
        stores the result in self.courses_and_scores.
        """

        # take the self.courses and self.strategy and fits them into self.courses_and_scores.
        self.courses_and_scores = dict()

        for ind in range(len(self.courses)):
            self.courses_and_scores[self.courses[ind]] = self.strategy[ind]

    def evaluate_satisfaction(self, post_assignment_results):
        """
        :param post_assignment_results: array which describes the courses the student got
        after courses assignment process.
        :return: the evaluation score (float in range [0,1])
        """
        return self.satisfaction_func(self.courses_and_scores, post_assignment_results)

    def get_courses_and_scores(self):
        """
        :return: the dictionary of courses and the scores which the strategy
        matched it.
        """
        return self.courses_and_scores
