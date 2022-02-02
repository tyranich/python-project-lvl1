#!usr/bin/env/ python3
from brain_games import engine
import random
from brain_games.games import brain_gcd


def main():
    engine.start_game(brain_gcd)


if __name__ == "__main__":
    main()
