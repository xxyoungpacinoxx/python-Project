from config import INPUT_AUTH
import random


def get_user_choice():
    user_choice = input('Enter Your Choice (r,p,s): ')
    if user_choice not in INPUT_AUTH:
        user_choice = input('Wrong choice, select again: ')
    return user_choice


def get_system_choice():
    return random.choice(INPUT_AUTH)


def winner(user, system):



def play(user,system):
    pass
