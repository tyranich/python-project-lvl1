#!/usr/bin/env python3
from brain_games import engine
import random
from brain_games.games import brain_calc
import sys


def main():
    engine.start_game(brain_calc)


if __name__ == "__main__":
    main()
