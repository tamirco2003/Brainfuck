from bf_cmds import *
import argparse
import sys
import re

CODE_REGEX = r'[><+\-.,[\]]'

cmds = {
    '>': forward,
    '<': backward,
    '+': inc,
    '-': dec,
    '.': out,
    ',': inp,
    '[': loop_start,
    ']': loop_end
}


def main_interpreter(filepath, size):
    fixed_size = bool(size)
    brackets = {}

    mem = [0 for _ in range(size or 30000)]
    index = 0

    code = get_code(filepath)
    ip = 0

    output = []

    generate_bracket_locations(code, brackets)

    try:
        while ip < len(code):
            index, ip = execute(code, fixed_size, mem,
                                index, ip, output, brackets)
    except Exception as err:
        print(err)
        print(ip)

    print(''.join(output), end='')
    print('\nDone!')


def get_code(filepath):
    """
    Takes filepath, returns only code.
    """
    with open(filepath, 'r') as source:
        data = source.read()
        return re.findall(CODE_REGEX, data)


def generate_bracket_locations(code, brackets):
    """
    Scans the code for brackets and stores the pairs' locations.
    """
    stack = []
    for code_index in range(len(code)):
        cmd = code[code_index]
        if cmd == '[':
            stack.append(code_index + 1)
        elif cmd == ']':
            open_loc = stack.pop()
            brackets[open_loc] = code_index + 1
            brackets[code_index + 1] = open_loc


def execute(code, fixed, mem, i, ip, output, brackets):
    """
    Interprets a single brainfuck command.
    """
    return cmds[code[ip]](fixed, mem, i, ip, output, brackets)


def main():
    parser = argparse.ArgumentParser(description='Brainfuck interpreter')
    parser.add_argument('path', metavar='path', type=str,
                        help='path to brainfuck file')
    parser.add_argument('-s', '--size', type=int,
                        help='use for fixed memory size')

    args = parser.parse_args()

    main_interpreter(args.path, args.size)


if __name__ == '__main__':
    main()
