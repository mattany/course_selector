"""
Graphs.py
--------------
In this file the graphs are created.
It first creates the text file and then convers it to excel file.
Then, insert the data to Pandas DataFrame.
And then we use the library matplotlib.pyplot to create beautiful graphs.

Written by: Omer Liberman (July 14nd).
"""

from Runner import run
from ExcelExporter import ExcelExporter
import matplotlib.pyplot as plt
import pandas as pd


def create_data_excel_file():
    """
    Runs the methods in Runner and in ExcelExporter which creates the text file
    and then insert the data to excel.
    :return: the address\name of the excel file.
    """
    run()
    excel_exporter = ExcelExporter()
    excel_exporter.run()
    return excel_exporter.get_excel_file_name()


dataset_address = create_data_excel_file()

data_frame = pd.read_csv(dataset_address)

print("A")


