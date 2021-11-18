#!/usr/bin/env python3
"""The Crow's Nest"""

import argparse

def get_args():
    parser = argparse.ArgumentParser(description="The Crow's Nest")

    parser.add_argument('word', help='Any word')
    parser.add_argument('--starboard', metavar='starboard', default='larboard', help='changes the side to the right side of the boat. By default, it is set to larboard (left side of the boat)')

    return parser.parse_args()


def main():
    args = get_args()
    word = args.word
    side = args.starboard

    article = "an" if word[0].lower() in "aeiou" else "a"

    print(f"Ahoy, Captain, {article} {word} off the {side} bow!")


if __name__ == "__main__":
    main()