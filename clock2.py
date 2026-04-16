'''this implementation of clock page replacement uses the tie-breaking policy
of circular order of evaluation'''


class clock:
    def run(maxFrames, ref, trace):
        frames = []  
        faults = 0
        hits = 0
        i = 0
        hand = 0  

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
                    # case where still have empty frames available adding page with use bit set to 1
                    frames.append([r, 1])
                else:
                    # case where frames are full, clock replacement performed
                    while True:
                        # identify all pages currently having a use bit of 0
                        candidates = [idx for idx, f in enumerate(frames) if f[1] == 0]
                        
                        if candidates:
                            # tie-breaker: If multiple pages have use bit 0, evict the one with the smallest page number 
                            best_index = min(candidates, key=lambda idx: frames[idx][0])
                            
                            # replace the selected page
                            frames[best_index] = [r, 1]
                            
                            # update the hand to be right after the replaced frame 
                            hand = (best_index + 1) % maxFrames
                            break
                        else:
                            # if all use bits are 1, everyone gets their "second chance" flipped to 0, and we re-scan to find the smallest page 
                            for frame in frames:
                                frame[1] = 0
                            # hand continues moving in a circular fashion logically
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