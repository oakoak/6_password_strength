import argparse
from getpass import getpass
from string import punctuation
from os.path import isfile


def has_upper(password):
    return any([symbol.isupper() for symbol in password])


def has_lower(password):
    return any([symbol.islower() for symbol in password])


def has_digit(password):
    return any([symbol.isdigit() for symbol in password])


def has_special_characters(password):
    return any([symbol in punctuation for symbol in password])


def check_length(password):
    length_password = len(password)
    min_length = 5
    normal_length = 8
    long_len = 10
    if length_password < min_length:
        return 0
    elif min_length <= length_password < normal_length:
        return 1
    elif normal_length <= length_password < long_len:
        return 2
    else:
        return 3


def is_password_in_black_list(password, black_list):
    return password not in black_list


def get_password_strength(password, black_list):
    return sum([
        has_upper(password),
        has_lower(password),
        has_digit(password),
        has_special_characters(password),
        check_length(password),
        is_password_in_black_list(password, black_list)*3
    ])


def load_black_list(path):
    with open(path, "r") as untreated_file:
        black_list = untreated_file.read().splitlines()
        return black_list


def get_parser_args():
    parser = argparse.ArgumentParser(
        description="Path to the black list"
    )
    parser.add_argument(
        "path",
        nargs="?",
        help="Input path to the black list"
    )
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    argument = get_parser_args()
    if argument.path is None or not isfile(argument.path):
        print("file with the name of the '{}' is not found, the blacklist is empty".format(argument.path))
        black_list = []
    else:
        black_list = load_black_list(argument.path)

    password = getpass()
    password_strength = get_password_strength(password, black_list)
    print("Strength your password: {}".format(password_strength))
