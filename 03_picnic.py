#!/usr/bin/env python3
"""Picnic"""

import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Picnic')

    parser.add_argument('item', nargs='+', type=str, help="Item(s) to bring along")

    parser.add_argument('-s', '--sorted', action='store_true', help='Sorts the items (default: False)')

    parser.add_argument('-c', '--character', default=',', help='Character to be used to separate the items instead of the default comma. eg. -c ";" (make sure to put the character in quotes)')

    return parser.parse_args()


def main():
    args = get_args()
    item = args.item
    char = args.character

    if args.sorted:
        item.sort()

    if len(item) == 1:
        print(f'You are bringing {item[0]}.')
    elif len(item) == 2:
        print(f"You are bringing {item[0]} and {item[1]}.")
    else:
        print(f'You are bringing {char.join(item[0:-1])}{char} and {item[-1]}.')


if __name__ == "__main__":
    main()