import unittest
from task2 import rev


class Test(unittest.TestCase):
    def true_pal(self):
        """
        True palindrome test 1
        """
        a = 'mamamamamam'
        self.assertTrue(rev(a))

        """
        True palindrome test 2
        """
        a = 'ma a m a am'
        self.assertTrue(rev(a))

    def false_pal(self):
        """
        False palindrome test 1
        """
        a = 'mama'
        self.assertFalse(rev(a))

        """
        False palindrome test 2
        """
        a = 'a mmama m mama'
        self.assertFalse(rev(a))
