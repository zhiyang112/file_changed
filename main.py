import os
import sys


def hello(filename):
    with open(filename) as f:
        sql = f.read().format(ENVIRONMENT=os.environ.get("ENVIRONMENT"))
        print(sql)


if __name__ == "__main__":
    hello(str(sys.argv[1]))
