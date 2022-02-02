#!/usr/bin/env python3
import random
from brain_games import engine
from brain_games.games import brain_even


def main():
    engine.start_game(brain_even)


if __name__ == '__main__':
    main()
