import argparse


def has_upper(password):
    if True in [symbol.islower() for symbol in password]:
        return 1
    return 0


def has_lower(password):
    if True in [symbol.isupper() for symbol in password]:
        return 1
    return 0


def has_digit(password):
    if True in [symbol.isdigit() for symbol in password]:
        return 1
    return 0


def has_special_characters(password, special_characters):
    if True in [symbol in special_characters for symbol in password]:
        return 1
    return 0


def length_check(password):
    length_password = len(password)
    min_length = 5
    normal_length = 8
    long_len = 10
    if length_password < min_length:
        return 0
    elif (min_length <= length_password) and (length_password < normal_length):
        return 1
    elif (normal_length <= length_password) and (length_password < long_len):
        return 2
    else:
        return 3


def is_password_in_black_list(password, black_list):
    return 0 if password in black_list else 3


def get_password_strength(password, black_list):
    return sum([
        has_upper(password),
        has_lower(password),
        has_digit(password),
        has_special_characters(password,
                               """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""),
        length_check(password),
        is_password_in_black_list(password, black_list)
    ])


def load_black_list(path):
    with open(path, "r") as untreated_file:
        black_list = list(untreated_file.read().splitlines())
        return black_list


def get_parser_args():
    parser = argparse.ArgumentParser(
        description="Path to the black list"
    )
    parser.add_argument(
        "path",
        default="password.lst",
        nargs="?",
        help="Input path to the black list"
    )
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    try:
        argument = get_parser_args()
        black_list = load_black_list(argument.path)
        password = input('Input user password: ')
        password_strength = get_password_strength(password, black_list)
        print("strength your password: {}".format(password_strength))
    except FileNotFoundError:
        print("Error: file '{}' not found".format(argument.path))
