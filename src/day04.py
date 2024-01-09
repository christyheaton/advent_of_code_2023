class Card:
    def __init__(self, line: str):
        self.line = line
        self.data = self.parse_card()

    def parse_card(self) -> dict:
        winning_numbers = self.line.split(":")[1].split("|")[0].split()
        actual_numbers = self.line.split(":")[1].split("|")[1].split()
        return {"winning_numbers": winning_numbers, "actual_numbers": actual_numbers}

    def count_wins(self) -> int:
        return sum(
            num in self.data["winning_numbers"] for num in self.data["actual_numbers"]
        )

    def calculate_score(self) -> int:
        wins = self.count_wins()
        if wins > 2:
            score = 2 ** (wins - 1)
        else:
            score = wins
        return score


def main() -> None:
    with open("../data/day04.txt") as file:
        lines = [line.rstrip() for line in file]

    total_score = 0
    for line in lines:
        c = Card(line)
        total_score += c.calculate_score()
    print(f"Part 1: {total_score}")


if __name__ == "__main__":
    main()
