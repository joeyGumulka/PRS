# PRS

A page replacement simulator created for "COMP330; Operating Systems", to be used as the Mini Project Assignment submission.

--------------------------------------------------------------------------------------------------------------------------------------------------------
## ABOUT

Course: COMP3300
Submission Date: April 15th, 2026
Authors: Basra, Vedant & Gumulka, Joey
Python Version: Python 3.14.4

--------------------------------------------------------------------------------------------------------------------------------------------------------
## AI USAGE STATEMENT

Throughout the development of our page replacement simulator mini project as a group we selectively made use of AI tools primarily with the goal of work efficiency and test case verification. As a group we made use of the following LLMs; ChatGPT, Gemini, and Claude. Intelligent application of these LLMs allowed for significant reduction in the amount of time spent searching for examples of Python syntax as well as features of the language (i.e. lists), for which we were fairly unfamiliar. Essentially, AI was used to provide generic examples of conditional structures, library calls, and list manipulation. This is to say that all code and comments were written manually by hand with AI serving as nothing more than a more efficient way to reference documentation rather than manually searching. Moreover, we also made use of AI tools to assist in creating test cases, ensuring that they covered as many unique situations and edge cases as feasible.

--------------------------------------------------------------------------------------------------------------------------------------------------------
## Tie-Breaking Policy
- FIFO: The page at index 0 is evicted, as it has been in memory the longest since its initial load.
- recency by moving recently accessed (“hit”) pages to the end of the array, ensuring that the least recently used page shifts to index 0 and is selected for eviction in tie situations.
- Clock (Second Chance): The first page encountered with a use bit of 0 is evicted. If all pages have a use bit of 1, the algorithm completes a full rotation, resetting use bits to 0, and then evicts the page at the current hand position

--------------------------------------------------------------------------------------------------------------------------------------------------------
## DESIGN DECISIONS
To facilitate organization and collaboration, the project is hosted on a GitHub repository (https://github.com/joeyGumulka/PRS). Each algorithm is implemented in its own class file to maintain clarity and modularity, while main.py serves as the entry point of the program. The main.py file is responsible for handling input and output operations with JSON files and coordinating the execution of the algorithm classes. Additionally, each algorithm is supported by at least ten test cases to thoroughly evaluate functionality, including various edge cases.