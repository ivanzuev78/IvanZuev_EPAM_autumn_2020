import unittest

from HomeWork1.Tasks.task05 import find_maximal_subarray_sum


class TestTask03(unittest.TestCase):
    def setUp(self) -> None:
        self.example_array = [1, 3, -1, -3, 5, 3, 6, 7]

    def test_example(self):
        self.assertEqual(find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3), 16)


if __name__ == "__main__":
    unittest.main()
