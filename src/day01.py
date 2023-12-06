from collections import OrderedDict
from word2number import w2n


def find_digits(input_str: str) -> int:
    nums = [i for i in input_str if i.isdigit()]
    return int(nums[0] + nums[-1])


def find_digits_or_spelled(input_str: str):
    arr = [
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
        arr.append(str(i))
    temp_result = [ele for ele in arr if ele in input_str]
    order_tracking = {}
    for item in temp_result:
        order_tracking[input_str.find(item)] = item
    sorted_dict = OrderedDict(sorted(order_tracking.items()))

    print(sorted_dict)
    return temp_result


def main():
    with open("../data/day01_test_pt1.txt") as file:
        lines = [line.rstrip() for line in file]
    count = 0
    for line in lines:
        digits = find_digits(line)
        count += digits
    print(f"Part 1 solution: {count}.")

    # for line in lines:
        # print(line)
        # find_digits_or_spelled(line)
    # print(f"Part 2 solution: {count}.")


if __name__ == "__main__":
    main()
