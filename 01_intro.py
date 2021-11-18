#!/usr/bin/env python3
"""
Purpose: Say Hello
"""

import argparse

def get_args():
    # figures out all the arguments. displays the desciption in the help
    parser = argparse.ArgumentParser(description='Say Hello')
    # parser.add_argument('name', help='Name to greet') # required/positional argument(s) to be parsed to the program

    # to make arguments optional and display some default value
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')

    return parser.parse_args() # returns the parsed arguments


def main():
    args = get_args() # gets the args from get_args() and parses it to the program
    print(f'Hello, {args.name}!') # prints the value of the parsed to the name argument


if __name__ == '__main__':
    main()