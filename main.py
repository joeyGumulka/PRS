#IMPORT LIBS
import json
import sys
from fifo import fifo
from lru import lru
from clock import clock



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
    result = fifo.run( frames, ref, trace)
elif algo == "LRU":
    result = lru.run(frames, ref, trace)
elif algo == "CLOCK":
    result = clock.run(frames, ref, trace)
else:
    sys.exit(1)

#Formatting and dumping results to json (requested format is annoying not automatic so need to  manually space out and fix the json)

base = {    #all outputs except the list (list needs special formatting to print all in one line like in provided example output)
    "algorithm": result["algorithm"],
    "frames": result["frames"],
    "faults": result["faults"],
    "hits": result["hits"]
}

with open("output.json", "w") as f:
    f.write(json.dumps(base, indent=4)[:-2])  # remove closing }
    f.write(',\n    "final_frames": ')
    f.write(json.dumps(result["final_frames"]))
    f.write("\n}")  #Re-add closing bracket