from unittest import TestCase, TestLoader, TextTestRunner

points = {
        'both_positive': 0,
        'first_negative_second_positive': 0,
        'first_positive_second_negative': 0,
        'both_negative': 0,
        'first_is_zero': 0,
        'second_is_zero': 0,
        'both_zero': 0,
        'first_is_decimal': 0,
        'second_is_decimal': 0,
        'both_decimal': 0,
        'first_is_big': 0,
        'second_is_big': 0,
        'both_big': 0,
        'first_is_small': 0,
        'second_is_small': 0,
        'both_small': 0,
    }


def multiply(a, b):
    global points

    points['both_positive'] = 1 if a > 0 and b > 0 else points.get('both_positive', 0)
    points['first_negative_second_positive'] = 1 if a < 0 and b > 0 else points.get('first_negative_second_positive', 0)
    points['first_positive_second_negative'] = 1 if a > 0 and b < 0 else points.get('first_positive_second_negative', 0)
    points['both_negative'] = 1 if a < 0 and b < 0 else points.get('both_negative', 0)
    points['first_is_zero'] = 1 if a == 0 and b != 0 else points.get('first_is_zero', 0)
    points['second_is_zero'] = 1 if a != 0 and b == 0 else points.get('second_is_zero', 0)
    points['both_zero'] = 1 if a == 0 and b == 0 else points.get('both_zero', 0)
    points['first_is_decimal'] = 1 if isinstance(a, float) and isinstance(b, int) else points.get('first_is_decimal', 0)
    points['second_is_decimal'] = 1 if isinstance(a, int) and isinstance(b, float) else points.get('second_is_decimal', 0)
    points['both_decimal'] = 1 if isinstance(a, float) and isinstance(b, float) else points.get('both_decimal', 0)
    points['first_is_big'] = 1 if abs(a) > 1000 and abs(b) < 1000 else points.get('first_is_big', 0)
    points['second_is_big'] = 1 if abs(a) < 1000 and abs(b) > 1000 else points.get('second_is_big', 0)
    points['both_big'] = 1 if abs(a) > 1000 and abs(b) > 1000 else points.get('both_big', 0)
    points['first_is_small'] = 1 if abs(a) < 1 and abs(b) > 1 else points.get('first_is_small', 0)
    points['second_is_small'] = 1 if abs(a) > 1 and abs(b) < 1 else points.get('second_is_small', 0)
    points['both_small'] = 1 if abs(a) < 1 and abs(b) < 1 else points.get('both_small', 0)

    return a * b


# region Task
class TestMultiply(TestCase):
    def test_both_positive(self):
        a, b = 4, 2
        answer = 8
        self.assertEqual(multiply(a, b), answer)

    def test_first_negative_second_positive(self):
        a, b = -4, 2
        answer = -8
        self.assertEqual(multiply(a, b), answer)

    def test_first_positive_second_negative(self):
        a, b = 4, -2
        answer = -8
        self.assertEqual(multiply(a, b), answer)

    def test_both_negative(self):
        a, b = -4, -2
        answer = 8
        self.assertEqual(multiply(a, b), answer)

    def test_first_is_zero(self):
        a, b = 0, -2
        answer = 0
        self.assertEqual(multiply(a, b), answer)

    def test_second_is_zero(self):
        a, b = -2, 0
        answer = 0
        self.assertEqual(multiply(a, b), answer)

    def test_both_zero(self):
        a, b = 0, 0
        answer = 0
        self.assertEqual(multiply(a, b), answer)

    def test_first_is_decimal(self):
        a, b = 1.5, -2
        answer = -3
        self.assertEqual(multiply(a, b), answer)

    def test_second_is_decimal(self):
        a, b = 2, -1.5
        answer = -3
        self.assertEqual(multiply(a, b), answer)

    def test_both_decimal(self):
        a, b = 2.5, 1.2
        answer = 3
        self.assertEqual(multiply(a, b), answer)

    def test_first_is_big(self):
        a, b = 10**9, 10
        answer = 10000000000
        self.assertEqual(multiply(a, b), answer)

    def test_second_is_big(self):
        a, b = 10, -10**9
        answer = -10000000000
        self.assertEqual(multiply(a, b), answer)

    def test_both_big(self):
        a, b = 10**9, -10**9
        answer = -1000000000000000000
        self.assertEqual(multiply(a, b), answer)

    def test_first_is_small(self):
        a, b = 10**(-9), 10
        answer = 0.00000001
        self.assertEqual(multiply(a, b), answer)

    def test_second_is_small(self):
        a, b = -10, 10**(-9)
        answer = -0.00000001
        self.assertEqual(multiply(a, b), answer)

    def test_both_small(self):
        a, b = -10**(-9), -10**(-9)
        answer = 0.000000000000000001
        self.assertEqual(multiply(a, b), answer)
# endregion


loader = TestLoader()
suite = loader.loadTestsFromTestCase(TestMultiply)
runner = TextTestRunner()
result = runner.run(suite)

if result.wasSuccessful():
    if sum(points.values()) == len(points):
        print('{"verdict": \'Ok\'}')
    else:
        print(f'{{"verdict": \'WrongAnswer\', \'error\': \'Не все случаи покрыты тестами. {sum(points.values())} / {len(points)}\'}}')