"""
A computer can processes code files in a file. If the file has code lines that are divisible by the number of cores,
The computer can split the code lines among the cores.
Example if the file has 5, 10, 20 code lines, these can all be  processed by a computer that 
has 5 cores since they are all divisible by 5. The number of files that can be 
processed at the same time also has a limit. If the limit is 2 then 2 files 
can be processed simultaneously.
Given a list of n files with file length at every index, given the number of cores, given the limit. 
Assuming each line is processed per second, find the time taken by a computer to process the list of files.

Example:
    files = [5,1,3,8]
    numCores = 5
    limit = 1

Since there is a file with 5 lines, and numCores is 5,
those lines can be divided among the 5 cores therefore time taken is (5/5) = 1
So the process time is (5/5) + 1 + 3 + 8 = 13, return 13

Example 2:
    files = [12, 4, 8, 3, 1]
    numCores = 4
    limit = 2

There are 4 cores and 3 files divisible by 4
Limit is 2 so only 2 files can be processed simultaneously
Processing file 1 = (12/4) = 3, processing file 2 = (4/4) = 1
processing file 3 = (8/4) = 2, Processing file 4 = 3
Processing file 5 = 1

2 files can be processed at a go, so file 1 and file 4 are processed  simultaneously 
since they both utilize the 3 seconds. File 2 and file 3 can also be processed 
simultaneously so we choose the max time which is 2 seconds
finally file 5 is alone so time is 1 second.
Process time = 3 + 2 + 1 = 6. Return 6

"""

from collections import Counter
def Solution(files,numCores, limit):
    c = Counter(files)
    print()
    keys = list(c.keys())
    values = list(c.values())
    print(keys)
    
    value = [int((keys[i]/numCores)) if keys[i]%numCores == 0 else keys[i] for i in range(len(keys))]
    value = [value[i] * values[i]  for i in range(len(keys))]
    
    return sum(value)
    print(value) 
    print(c)



files = [5, 3, 1] 
numCores = 5
limit = 5
Solution(files, numCores, limit)