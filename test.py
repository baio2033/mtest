import os

def print_env():
    print(os.environ())

for _ in os.listdir():
    print(_)

if __name__=="__main__":
    print("main")
print_env()
