from github import Github
import pandas as pd

ACCESS_TOKEN  = "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"
# creating a github object
g = Github(ACCESS_TOKEN)

def cleanResults(results):
    """
    results is expected to be the response of a github 
    search request for commits with a certain phrase.
    """
    # creating two lists that will store 
    # dates and the messages respectively
    dates = []
    messages = []
    # looping through each result
    for result in results:
        commit = result.raw_data
        # raw_data is a dictionary
        # interest is in keys whose values 
        # have the date and message
        commit = commit.get("commit")
        date = commit.get("author").get("date")
        message = commit.get("message")

        # cleaning up the data 
        if "bumps" in message.lower():
            indexOfBumps = message.lower().index("bumps")
            message = message[:indexOfBumps]
        # ignoring files that dont have bump in the message
        if "bump" not in message.lower(): 
            continue
        while "\n" in message:
            message = message.replace("\n", " ")
        # appending the message to 
        # the messages list
        messages.append(message)
        # removing time from the date
        indexOfT = date.find('T')
        date = date[:indexOfT]
        dates.append(date)
    
    # putting the lists in a pandas dataphrame
    dt = pd.DataFrame()
    dt['Date'] = dates
    dt['Message'] = messages
    # returning the dataframe
    return dt


##-------- bump repo:numpy/numpy ---------##
# getting the response and passing it to the cleanResults function
results = g.search_commits("bump repo:numpy/numpy")
#printing count of results
print(results.totalCount)
dt = cleanResults(results)
# writing the dataframe to a file
dt.to_excel("numpy_numpy_BumpCommit.xlsx",index = False)


##---------- bump repo:elastic/logstash ----------##
# getting the response and passing it to the cleanResults function
results = g.search_commits("bump repo:elastic/logstash")
#printing count of results
print(results.totalCount)
dt = cleanResults(results)
# writing the dataframe to a file
dt.to_excel("elastic__BumpCommit.xlsx",index = False)
