"""
Given a list of strings, find out how many 
occurances of each query in the queries list.
Return a list of counts of the occurances per query
"""

def Solution(strings,queries):
    soln = []
    for q in queries:
        soln.append(strings.count(q))

    print(soln)   
    pass

strings = ['aba','baba','aba','xzxb']

queries = ['aba','xzxb','ab']

Solution(strings,queries)