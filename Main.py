"""
Main.py
--------------
In this file we can control the entire situation.
Means that here we run the entire program, change constants, etc.

Written by:
"""

from Satisfaction import borda_count_evaluation,investment_evaluation
import Strategy

"""
General Constants - relevant for the entire situation we run.
"""
# Number of strategies in the game.
NUM_OF_STRATEGIES = len(Strategy)

# Number of students.
NUM_OF_STUDENTS = 100

# Size of class.
CLASS_SIZE = 0

"""
Relevant for the each student.
"""
# Number of points each student have to share between courses.
POINTS_FOR_EACH_STUDENT = 100

# The satisfaction func each student use to evaluate his assignments.
SATISFACTION_FUNC = borda_count_evaluation

# Boolean value weather to upload the course list from a file.
UPLOAD_COURSES_LIST_FROM_FILE = False

# Boolean which indicates whether students has a random courses selection.
RANDOM_COURSES_SELECTION_FOR_EACH_STUDENT = False

"""
Technical Constants - relevant to data files and files uploading.
"""
# The name of the text file which Runner.py outputs the data to.
DATA_TEXT_FILE = ""

# This boolean intend to avoid time wasting for re-creating the text file.
IS_TEXT_FILE_EXIST = False

# The name of the excel file which ExcelExporter.py converts the data from the text file to.
DATA_EXCEL_FILE = ""

# This boolean intend to avoid time wasting for re-creating the excel file.
IS_EXCEL_FILE_EXIST = False







