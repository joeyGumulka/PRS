''' this implementation of clock is consistent with the actual clock page 
replacement algorithm '''

class clock:
    def run(maxFrames, ref, trace):
        frames = []  
        faults = 0
        hits = 0
        i = 0
        hand = 0  # the "clock hand" pointing to the current frame index

        for r in ref:
            i += 1
            page_found = False
            
            # checking for the hit condition 
            for frame in frames:
                if frame[0] == r:
                    hits += 1
                    frame[1] = 1  # second chance granted
                    page_found = True
                    break
            
            if not page_found:
                faults += 1
                if len(frames) < maxFrames:
                    # case where still have empty frames available
                    # adding page with use bit set to 1
                    frames.append([r, 1])
                else:
                    # case where frames are full, clock replacement performed
                    while True:
                        current_page = frames[hand]
                        
                        if current_page[1] == 0:
                            # replace this page if use bit was 0
                            frames[hand] = [r, 1]
                            hand = (hand + 1) % maxFrames
                            break
                        else:
                            # second chance
                            current_page[1] = 0
                            hand = (hand + 1) % maxFrames

            if trace:
                display_frames = [f"{f[0]}({f[1]})" for f in frames]
                print(f"---------------------------------------------------------------")
                print(f"Iteration: {i}")
                print(f"Current Page: {r}")
                print(f"Remaining Pages {ref[i:]}")
                print(f"Frames: {display_frames}")
                print(f"Hand Position: {hand}")
                print(f"Faults: {faults}")
                print(f"Hits: {hits}")
            
        return {
                "algorithm": "Clock",
                "frames": maxFrames,
                "faults": faults,
                "hits": hits,
                "final_frames": [f[0] for f in frames]
            }