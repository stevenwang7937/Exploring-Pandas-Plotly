import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_zero_k(self):
        """ k equals zero """

        nums = [1, 2, 3, 4, 5, 6]
        k = 0
        nums_expected = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, k)

        self.assertEqual(nums, nums_expected)


    def test_one_k(self):
        """ k equals one """

        nums = [1, 2, 3, 4, 5, 6]
        k = 1
        nums_expected = [6, 2, 3, 4, 5, 1]
        a1.swap_k(nums, k)

        self.assertEqual(nums, nums_expected)


    def test_even_max_k(self):
        """ length of list is even and k equals max value """

        nums = [1, 2, 3, 4, 5, 6]
        k = 3
        nums_expected = [4, 5, 6, 1, 2, 3]
        a1.swap_k(nums, len(nums) // 2)

        self.assertEqual(nums, nums_expected)


    def test_odd_max_k(self):
        """ length of list is odd and k equals max value """

        nums = [1, 2, 3, 4, 5]
        k = 2
        nums_expected = [4, 5, 3, 1, 2]
        a1.swap_k(nums, len(nums) // 2)

        self.assertEqual(nums, nums_expected)    


if __name__ == '__main__':
    unittest.main(exit=False)
