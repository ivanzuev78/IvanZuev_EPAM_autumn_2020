import unittest

from HomeWork1.Tasks.task02 import check_fibonacci


class TestTask02(unittest.TestCase):

    def test_empty_sequence(self):

        empty_sequence = []

        self.assertEqual(check_fibonacci(empty_sequence), False)

    def test_sequence_len_1(self):

        sequence_len1_true = [0]
        sequence_len1_true_2 = [1]
        sequence_len1_false = [2]

        self.assertEqual(check_fibonacci(sequence_len1_true), True)
        self.assertEqual(check_fibonacci(sequence_len1_true_2), True)
        self.assertEqual(check_fibonacci(sequence_len1_false), False)

    def test_sequence_len_2(self):

        sequence_len2_true = [0, 1]
        sequence_len2_true_2 = [1, 1]
        sequence_len2_false = [1, 2]

        self.assertEqual(check_fibonacci(sequence_len2_true), True)
        self.assertEqual(check_fibonacci(sequence_len2_true_2), True)
        self.assertEqual(check_fibonacci(sequence_len2_false), False)

    def test_sequence_len_3(self):

        sequence_len3_true = [0, 1, 1]
        sequence_len3_true_2 = [1, 1, 2]

        self.assertEqual(check_fibonacci(sequence_len3_true), True)
        self.assertEqual(check_fibonacci(sequence_len3_true_2), True)

    def test_sequence_len_more_than_3(self):

        sequence_true = [1, 1, 2, 3, 5, 8]
        sequence_true_2 = [1, 1, 2, 3, 5]
        sequence_false = [i for i in range(10)]
        sequence_false_2 = [1, 1, 2, 3, 5, 7]

        self.assertEqual(check_fibonacci(sequence_true), True)
        self.assertEqual(check_fibonacci(sequence_true_2), True)
        self.assertEqual(check_fibonacci(sequence_false), False)
        self.assertEqual(check_fibonacci(sequence_false_2), False)


if __name__ == "__main__":
    unittest.main()
