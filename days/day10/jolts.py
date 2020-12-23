import logging, sys
from copy import deepcopy
import numpy
logging.basicConfig(
    level=logging.DEBUG,
    filename='days/day10/out.log',
    filemode='w',
    # stream=sys.stdout,
    format=(
        '[%(asctime)s] '
        '%(levelname)s	'
        '<%(funcName)s:%(lineno)s>: '
        '%(message)s'
    )
)

ACCEPTABLE_DIFF = 3

def jolt_options(indx, adapters, diff, lookup):
    if indx == len(adapters)-1:
        return 1
    
    variations = 0
    for i in range(indx+1, len(adapters)):
        if adapters[i] - adapters[indx] > diff:
            break
        if not lookup[i]:
            lookup[i] = jolt_options(i, adapters, diff, lookup)
        
        variations += lookup[i]
    
    lookup[indx] = variations
    return variations
    


def main():
    with open('days/day10/input.txt', 'r') as infile:
        data = infile.read()

    data = data.split('\n')[:-1]
    data = [int(i) for i in data]
    data.sort()

    outlet = 0
    device = (data[-1] + 3)
    fixeddata = [outlet] + data + [device]

    # Part 1
    diff1 = 0
    diff3 = 0
    for d in range(len(fixeddata)-1):
        logging.debug(f'{fixeddata[d+1]} - {fixeddata[d]} = [{fixeddata[d+1]-fixeddata[d]}]')
        if fixeddata[d+1] - fixeddata[d] == 1:
            diff1 += 1
        elif fixeddata[d+1] - fixeddata[d] == 3:
            diff3 += 1

    pone = (diff1 * (diff3))
    logging.info(f'Diff1: {diff1} Diff3: {diff3} Pone: {pone}')
    
    # Part 2
    '''
    Memoization Table:
        - Array of `len(num_adapters)`
        - Ways to get from adapter[i] -> adapter[x] == sum((ways to get from adapter[j] -> adapter[k])) for adapter[j] such that adapter[j] reachable *directly* by adapter[i]

    Example:
        adapters = [ 0, 2, 3, 4, 5, 7 ]

        Unique ways to get from adapter[0] to adapter[5]:

        adapter[0] can reach 2 adapters directly:                   (9 solutions: 0->2(6), 0->3(3))
            - adapter[1] can reach 3 adapters directly:             (6 solutions: 2->3(3), 2->4(2), 2->5(1))
                - adapter[2] can reach 2 adapters directly:         (3 solutions: 3->4(2), 3->5(1))
                    - adapter[3] can reach 2 adapters directly      (2 solutions: 4->7, 4->5(1))
                        - adapter[4] can reach 1 adapter directly   (1 solution: 5->7)
                            - adapter[5]
                        - adapter[5]
                    - adapter[4]
                - adapter[3]:
                    - adapter[4]
                    - adapter[5]
                - adapter[4]:
                    - adapter[5]
            - adapter[2]
                - adapter[3]
                - adapter[4]

        [0 [2 [3 [4 [5 [7]]]]]]
        [0 [2 [3 [4    [7]]]]]
        [0 [2 [3    [5 [7]]]]]
        [0 [2    [4 [5 [7]]]]]
        [0 [2    [4    [7]]]]
        [0 [2       [5 [7]]]]
        [0    [3 [4 [5 [7]]]]]
        [0    [3    [5 [7]]]]
        [0    [3 [4    [7]]]]


         ___0___  ___2___  ___3___  ___4___  ___5___  ___7___ 
        [       ][       ][       ][       ][       ][       ]
        [   9   ][   6   ][   3   ][   2   ][   1   ][   /   ]
        [_______][_______][_______][_______][_______][_______]

    '''
    num_adapters = len(fixeddata)
    lookup = [None for i in range(num_adapters)]
    ptwo = jolt_options(0, fixeddata, ACCEPTABLE_DIFF, lookup)
    logging.debug(f'\n\n{lookup}\n')

    return pone, ptwo


if __name__ == '__main__':
    print(main())