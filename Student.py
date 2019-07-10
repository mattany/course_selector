"""
Student.py
--------------
This file includes the class of single student.
Each student has:
1) list of _courses (coursesList.py)
2) points distribution between the _courses (_points_distribution.py)
3) satisfaction function which indicated the level of satisfaction (satisfaction.py)
4) _courses and scores (dictionary)

Written by: Omer Liberman (July 5th).
"""

from Satisfaction import borda_count_evaluation, investment_evaluation
from CoursesList import select_courses_randomly, select_courses_uniformly
from Strategy import strategy_factory

DEF_NUM_OF_POINTS = 100


class Student:

    def __init__(self, strategy, courses_list, points=DEF_NUM_OF_POINTS, satisfaction_func=borda_count_evaluation,
                 random_courses=False):
        """
        :param strategy: the _points_distribution of points distribution between _courses.
        :param courses_list: the list of _courses which the student select from.
        :param points: the number of points to distribute between the _courses.
        :param satisfaction_func: the func which measure satisfaction of assignment.
        :param random_courses: boolean. determines weather all student have same preferences or not.
        """
        self._strategy = strategy
        # array of the points distribution:
        self._points_distribution = strategy_factory(self._strategy, len(courses_list), points)
        self._satisfaction_func = satisfaction_func
        self._post_assignment_results = []
        self.courses_and_scores = None

        if random_courses:
            self._courses = select_courses_randomly(len(courses_list), courses_list)
        else:
            self._courses = select_courses_uniformly(len(courses_list), courses_list)

    def fit_courses_and_scores(self):
        """
        Fits the _courses to the _points_distribution.
        stores the result in self.courses_and_scores.
        """

        # take the self._courses and self._points_distribution and fits them into self.courses_and_scores.
        self.courses_and_scores = dict()

        for ind in range(len(self._courses)):
            self.courses_and_scores[self._courses[ind]] = self._points_distribution[ind]

    def evaluate_satisfaction(self):
        """
        :return: the evaluation score (float in range [0,1])
        """
        return self._satisfaction_func(self.courses_and_scores,
                                       self._post_assignment_results)

    def get_courses_and_scores(self):
        """
        :return: the dictionary of _courses and the scores which the _points_distribution
        matched it.
        """
        return self.courses_and_scores

    def add_assignment(self, new_course):
        self._post_assignment_results.append(new_course)
