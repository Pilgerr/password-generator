import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$%&*/\?"

def password_generator(len_pass = 8):
    Use_for = lower_case + upper_case + numbers + symbols
    password = "".join(random.sample(Use_for, len_pass))
    return password