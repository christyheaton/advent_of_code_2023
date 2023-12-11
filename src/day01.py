from collections import OrderedDict

from word2number import w2n


def find_first_last_digits(input_str: str) -> int:
    """
    :param input_str: a string containing at least one digit
    :return: the fist and last digits in the input_str
    """
    nums = [i for i in input_str if i.isdigit()]
    return int(nums[0] + nums[-1])


def get_number_list() -> list[str]:
    """
    :return: a list of numbers relevant to this challenge
    """
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for i in range(10):
        nums.append(str(i))
    return nums


def find_first_last_digits_or_spelled(input_str: str) -> int:
    """
    :param input_str: a string containing at least one digit or spelled out number
    :return: the fist and last numbers in the input_str
    """
    arr = get_number_list()
    temp_result = [ele for ele in arr if ele in input_str]
    order_tracking = {}
    for item in temp_result:
        order_tracking[input_str.find(item)] = item
        order_tracking[input_str.rfind(item)] = item
    sorted_dict = OrderedDict(sorted(order_tracking.items()))
    for k, v in sorted_dict.items():
        sorted_dict[k] = w2n.word_to_num(v)
    listed_items = list(sorted_dict.items())
    result = int(str(listed_items[0][-1]) + str(listed_items[-1][-1]))
    return result


def main() -> None:
    with open("../data/day01_input.txt") as file:
        lines = [line.rstrip() for line in file]

    pt1_count = 0
    for line in lines:
        pt1_count += find_first_last_digits(line)
    print(f"Part 1 solution: {pt1_count}.")

    pt2_count = 0
    for line in lines:
        pt2_count += find_first_last_digits_or_spelled(line)
    print(f"Part 2 solution: {pt2_count}.")


if __name__ == "__main__":
    main()
