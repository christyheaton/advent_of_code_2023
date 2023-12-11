import pytest

from src.day01 import find_first_last_digits, find_first_last_digits_or_spelled


@pytest.mark.parametrize(
    "test_input,expected",
    [("1abc2", 12), ("pqr3stu8vwx", 38), ("a1b2c3d4e5f", 15), ("treb7uchet", 77)],
)
def test_part1(test_input: str, expected: int) -> None:
    """
    :param test_input: a sample input
    :param expected: the expected result
    :return:
    """
    assert find_first_last_digits(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_part2(test_input: str, expected: int) -> None:
    """
    :param test_input: a sample input
    :param expected: the expected result
    :return:
    """
    assert find_first_last_digits_or_spelled(test_input) == expected
