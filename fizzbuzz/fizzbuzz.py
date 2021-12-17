class Fizzbuzz:
    def fizzbuzz(self, number):
        result = ""
        if number % 3 == 0:
            result = "Fizz"
        if number % 5 == 0:
            result = result + "Buzz"
        if result == "":
            result = str(number)
        return result


class NumberRendering:
    def __init__(self, render):
        self.render = render

    def show_numbers(self, times, format_render):
        for i in range(times):
            self.render(format_render(i + 1))
