# reddit_crawler
A python web crawler that I wrote from scratch.


It starts at www.reddit.com and searches for href tags. 
Subreddits: creates a file called subs.txt and appends all patterns matching /r/* to this file with no repetition.
Users: creates a file called users.txt and appends all patterns matching /user/* to this file with no repetition.
Topics: creates a file called topics.txt and appends all patterns matching /t/* to this file with no repetition.

To run:
1. Install the requirements in requirements.txt 
2. >python3 main.py
