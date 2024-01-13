class Card:
    def __init__(self, line: str):
        self.line = line
        self.id = int(self.line.split(":")[0].split()[1])
        self.data = self.parse_card()
        self.score = 0

    def __repr__(self) -> str:
        return f"{self.id}: {self.score}"

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
            self.score = 2 ** (wins - 1)
        else:
            self.score = wins
        return self.score


class CardCounter:
    def __init__(self, cards):
        self.cards = cards
        self.card_counts = {}
        self.get_initial_card_counts()

    def get_initial_card_counts(self) -> None:
        for card in self.cards:
            self.card_counts[int(card.id)] = 1

    def count_cards(self) -> int:
        for card in self.cards:
            wins = card.count_wins()
            for i in range(card.id+1, card.id+wins+1):
                self.card_counts[i] += self.card_counts[card.id]
        return sum(self.card_counts.values())


def main() -> None:
    with open("../data/day04.txt") as file:
        lines = [line.rstrip() for line in file]

    cards = []
    total_score = 0
    for line in lines:
        c = Card(line)
        cards.append(c)
        total_score += c.calculate_score()
    print(f"Part 1: {total_score}")

    counter = CardCounter(cards)
    print(f"Part 2: {counter.count_cards()}")


if __name__ == "__main__":
    main()
