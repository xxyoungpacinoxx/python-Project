import string


def return_number(user_input: str):
    num_list = []
    for item in user_input:
        num_list.append(string.ascii_letters.index(item))
    return num_list


# 26 is ultra key to broke generator
def key_generator(num_list: list):
    return list(map(lambda x: x+18, num_list))


def encryption(generate_list: list):
    token = str()
    for item in generate_list:
        token += string.ascii_letters[item]
    return token


print(encryption(key_generator(return_number('abcdefgh'))))
