import unittest
from ..Tasks.task04 import check_sum_of_four


class MyTestCase(unittest.TestCase):
    def test_check_sum_of_four(self):

        input_1 = [-20, -30]
        input_2 = [20, 30]
        input_3 = [-100, -200]
        input_4 = [100, 200]

        self.assertEqual(check_sum_of_four(input_1, input_2, input_3, input_4), 4)


if __name__ == "__main__":
    unittest.main()
