import json
import sys

# functions for the algorithm
def fifo():
    print('ok')

def lru():
    print("ok")

def clock():
    print("ok")

# taking in the input
input_file = sys.argv[1]
with open(input_file, "r") as file:
    data = json.load(file)

algo = data["algorithm"]
frames = data["frames"]
ref = data["references"]
trace = ["trace"]

if frames <= 0:
    print ("Invalid input for 'frames'.")
    sys.exit()

if trace == None:
    print("Invalid input for 'trace'")
    sys.exit()

# running the needed algorithm
if algo == "fifo":
    fifo()

elif algo == "lru":
    lru()

elif algo == "clock":
    clock()

else:
    print("Invalid algorithm")
    sys.exit()