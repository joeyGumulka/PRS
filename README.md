# PRS

A page replacement simulator created for "COMP330; Operating Systems", to be used as the Mini Project Assignment submission.

--------------------------------------------------------------------------------------------------------------------------------------------------------
## ABOUT

Course: COMP3300
Submission Date: April 15th, 2026
Authors: Basra, Vedant & Gumulka, Joey
Python Version: Python 3.14.4
Repository: https://github.com/joeyGumulka/PRS

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

Throughout the development of our page replacement simulator mini project we discussed and made multiple design decisions that I believe strongly contributed to our overall success. Firstly, we made the choice to host our project on a GitHub repository (https://github.com/joeyGumulka/PRS) which allowed for organization of our work into distinct branches while simultaneously enabling seamless collaboration. Furthermore, another design decision that greatly improved the quality of our project as a whole was the application of OOP design principles, most significantly for this project, encapsulation. Each of the 3 page replacement policies was coded in a separate class, allowing us to reuse a single main file for running all inputs regardless of the policy specified. Doing this allowed a significant reduction in the volume of code required to make our project functional, as well as providing much easier readability and troubleshooting. Moreover, another meaningful design decision that we found to be of great benefit when collaborating with group members was ensuring all code was very well commented, thereby reducing the amount of time needed for one group member to understand the purpose of code contributed by others without the need for extensive manual clarification each time.