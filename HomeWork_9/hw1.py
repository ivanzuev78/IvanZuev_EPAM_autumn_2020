"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    opened_files = []
    for file in file_list:
        with open(file, "r") as f:
            opened_files.append(list(reversed(list(f))))

    while opened_files:
        current_list_to_take_numb = None
        current_list_index = None
        for index, numb_list in enumerate(opened_files):
            if current_list_to_take_numb is None:
                current_list_to_take_numb = opened_files[0]
                current_list_index = index
            elif int(numb_list[-1]) < int(current_list_to_take_numb[-1]):
                current_list_to_take_numb = numb_list
                current_list_index = index
        yield int(current_list_to_take_numb.pop(-1))
        if not current_list_to_take_numb:
            opened_files.pop(current_list_index)
