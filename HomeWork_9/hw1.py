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

    opened_files = {}
    for filename in file_list:
        file = open(filename, "r")
        opened_files[filename] = {"file": file}
        numb = next(opened_files[filename]["file"])
        if numb[:-1].isdigit():
            opened_files[filename]["numb"] = int(numb[:-1])
        else:
            raise ValueError("String is not a numb")

    while opened_files:
        current_file_manager_dict_to_take_numb = None
        for filename in opened_files:
            if current_file_manager_dict_to_take_numb is None:
                current_file_manager_dict_to_take_numb = filename
            elif (
                opened_files[filename]["numb"]
                < opened_files[current_file_manager_dict_to_take_numb]["numb"]
            ):
                current_file_manager_dict_to_take_numb = filename
        yield opened_files[current_file_manager_dict_to_take_numb]["numb"]
        try:
            numb = next(opened_files[current_file_manager_dict_to_take_numb]["file"])
            opened_files[current_file_manager_dict_to_take_numb]["numb"] = int(
                numb[:-1]
            )
        except StopIteration:
            opened_files[current_file_manager_dict_to_take_numb]["file"].close()
            del opened_files[current_file_manager_dict_to_take_numb]
        except ValueError:
            raise ValueError("String is not a numb")
