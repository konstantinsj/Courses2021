# File Operations
#
# You will want to use veidenbaums.txt for analysis. It is in the class git repository under Day12_File_Operations
# folder You can also download it directly from the following link:

# https://raw.githubusercontent.com/ValRCS/Python_TietoEvry_Sep2021/main/Day12_File_Operations/veidenbaums.txt
#
# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
#
# check file_line_len ("veidenbaums.txt") -> should be 971 or 972
# a recommended approach is to use a context manager


import os  # system library
import string
from datetime import datetime as dt  # datetime has datetime submodule(klase)
from pathlib import Path  # this is newer for path manipulation


def file_line_len(fpath):
    with open(fpath, encoding="utf-8") as fstream:
        lines = fstream.readlines()  # reads all lines defined with newline
    return len(lines)


print(file_line_len("veidenbaums.txt"))

# 1b -> write the function get_poem_lines (fpath),
# which returns a list with only those lines that contain poetry.
# So we want to avoid/filter out those lines that contain whitespace and also those lines with poem titles.
#
# PS preferably use encoding = "utf-8"

def get_poem_lines(fpath):
    with open(fpath, encoding="utf-8") as fstream:
        lines = (line.rstrip() for line in fstream if
                 not line.__contains__("***"))  # getting rid of whitespace and *** lines
        lines = list(line for line in lines if line)
        return lines


print(get_poem_lines("veidenbaums.txt"))
