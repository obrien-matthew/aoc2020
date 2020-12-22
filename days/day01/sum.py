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

def rec_sum(remain, sofar, prev, data, sum_to):
    '''
    Recursive function to get `sum_with` integers from a list of 
        integers which sum to `sum_to`.
    Returns the list of summable integers or None.

    Args:
        remain ([type]): [description]
        sofar ([type]): [description]
        prev ([type]): [description]
        data ([type]): [description]
        sum_to ([type]): [description]

    Returns:
        list: The list of summable integers or None.
    '''
    if remain == 0:
        if sofar == sum_to: return prev
        else: return None
    ilen = len(data)
    for i in range(ilen):
        if i in prev: continue
        cprev = deepcopy(prev)
        cprev.append(data[i])
        ret = rec_sum(remain-1, sofar+data[i], cprev, data, sum_to)
        if not ret:
            continue
        return ret
        


def main():

    with open('days/day01/input.txt', 'r') as infile:
        data = infile.read()
    
    data = data.split('\n')[:-1]
    data = [int(x) for x in data]
    ans = rec_sum(SUM_WITH, 0, list(), data, SUM_TO)
    return prod(ans)

if __name__ == '__main__':
    print(main())
