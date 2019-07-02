"""
AllCourses.py
--------------
This file includes the list of all the courses in school
There is a default list of courses which includes 8 well known courses
or you can upload new courses from a file text is called "AllCourses.txt" and
looks like:

AllCourses.txt:
course_name_1
course_name_2
...
course_name_AnyNumber

Written by: Omer Liberman (July 2nd).
"""


def read_courses_from_file():
    """
    Read given courses from a file (each course in separated line).
    :return: array of the courses.
    """
    courses = []
    with open("AllCourses.txt") as f:
        for line in f:
            courses.append(line)
    return courses


class AllCourses:
    DEF_LIST_OF_ALL_COURSES = ["Intro to AI", "Crypto", "Intro to ML",
                               "Algorithms", "Infi", "Macro", "Probability",
                               "Intro to NN"]

    def __init__(self, upload=False):
        if not upload:
            self.all_courses_list = AllCourses.DEF_LIST_OF_ALL_COURSES
        else:
            self.all_courses_list = read_courses_from_file()

    def get_list_of_courses(self):
        """
        :return: the list of all courses in the school (list of strings).
        """
        return self.all_courses_list


