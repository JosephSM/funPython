from random import uniform
from pprint import pprint

def bucket():
    bucketdict = {}
    for i in range(100):
        r = int(uniform(500,550))
        if r in bucketdict:
            bucketdict[r] += 1
        else:
            bucketdict[r] = 1
    return bucketdict


bucketlist = list(bucket().iteritems())
pprint(sorted(bucketlist, reverse=True, key=lambda item: item[1]))
