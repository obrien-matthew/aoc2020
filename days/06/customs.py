
import logging, sys
from copy import deepcopy
logging.basicConfig(
    level=logging.DEBUG,
    # filename='out.log',
    stream=sys.stdout,
    format=(
        '[%(asctime)s] '
        '%(levelname)s	'
        '<%(funcName)s:%(lineno)s>: '
        '%(message)s'
    )
)


def main():
    with open('days/06/input.txt', 'r') as infile:
        data = infile.read()
    
    data = data[:-1].split('\n\n')
    anyone_sum = 0
    everyone_sum = 0
    for row in data:
        # part 1
        temp = set(list(row))
        if '\n' in temp: temp.remove('\n')
        anyone_sum += len(temp)

        # part 2
        temp = row.split('\n')
        init_set = set(temp[0])
        for t in temp:
            temp_set = set()
            t = list(t)
            for c in t:
                if c in init_set:
                    temp_set.add(c)
            init_set = deepcopy(temp_set)

        everyone_sum += len(init_set)
    
    return anyone_sum, everyone_sum


if __name__ == '__main__':
    print(main())