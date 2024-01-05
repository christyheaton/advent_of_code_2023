class Game:
    def __init__(self, line: str):
        self.game_id = int((line.split(":")[0].split()[-1]))
        game_data = line.split(": ")[1]
        self.round_data = game_data.split(";")
        self.rounds = []
        self.parse_round()

    def parse_round(self):
        for r in self.round_data:
            round_dict = {}
            cubes = r.split(",")
            for cube in cubes:
                count, color = cube.split()
                round_dict[color] = int(count)
            self.rounds.append(round_dict)


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


def get_game_power(input_str: str) -> int:
    """
    Get game power using minimum number of each color
    :param input_str: multiple games
    :return: power value of all games in set
    """
    minimums = {"red": 0, "green": 0, "blue": 0}
    games = input_str.split(": ")[1:]
    for game in games:
        rounds = game.split(";")
        for r in rounds:
            cubes = r.split(",")
            for cube in cubes:
                count, color = cube.split()
                if int(count) > minimums[color]:
                    minimums[color] = int(count)
    product = 1

    for value in minimums.values():
        product *= value

    return product


def main() -> None:
    with open("../data/day02.txt") as file:
        lines = [line.rstrip() for line in file]

    for line in lines:
        game = Game(line)
        print(game.game_id)
        print(game.rounds)

    count = 0
    for line in lines:
        game_id = int((line.split(":")[0].split()[-1]))
        if check_possible(line):
            count += game_id
    print(f"Part 1 solution: {count}")

    count = 0
    for line in lines:
        power = get_game_power(line)
        count += power
    print(f"Part 2 solution: {count}")


if __name__ == "__main__":
    main()
