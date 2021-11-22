import os
import sys


def hello(a):
    with open(a) as f:
        sql = f.read().format(env=os.environ.get("ENVIRONMENT"))
        print(sql)


if __name__ == "__main__":
    hello(str(sys.argv[1]))
