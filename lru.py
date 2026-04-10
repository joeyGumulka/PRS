class lru:
    def run(maxFrames, ref, trace):
        
        #NOTE - list in python is functionally a queue thus secondary queue for page history is redunant in this case
        #front = oldest & end = newest -> frames used both as queue and storing current pages in frames (only possible as reference by index/pointer is not needed for this simple policy simulation)

        #Internal variable declarations
        frames = [];    #Define the frames array, will be used to store current overall frame status
        faults = 0; #Counter for faults
        hits = 0;   #Counter for hits
        i = 0;  #Iteration counter

        for r in ref:   #Iterate through each page
            i += 1  
            if r in frames: #Hit; Increase counter, move current page to end of queue (A.K.A. most recently accessed page) 
                hits += 1 
                frames.remove(r)   #Remove r from queue (current position)
                frames.append(r)    #Append r to end of queue denoting that it is the most recent page (functionally using the frames as a queue and frames simultaniously)
            else:
                if len(frames) < maxFrames:   #Fault & avaliable frame -> add r to frames
                    faults += 1 
                    frames.append(r)    #Add current page to avaliable frame
                else: #Frames full & page not in current frame -> LRU 
                    faults += 1 
                    frames.pop(0)    #Remove front element in queue (oldest)
                    frames.append(r)    #Replace with new page
            if trace == True:   #Print trace if desired
                print("---------------------------------------------------------------\nIteration ", i, "\nRemaining Pages ",  ref[i:], "\nCurrent Page: ", r, "\nFrame: ", frames, "\nFaults:", faults, "\nHits:", hits, "\n\n")