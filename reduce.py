import sys
from collections import defaultdict

topics =  sys.stdin.read().split()

topicsDict = defaultdict(int)
for topic in topics:
    topicsDict[topic] += 1


print(max(topicsDict.items(), key=(lambda key: topicsDict[key]))[0])
