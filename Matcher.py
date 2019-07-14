"""
Matcher.py
--------------
This class makes the assignment of students to classes.

Example:
    CLASS_SIZE = 30
    matcher = Matcher(course_list, strategy_d, CLASS_SIZE)
    matcher.match()   ----> returns list of students with their assignment.

Written by: Linoy Palas (July 10th).
"""

from Student import Student


class Matcher:
    def __init__(self, courses_list, strategy_dict, class_size, random_list_for_each_student=False):

        """
        :param courses_list: list of _courses.
        :param strategy_dict: dict which looks like {_strategy: num_of_students_uses_this _strategy}
        :param class_size: the number of students which can be in each course.
        :param random_list_for_each_student: boolean. describes if each student has his own preferences list
        or all students have same preferences.
        """
        self._courses_list = courses_list
        self._strategy_dict = strategy_dict
        self._class_size = class_size
        self._students_list = []
        self.random_list_for_each_student = random_list_for_each_student

    def _set_student_list(self):
        """
        Creates the list of students base on their _strategy.
        (the number of students is the sum of the values in self._strategy_dict)
        Saves this list in self._students_list
        """
        for key, value in self._strategy_dict.items():
            for i in range(value):
                student = Student(key, self._courses_list, self.random_list_for_each_student)
                student.fit_courses_and_scores()
                self._students_list.append(student)

    def _courses_matching(self):
        """
        This method makes the course matching.
        Each student gives points to specific course.
        For each course , we sort the list of students by the score the student
        gives to the specific course.
        The first (self._class_size) students are assigned to the course.
        """
        for course in self._courses_list:
            self._students_list.sort(key=lambda s: s.courses_and_scores[course], reverse=True)
            for i in range(self._class_size):
                self._students_list[i].add_assignment(course)

    def match(self):
        """
        This method runs the other methods.
        :return: list of students with their assignments included.
        """
        self._set_student_list()
        self._courses_matching()
        return self._students_list

# FOR TESTING:

# if __name__ == '__main__':
#     from AllCourses import AllCourses
#     from Strategy import Strategy
#
#     course_list = AllCourses().get_list_of_courses()
#     strategy_d = {Strategy.Linear: 2, Strategy.Const: 2, Strategy.Exp: 2, Strategy.Quad: 2}
#     matcher = Matcher(course_list, strategy_d, 3)
#     print(matcher.match())
