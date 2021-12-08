from unittest import TestCase
from fake_package.fake_class_sum import class_sum
from fake_package.fake_class_multiply import class_multiply


class TestsSumMultiply(TestCase):
    def setUp(self):
        self.x = 2
        self.y = 3
        self.summer = class_sum(self.x, self.y)
        self.multiplier = class_multiply(self.x, self.y)
        self.sum_result = self.x + self.y
        self.multiply_result = self.x * self.y

    def tearDown(self) -> None:
        return super().tearDown()

    def test_sum(self):
        self.assertEqual(self.summer.summed, self.sum_result)

    def test_sum2(self):
        self.assertEqual(self.summer.sum(self.x, self.y), self.sum_result)

    def test_multiply(self):
        self.assertEqual(self.multiplier.multiplied, self.multiply_result)

    def test_multiply2(self):
        self.assertEqual(self.multiplier.multiply(self.x, self.y), self.multiply_result)
