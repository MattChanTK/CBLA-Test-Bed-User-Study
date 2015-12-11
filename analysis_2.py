__author__ = 'Matthew'

import xlrd
import csv
import os
import glob
import numpy as np
from scipy import stats

# define the root directory where the data are
data_root_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print("Study Data Root Directory: ", data_root_dir, end='\n\n')


# remember where the program executed
program_dir = os.getcwd()

# change to the study data directory
os.chdir(data_root_dir)

# study's data folder name header
trial_data_dir = "user_study_excel_data"

# change to the study's data folder
os.chdir(trial_data_dir)

# open the workbooks containing the data
study_id = 1
win_size = 10.0

# first, open the activation workbook
activation_book_file_name = "study_%d (%.2fs).xls" % (study_id, win_size)
activation_book = xlrd.open_workbook(activation_book_file_name)

# open the survey sheet
activation_sheet = activation_book.sheet_by_name('Node Activation')

# second, read in the csv containing the snapshot
os.chdir(data_root_dir)
os.chdir("study_%d" % study_id)
snapshot_sheet = []
with open(glob.glob("cbla*.csv")[0]) as file:
    snapshot_reader = csv.reader(file)
    for row in snapshot_reader:
        snapshot_sheet.append(row)
