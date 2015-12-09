__author__ = 'Matthew'
# This analysis performs ANOVA on the survey data

import pandas
import openpyxl as pyxl
import os

# define the root directory where the data are
data_root_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print("Study Data Root Directory: ", data_root_dir)

# remember where the program executed
program_dir = os.getcwd()

# change to the study data directory
os.chdir(data_root_dir)

# open the workbook containing the data
study_book_file_name = "user_study_dec_7_2015.xlsx"
study_book = pyxl.load_workbook(study_book_file_name)

# open the survey sheet
survey_sheet = study_book.get_sheet_by_name('Survey')


