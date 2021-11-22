import argparse
import os

environment = os.environ.get("ENVIRONMENT")

parser = argparse.ArgumentParser()
parser.add_argument("--filename", type=str)

args = parser.parse_args()
filename = args.filename


def hello(filename):
    # with open(filename) as f:
    # sql = f.read().format(ENVIRONMENT=environment)
    # create view here
    print(filename)
