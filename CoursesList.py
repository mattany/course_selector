"""
CoursesList.py
--------------
This file includes the _courses list each student has.
It has a functionality to return a random list or a default set list.
Each student has a field of this class which stated which _courses the student took.

Written by: Omer Liberman (July 2nd).
"""

import random


def select_courses_randomly(num_of_courses, courses_list):
    """
    Make a random selection of self.num_of_courses out of the all _courses.
    Just update the field self.selected_courses of the class.
    """
    return list(random.sample(courses_list, num_of_courses))


def select_courses_uniformly(num_of_courses, courses_list):
    """
    Make a uniform selection of self.num_of_courses out of the all _courses.
    Just update the field self.selected_courses of the class.
    """
    return list(courses_list[:num_of_courses])


