# File Operations
#
# You will want to use veidenbaums.txt for analysis. It is in the class git repository under Day12_File_Operations
# folder You can also download it directly from the following link:

# https://raw.githubusercontent.com/ValRCS/Python_TietoEvry_Sep2021/main/Day12_File_Operations/veidenbaums.txt
#
# 1a -> write the function file_line_len(fpath), which returns the number of lines in the file
#
# check file_line_len ("veidenbaums.txt") -> should be 971 or 972

import os  # system library
import string
from datetime import datetime as dt  # datetime has datetime submodule(klase)
from pathlib import Path  # this is newer for path manipulation


# a recommended approach is to use a context manager
def file_line_len(fpath):
    with open(fpath, encoding="utf-8") as fstream:
        lines = fstream.readlines()  # reads all lines defined with newline
    return len(lines)


print(file_line_len("veidenbaums.txt"))
