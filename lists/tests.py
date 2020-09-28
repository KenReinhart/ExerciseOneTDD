from django.test import TestCase #augmented version of the standard unittest.TestCase.
#import unittest
class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)