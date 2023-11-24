import pytest
from main import split_word, calculate_score, generate_tiles


def test_split_word():
    assert split_word("GUARDIAN") == ["G", "U", "A", "R", "D", "I", "A", "N"]


def test_split_word_empty():
    assert split_word("") == []


def test_calculate_score():
    assert calculate_score(["G", "U", "A", "R", "D", "I", "A", "N"]) == 10


def test_calculate_score_empty():
    assert calculate_score([]) == 0


def test_generate_tiles_valid():
    BAG = {"E": 12, "A": 9, "I": 9, "O": 8, "N": 6, "R": 6, "T": 6, "L": 4, "S": 4, "U": 4, "D": 4, "G": 3, "B": 2,
           "C": 2, "M": 2, "P": 2, "F": 2, "H": 2, "V": 2, "W": 2, "Y": 2, "K": 1, "J": 1, "X": 1, "Q": 1, "Z": 1}

    generate_tiles(BAG)

    for value in BAG.values():
        assert int(value) >= 0
