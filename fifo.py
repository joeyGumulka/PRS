class fifo:
    def run(maxFrames, ref, trace):
        
        #NOTE - list in python is functionally a queue thus we can simply append to add new elements and pop the first element when doing FIFO; very convenient 

        #Internal variable declarations
        frames = [];    #Define the frames array, will be used to store current overall frame status
        faults = 0; #Counter for faults
        hits = 0;   #Counter for hits
        i = 0;  #Iteration counter

        for r in ref:   #Iterate through each page
            i += 1  
            if r in frames:
                hits += 1   #Hit, no change to frames needed
            else:
                if len(frames) < maxFrames:   #Fault & avaliable frame -> add r to frames
                    faults += 1 
                    frames.append(r)    #Add current page to avaliable frame
                else: #Frames full & page not in current frame -> FIFO 
                    faults += 1 
                    frames.pop(0)    #Remove front element in queue
                    frames.append(r)    #Replace with new page
            if trace == True:   #Print trace if desired
                print("---------------------------------------------------------------\nIteration ", i, "\nRemaining Pages ",  ref[i:], "\nCurrent Page: ", r, "\nFrame: ", frames, "\nFaults:", faults, "\nHits:", hits, "\n\n")

        return {
            "algorithm": "FIFO",
            "frames": maxFrames,
            "faults": faults,
            "hits": hits,
            "final_frames": frames
        }