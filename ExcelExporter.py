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

from Strategy import Strategy
import pandas as pd

"""
Columns Headlines
"""
num_of_students_headline = "Num of students - "
satisfaction_rate_headline = "Avg Rate of students - "
headlines_relevant_for_all_strategies = [num_of_students_headline, satisfaction_rate_headline]
# -----
median_satisfaction_headline = "Median (all students)"
avg_satisfaction_headline = "Average (all students)"


class ExcelExporter:

    def __init__(self, input_text_file, output_excel_file):
        """
        :param input_text_file: the text file should be parsed to excel.
        :param output_excel_file: the address of the output excel file.
        """
        self._input_text_file = input_text_file
        self._output_excel_file = output_excel_file
        self.columns = None

    @staticmethod
    def _create_columns_titles():
        """
        :return: titles for the columns in the excel.
        IMPORTANT - IT WORKS ONLY FOR THIS PROJECT!
        """
        columns_titles = list()
        for headline in headlines_relevant_for_all_strategies:
            for name, member in Strategy.__members__.items():
                to_append = headline + str(name)
                columns_titles.append(to_append)
        columns_titles.append(median_satisfaction_headline)
        columns_titles.append(avg_satisfaction_headline)
        return columns_titles

    def _convert_results_file_to_excel(self):
        """
        MAKE SURE THE TEXT FILE IS EXISTED BEFORE USE THIS METHOD!
        In order to generate it call the method run_program in analyzer.

        This method takes the txt file which was made by the Runner.
        This file includes all the data extracted.
        The excel file is named EXCEL_DATA_FILE
        """
        df = pd.read_csv(self._input_text_file, names=ExcelExporter._create_columns_titles())
        # df.columns = ExcelExporter._create_columns_titles()
        df.to_csv(self._output_excel_file)

    def run(self):
        """
        Runs the purpose of the object - creates the wanted excel.
        :return:
        """
        self._convert_results_file_to_excel()
