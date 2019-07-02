"""
CoursesList.py
--------------
This file includes the courses list each student has.
It has a functionality to return a random list or a default set list.
Each student has a field of this class which stated which courses the student took.

Written by: Omer Liberman (July 2nd).
"""

import random
from AllCourses import AllCourses

"""
List of all the courses in the university.
"""
upload_courses_from_file = False
ALL_COURSES = AllCourses(upload_courses_from_file).get_list_of_courses()

"""
Default number of courses each student select.
"""
DEF_NUM_OF_COURSES_PER_STUDENT = 5


class CoursesList:

    def __init__(self, num_of_courses=DEF_NUM_OF_COURSES_PER_STUDENT):
        self.num_of_courses = num_of_courses
        self.selected_courses = None

    def select_courses_randomly(self):
        """
        Make a random selection of self.num_of_courses out of the all courses.
        Just update the field self.selected_courses of the class.
        """
        self.selected_courses = list(random.sample(ALL_COURSES, self.num_of_courses))

    def select_courses_uniformly(self):
        """
        Make a uniform selection of self.num_of_courses out of the all courses.
        Just update the field self.selected_courses of the class.
        """
        self.selected_courses = list(ALL_COURSES[:self.num_of_courses])

    def get_selected_courses(self):
        """
        Raise an exception if the courses hasn't been selected.
        *** Make sure you first select the courses !!! ***
        :return: the list of selected courses (self.selected_courses).
        """
        if self.selected_courses is None:
            raise Exception("Courses has yet been selected!")
        return self.selected_courses

