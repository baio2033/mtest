import os

def print_env():
    print(os.environ())

for _ in os.listdir():
    print(_)

print_env()