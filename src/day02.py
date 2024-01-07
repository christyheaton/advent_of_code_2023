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

    def check_possible(self) -> bool:
        maximums = {"red": 12, "green": 13, "blue": 14}
        for r in self.rounds:
            for color in ["red", "green", "blue"]:
                if not r.get(color):
                    continue
                if maximums[color] < r[color]:
                    return False
        return True

    def get_game_power(self) -> int:
        minimums = {"red": 0, "green": 0, "blue": 0}
        for r in self.rounds:
            for color in ["red", "green", "blue"]:
                if not r.get(color):
                    continue
                if int(r[color]) > minimums[color]:
                    minimums[color] = int(r[color])

        product = 1

        for value in minimums.values():
            product *= value

        return product


def main() -> None:
    with open("../data/day02.txt") as file:
        lines = [line.rstrip() for line in file]

    possible_count = 0
    game_power_count = 0

    for line in lines:
        game = Game(line)
        if game.check_possible():
            possible_count += game.game_id
        power = game.get_game_power()
        game_power_count += power

    print(f"Part 1 solution: {possible_count}")
    print(f"Part 2 solution: {game_power_count}")


if __name__ == "__main__":
    main()
