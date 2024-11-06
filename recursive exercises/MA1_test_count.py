# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import count


class Test(unittest.TestCase):

    def test_count(self):
        print('\nTests count')

        # Test 1: tom lista
        self.assertEqual(count(1, []), 0)
        self.assertEqual(count(1, [[]]), 0)
        self.assertEqual(count(1, [[], []]), 0)

        # Test 2: första, sista och inuti lista
        self.assertEqual(count(1, [1, 2, 3]), 1)
        self.assertEqual(count(2, [1, 2, 2, 3]), 2)
        self.assertEqual(count(3, [1, 2, [3], 3, 3]), 3)

        # Test 3: leta efter en lista
        self.assertEqual(count([2], [1, [2], 3]), 1)
        self.assertEqual(count([2, 3], [[2, 3], 4, 5]), 1)
        self.assertEqual(count([2], [[2], [2], [2]]), 3)

        # Test 4: leta i sublists
        self.assertEqual(count(1, [1, [1, [1, 2], 2], 3]), 3)
        self.assertEqual(count(2, [1, [2, [2, 3], 2], 2]), 4)

        # Test 5: leta efter ickeexisterande element
        self.assertEqual(count(4, [1, 2, 3]), 0)
        self.assertEqual(count(5, [1, [2, 3], [4]]), 0)

        # Test 6: kolla så att listan inte förstörs
        list = [1, [2, 3,[2,3,1]], 4]
        count(3, list)
        self.assertEqual(list, [1, [2, 3,[2,3,1]], 4])


if __name__ == "__main__":
    unittest.main()