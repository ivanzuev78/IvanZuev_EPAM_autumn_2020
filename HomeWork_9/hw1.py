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
    def read_next_numb_from_file(file_manager_dict: dict) -> dict:
        with open(file_manager_dict["filename"], "r") as f:
            f.seek(file_manager_dict["cursor_position"])
            numb = f.readline()
            if numb[:-1].isdigit():
                file_manager_dict["numb"] = int(numb)
            else:
                file_manager_dict["numb"] = None
            file_manager_dict["cursor_position"] = f.tell()
            return file_manager_dict

    opened_files = {}
    for file in file_list:
        opened_files[file] = read_next_numb_from_file(
            {"filename": file, "cursor_position": 0, "numb": None}
        )

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
        opened_files[current_file_manager_dict_to_take_numb] = read_next_numb_from_file(
            opened_files[current_file_manager_dict_to_take_numb]
        )
        if opened_files[current_file_manager_dict_to_take_numb]["numb"] is None:
            del opened_files[current_file_manager_dict_to_take_numb]
