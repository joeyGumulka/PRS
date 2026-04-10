#IMPORT LIBS
import json
import sys
from fifo import fifo
#TEMP PLACEHOLDER FUNCTIONS

def lru(frames, ref, trace):
    print("LRU NOT IMPLIMENTED YET")

def clock(frames, ref, trace):
    print("CLOCK NOT IMPLIMENTED YET")

input_file = sys.argv[1]    #Take input filepath as command-line arguement

with open(input_file, "r") as file: #Open the input file
    data = json.load(file)

#Convert file data into variables
#NOTE - Python supports data type assignment from json natively meaning explict declaration of type is not needed in this case
algo = data["algorithm"].upper()
frames = data["frames"]
ref = data["references"]
trace = data.get("trace", False)

#Check for if frames is 0 
if frames <= 0:
    print("ERROR: Impossible to run page replacement simulator with no frames.")
    sys.exit(1)

#Check algorithm type stated in provided json and run appropriate algorithm
if algo == "FIFO":
    fifo.run( frames, ref, trace)
elif algo == "LRU":
    lru(frames, ref, trace)
elif algo == "CLOCK":
    clock(frames, ref)
else:
    sys.exit(1)