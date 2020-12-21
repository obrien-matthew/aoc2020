import logging, sys
from math import prod
from copy import deepcopy
logging.basicConfig(
    level=logging.INFO,
    # filename='out.log',
    stream=sys.stdout,
    format=(
        '[%(asctime)s] '
        '%(levelname)s	'
        '<%(funcName)s:%(lineno)s>: '
        '%(message)s'
    )
)

# https://adventofcode.com/2020/day/1
# 1: 1003971
# 2: 84035952

SUM_TO = 2020
SUM_WITH = 3

def rec_sum(remain, sofar, prev, data):
    if remain == 0:
        if sofar == SUM_TO: return prev
        else: return None
    ilen = len(data)
    for i in range(ilen):
        if i in prev: continue
        cprev = deepcopy(prev)
        cprev.append(data[i])
        ret = rec_sum(remain-1, sofar+data[i], cprev, data)
        if not ret:
            continue
        return ret
        


def main():

    with open('days/01/input.txt', 'r') as infile:
        data = infile.read()
    
    data = data.split('\n')[:-1]
    data = [int(x) for x in data]
    ans = rec_sum(SUM_WITH, 0, list(), data)
    return prod(ans)

if __name__ == '__main__':
    print(main())
