# PRS
A page replacement simulator created for "COMP330; Operating Systems", to be used as the Mini Project Assignment submission.

--------------------------------------------------------------------------------------------------------------------------------------------------------
## ABOUT

- Course: COMP3300
- Submission Date: April 15th, 2026
- Authors: Basra, Vedant & Gumulka, Joey
- Python Version: Python 3.14.4

--------------------------------------------------------------------------------------------------------------------------------------------------------
## AI USAGE STATEMENT
AI tools were used as supportive learning resources during this project. Specifically, Google’s Gemini and OpenAI’s ChatGPT assisted in clarifying the algorithms behind FIFO, LRU, and Clock (Second Chance) page replacement methods, as well as in understanding how to read from and write to JSON files.

--------------------------------------------------------------------------------------------------------------------------------------------------------
## Tie-Breaking Policy
- FIFO: The page at index 0 is evicted, as it has been in memory the longest since its initial load.
- recency by moving recently accessed (“hit”) pages to the end of the array, ensuring that the least recently used page shifts to index 0 and is selected for eviction in tie situations.
- Clock (Second Chance): The first page encountered with a use bit of 0 is evicted. If all pages have a use bit of 1, the algorithm completes a full rotation, resetting use bits to 0, and then evicts the page at the current hand position

--------------------------------------------------------------------------------------------------------------------------------------------------------
## DESIGN DECISIONS
To facilitate organization and collaboration, the project is hosted on a GitHub repository (https://github.com/joeyGumulka/PRS). Each algorithm is implemented in its own class file to maintain clarity and modularity, while main.py serves as the entry point of the program. The main.py file is responsible for handling input and output operations with JSON files and coordinating the execution of the algorithm classes. Additionally, each algorithm is supported by at least ten test cases to thoroughly evaluate functionality, including various edge cases.