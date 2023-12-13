

def check_possible(input_str: str) -> bool:
    """
    Check if the game is possible under the conditions
    :param input_str: several games
    :return: True if the game is possible, otherwise False
    """
    maximums = {"red": 12, "green": 13, "blue": 14}

    games = input_str.split(": ")[1:]
    for game in games:
        rounds = game.split(";")
        for r in rounds:
            cubes = r.split(",")
            for cube in cubes:
                count, color = cube.split()
                if maximums[color] < int(count):
                    return False
    return True


def main() -> None:
    with open("../data/day02.txt") as file:
        lines = [line.rstrip() for line in file]

    count = 0
    for line in lines:
        game_id = int((line.split(":")[0].split()[-1]))
        if check_possible(line):
            count += game_id
    print(f"Part 1 solution: {count}")


if __name__ == "__main__":
    main()
