import os
import sys

environment = os.environ.get("ENVIRONMENT")


def hello(filename):
    # with open(filename) as f:
    #     print(filename)
    #     print(environment)
    #     sql = f.read().format(ENVIRONMENT=environment)
    print(filename)


if __name__ == "__main__":
    hello(str(sys.argv[1]))
