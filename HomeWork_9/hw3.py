import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(
    dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    """
    Write a function that takes directory path, a file extension and an optional tokenizer.
    It will count lines in all files with that extension if there are no tokenizer.
    If a the tokenizer is not none, it will count tokens.
    """
    current_dir = os.getcwd()
    os.chdir(dir_path)
    counter = 0
    for file in os.listdir():
        if Path(file).suffix == file_extension:
            with open(file, "r") as f:
                if tokenizer:
                    counter += len(tokenizer(f.read()))
                else:
                    counter += sum(1 for _ in f)

    os.chdir(current_dir)
    return counter
