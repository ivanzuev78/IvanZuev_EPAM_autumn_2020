import unittest
from HomeWork1.Tasks.task02 import check_fibonacci


class TestTask02(unittest.TestCase):

    def setUp(self) -> None:
        self.empty_sequence = []
        self.sequence_len1_true = [0]
        self.sequence_len1_true_2 = [1]
        self.sequence_len1_false = [2]
        self.sequence_len2_true = [0, 1]
        self.sequence_len2_true_2 = [1, 1]
        self.sequence_len2_false = [1, 2]
        self.sequence_len3_true = [ 0, 1, 1]
        self.sequence_len3_true_2 = [1, 1, 2]
        self.sequence_true = [1, 1, 2, 3, 5, 8]
        self.sequence_true_2 = [1, 1, 2, 3, 5]
        self.sequence_false = [i for i in range(10)]
        self.sequence_false_2 = [1, 1, 2, 3, 5, 7]

    def test_empty_sequence(self):
        self.assertEqual(check_fibonacci(self.empty_sequence), False)

    def test_sequence_len_1(self):
        self.assertEqual(check_fibonacci(self.sequence_len1_true), True)
        self.assertEqual(check_fibonacci(self.sequence_len1_true_2), True)
        self.assertEqual(check_fibonacci(self.sequence_len1_false), False)

    def test_sequence_len_2(self):
        self.assertEqual(check_fibonacci(self.sequence_len2_true), True)
        self.assertEqual(check_fibonacci(self.sequence_len2_true_2), True)
        self.assertEqual(check_fibonacci(self.sequence_len2_false), False)

    def test_sequence_len_3(self):
        self.assertEqual(check_fibonacci(self.sequence_len3_true), True)
        self.assertEqual(check_fibonacci(self.sequence_len3_true_2), True)

    def test_sequence_len_more_than_3(self):
        self.assertEqual(check_fibonacci(self.sequence_true), True)
        self.assertEqual(check_fibonacci(self.sequence_true_2), True)
        self.assertEqual(check_fibonacci(self.sequence_false), False)
        self.assertEqual(check_fibonacci(self.sequence_false_2), False)



if __name__ == '__main__':
    unittest.main()
