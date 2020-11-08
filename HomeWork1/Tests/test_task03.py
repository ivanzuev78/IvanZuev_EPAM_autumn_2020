import os
import unittest
from typing import Sequence

from HomeWork1.Tasks.task03 import find_maximum_and_minimum


class TestTask03(unittest.TestCase):

    files = []

    def file_maker(self, sequence: Sequence[int], filename: str) -> None:

        with open(filename, "w") as f:
            for i in sequence:
                f.write(f"{i}\n")

        self.files.append(filename)

    def setUp(self) -> None:

        self.file_maker([i for i in range(4)], "data_test_task03_min1_max9.txt")

        self.file_maker(
            [i for i in range(2)] + [-10] + [i + 10 for i in range(2)],
            "data_test_task03_min-10_max19.txt",
        )

        self.file_maker([1 for _ in range(3)], "data_test_task03_min1_max1.txt")

    def test_find_maximum_and_minimum(self):

        self.assertEqual(
            find_maximum_and_minimum("data_test_task03_min1_max9.txt"), (1, 3)
        )
        self.assertEqual(
            find_maximum_and_minimum("data_test_task03_min-10_max19.txt"), (-10, 11)
        )
        self.assertEqual(
            find_maximum_and_minimum("data_test_task03_min1_max1.txt"), (1, 1)
        )

    def test_find_maximum_and_minimum_empty_input(self):

        self.file_maker([], "data_test_task03_empty_input.txt")

        self.assertEqual(
            find_maximum_and_minimum("data_test_task03_empty_input.txt"), (None, None)
        )

    def tearDown(self) -> None:
        for file in self.files:
            os.remove(file)


if __name__ == "__main__":
    unittest.main()
