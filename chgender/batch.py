import argparse
from chgender import guess
import os


def main():
    parser = argparse.ArgumentParser(
        description='Gender guesser for Chinese names in English(pinyin) form')

    group = parser.add_mutually_exclusive_group()
    group.add_argument('-n', '--fnames', nargs='+', help='read first names from arguments')
    group.add_argument('-f',  '--file', nargs=1, help='read first or full names from file(abs dir)')

    parser.add_argument('-v', '--version', action='version', version='chgender_0.0..1')

    args = parser.parse_args()

    if args.fnames:
        for name in args.fnames:
            gender, prob = guess(name)
            print('name: {} => gender: {}, probability: {}'
              ''.format(name, gender, prob))
    elif args.file:
        with open(args.file[0], 'r') as f:
            for name in f:
                name = name.strip('\n')
                gender, prob = guess(name)
                print('name: {} => gender: {}, probability: {}'
                ''.format(name, gender, prob))
    else:
        print('see help: chg -h')


if __name__ == '__main__':
    main()
