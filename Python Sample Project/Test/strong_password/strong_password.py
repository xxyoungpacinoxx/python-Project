import string
import random
import argparse


def strong_password(length=8, up=False, lw=False, dg=False, punc=False):
    key = list()
    if up:
        key += string.ascii_uppercase
    if lw:
        key += string.ascii_lowercase
    if dg:
        key += string.digits
    if punc:
        key += string.punctuation
    if len(key) == 0:
        key = string.ascii_letters + string.digits + string.punctuation

    return ''.join(random.choices(key, k=length))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Strong Password Builder',
                                     description='Create Strong Password \nDeveloped by xxypxx ...')
    parser.add_argument('length', type=int, help='this is length parameter')
    parser.add_argument('-u', '--upper', help='Upper Case', action='store_true')
    parser.add_argument('-l', '--lower', help='Lower Case', action='store_true')
    parser.add_argument('-d', '--digit', help='Digit Case', action='store_true')
    parser.add_argument('-p', '--punc', help='Digit Case', action='store_true')

    args = parser.parse_args()
    print(args)
    print(strong_password(args.length, args.upper, args.lower, args.digit, args.punc))
