from fizzbuzz import Fizzbuzz
from fizzbuzz import NumberRendering
import unittest


class FizzBuzzTestCase(unittest.TestCase):
    """Unittests for FizzBuzz"""

    def test_return_number_for_integer(self):
        self.assertEqual(Fizzbuzz().fizzbuzz(2), "2")

    def test_return_fizz_for_3(self):
        self.assertEqual(Fizzbuzz().fizzbuzz(3), "Fizz")

    def test_retunr_fizz_for_multiple_of_3(self):
        self.assertEqual(Fizzbuzz().fizzbuzz(9), "Fizz")

    def test_return_buzz_for_5(self):
        self.assertEqual(Fizzbuzz().fizzbuzz(5), "Buzz")

    def test_return_fizzbuzz_for_multiple_of_3_and_5(self):
        self.assertEqual(Fizzbuzz().fizzbuzz(15), "FizzBuzz")


class NumberRenderingTestCase(unittest.TestCase):
    """Unittests for NumberRendering"""

    def setUp(self):
        self.render_count = 0
        self.render_txt = ""
        self.number_rendering = NumberRendering(self.dummy_render)

    def dummy_render(self, txt):
        self.render_count = self.render_count + 1

    def dummy_display(self, number):
        self.render_txt = str(number) + "txt"

    def test_can_render_many_numbers(self):
        self.number_rendering.show_numbers(times=2, format_render=self.dummy_display)
        self.assertEqual(2, self.render_count)

    def test_can_render_right_text(self):
        self.number_rendering.show_numbers(times=1, format_render=self.dummy_display)
        self.assertEqual("1txt", self.render_txt)

    def test_fizzbuzz(self):
        number_rendering = NumberRendering(print)
        number_rendering.show_numbers(100, Fizzbuzz().fizzbuzz)
