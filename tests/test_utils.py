import os
import sys

import pytest

ROOT_DIR = os.path.join(os.path.dirname(__file__), os.path.pardir)
MODULE_DIR = os.path.join(ROOT_DIR, "wordle_bot")
sys.path.insert(0, ROOT_DIR)

from wordle_bot.utils import check_guess, chunks


@pytest.mark.parametrize(
    "guess, answer, expected_output",
    [
        (
            "hello",
            "hello",
            ["+h", "+e", "+l", "+l", "+o"],
        ),
        (
            "cards",
            "sdarc",
            ["~c", "~a", "~r", "~d", "~s"],
        ),
        (
            "iiiii",
            "hello",
            ["-i", "-i", "-i", "-i", "-i"],
        ),
    ],
)
def test_check_guess(guess, answer, expected_output):
    assert check_guess(guess, answer) == expected_output


@pytest.mark.parametrize(
    "inp, expected_output",
    [
        (
            "-a-e-r-o-s",
            ["-a", "-e", "-r", "-o", "-s"],
        )
    ],
)
def test_chunks(inp, expected_output):
    assert list(chunks(inp)) == expected_output
