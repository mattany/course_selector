"""
Balance.py
--------------
This file includes methods which intends to find balance point.
Means that - finding a case where the satisfaction rate of all strategies
is (approximately) equal.
That is what we may consider "optimal" distribution.

Written by: Omer Liberman (July 30th).
"""
import pandas as pd

# Range for "mistake" - means that this the gap which we consider ok for difference of satisfaction rates
EPSILON = 0.05

# The names of data files.
DATA_FILE_L1_NORM = "rare_data_L1.txt"
DATA_FILE_BORDA_COUNT = "rare_data_borda.txt"

# Columns of students numbers.
COL_STU_NUM = ['Num of students - Const', 'Num of students - SquaredPow', 'Num of students - Exp',
               'Num of students - Linear', 'Num of students - Random']

# Columns of students satisfaction rate.
COL_STU_SAT_RATE = ['Avg Rate of students - Const', 'Avg Rate of students - SquaredPow',
                     'Avg Rate of students - Exp', 'Avg Rate of students - Linear', 'Avg Rate of students - Random']


def load_data(file_name):
    """
    Loads the data file into a python data frame.
    """
    columns_names = ["Num of students - Const", "Num of students - SquaredPow", "Num of students - Exp",
                     "Num of students - Linear",
                     "Num of students - Random", "Avg Rate of students - Const", "Avg Rate of students - SquaredPow",
                     "Avg Rate of students - Exp", "Avg Rate of students - Linear", "Avg Rate of students - Random",
                     "Median(all students)",
                     "Average(all students)"]
    to_ret = pd.read_csv(file_name, names=columns_names)
    print("Data loaded successfully.")
    return to_ret


def find_equilibrium(data_frame_loaded):
    balance_rows = []

    print("Start Looking for Equilibrium: ")
    for row_index, row_content in data_frame_loaded.iterrows():
        all_strategies_are_represented = True
        all_sat_rates_are_in_right_range = True

        for col in COL_STU_NUM:
            if row_content[col] == 0:
                all_strategies_are_represented = False
                break

        satisfactions_rates = []
        for col in COL_STU_SAT_RATE:
            satisfactions_rates.append(row_content[col])

        max_of_rates, min_of_rates = max(satisfactions_rates), min(satisfactions_rates)
        if max_of_rates - min_of_rates > EPSILON:
            all_sat_rates_are_in_right_range = False

        if all_strategies_are_represented is True and all_sat_rates_are_in_right_range is True:
            print("The " + str(len(balance_rows)) + " equilibrium.")
            to_append = (row_index, row_content)
            balance_rows.append(to_append)

    # Print out the results:
    if len(balance_rows) == 0:
        print("No Equilibrium!")
    else:
        print("Equilibrium found:")
        for r in balance_rows:
            print(r)


if __name__ == '__main__':
    df = load_data(DATA_FILE_L1_NORM)
    find_equilibrium(df)
