import argparse


def end_range(num):
    ls = []
    for i in range(0, num+1):
        ls.append(i)
    return ls


def between_range(input_list):
    ls = []
    for i in range(input_list[0], input_list[1]):
        ls.append(i)
    return ls


def jump_range(input_list):
    ls = []
    for i in range(input_list[0], input_list[1]):
        ls.append(i)
    return ls[input_list[0]:input_list[1]:input_list[2]]


parser = argparse.ArgumentParser()
parser.add_argument('-e', type=int, help='end_range function')
parser.add_argument('-b', type=str, help='between_range function')
parser.add_argument('-j', type=str, help='jump_range function')

args = parser.parse_args()
print(args)
if args.e is not None:
    print(end_range(args.e))
elif args.b is not None:
    print(between_range(list(eval(args.b))))
elif args.j is not None:
    print(jump_range(list(eval(args.j))))



