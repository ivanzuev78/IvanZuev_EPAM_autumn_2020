import os
import unittest

from HomeWork1.Tasks.task03 import find_maximum_and_minimum


class TestTask03(unittest.TestCase):
    def setUp(self) -> None:

        with open("data_test_task03_min1_max9.txt", "w") as f:
            for i in range(10):
                f.write(f"{i}\n")

        with open("data_test_task03_min-10_max19.txt", "w") as f:
            for i in range(10):
                f.write(f"{i}\n")
            f.write(f"-10\n")
            for i in range(10):
                f.write(f"{i+10}\n")

        with open("data_test_task03_min1_max1.txt", "w") as f:
            for i in range(10):
                f.write(f"1\n")

    def test_find_maximum_and_minimum(self):
        self.assertEqual(
            find_maximum_and_minimum("data_test_task03_min1_max9.txt"), (1, 9)
        )
        self.assertEqual(
            find_maximum_and_minimum("data_test_task03_min-10_max19.txt"), (-10, 19)
        )
        self.assertEqual(
            find_maximum_and_minimum("data_test_task03_min1_max1.txt"), (1, 1)
        )

    def tearDown(self) -> None:
        os.remove("data_test_task03_min1_max9.txt")
        os.remove("data_test_task03_min-10_max19.txt")
        os.remove("data_test_task03_min1_max1.txt")


if __name__ == "__main__":
    unittest.main()
