import random

HAND_SIZE = 7

BAG = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2,
       "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}


def split_word(word: str) -> list[str]:
    return [letter.capitalize() for letter in word]


def calculate_score(letters: list[str]) -> int:
    score = 0
    for letter in letters:
        if letter in ["E", "A", "I", "O", "N", "R", "T", "L", "S", "U"]:
            score += 1

        elif letter in ["D", "G"]:
            score += 2

        elif letter in ["B", "C", "M", "P"]:
            score += 3

        elif letter in ["F", "H", "V", "W", "Y"]:
            score += 4

        elif letter in ["K"]:
            score += 5

        elif letter in ["J", "X"]:
            score += 8

        elif letter in ["Q", "Z"]:
            score += 10

    return score


def generate_tiles(bag: list[str]) -> list[str]:
    hand = []
    for i in range(HAND_SIZE):
        picking_letter = True

        while picking_letter is True:
            random_number = random.randint(0, len(bag) - 1)
            letter = list(bag.keys())[random_number]

            if bag[letter] > 0:
                picking_letter = False

        hand.append(letter)
        bag[letter] -= 1

    return hand


def main():
    letters = split_word("GUARDIAN")
    calculate_score(letters)
    print(generate_tiles(BAG))


if __name__ == "__main__":
    main()
