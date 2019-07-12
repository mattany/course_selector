"""
ExcelExporter.py
--------------
This file includes the methods which makes analytics.

Example:
    exporter = ExcelExporter()
    exporter.run()

    exporter1 = ExcelExporter("input_txt_file.txt", "output_excel_file.csv")
    exporter1.run()

Written by: Omer Liberman (July 12nd).
"""

from Runner import OUTPUT_TEXT_FILE_NAME
from Strategy import Strategy
import pandas as pd

"""
The name of the excel file which is created and includes the data extracted by Runner.
"""
OUTPUT_EXCEL_FILE_NAME = "data.csv"

"""
Number of strategies.
"""
NUM_OF_STRATEGIES = len(Strategy)

"""
Columns Headlines
"""
num_of_students_headline = "Num of students from strategy "
satisfaction_rate_headline = "Satisfaction Rate of students from strategy "
headlines_relevant_for_all_strategies = [num_of_students_headline, satisfaction_rate_headline]
# -----
total_satisfaction_headline = "Satisfaction Rate (all students)"


class ExcelExporter:

    def __init__(self, input_text_file=OUTPUT_TEXT_FILE_NAME, output_excel_file=OUTPUT_EXCEL_FILE_NAME):
        """
        :param input_text_file: the text file should be parsed to excel.
        :param output_excel_file: the address of the output excel file.
        """
        self.input_text_file = input_text_file
        self.output_excel_file = output_excel_file
        self.columns = None

    def _create_columns_titles(self):
        """
        :return: titles for the columns in the excel.
        IMPORTANT - IT WORKS ONLY FOR THIS PROJECT!
        """
        columns_titles = []
        for headline in headlines_relevant_for_all_strategies:
            for name, member in Strategy.__members__.items():
                to_append = headline + str(name)
                columns_titles.append(to_append)
        columns_titles.append(total_satisfaction_headline)
        return columns_titles

    def _convert_results_file_to_excel(self):
        """
        MAKE SURE THE TEXT FILE IS EXISTED BEFORE USE THIS METHOD!
        In order to generate it call the method run_program in analyzer.

        This method takes the txt file which was made by the Runner.
        This file includes all the data extracted.
        The excel file is named EXCEL_DATA_FILE
        """
        df = pd.read_csv(self.input_text_file)
        df.columns = self._create_columns_titles()
        df.to_csv(self.output_excel_file)

    def run(self):
        """
        Runs the purpose of the object - creates the wanted excel.
        :return:
        """
        self._convert_results_file_to_excel()


