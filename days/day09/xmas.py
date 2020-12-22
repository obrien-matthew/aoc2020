import logging, sys
from days.day01.sum import rec_sum
logging.basicConfig(
    level=logging.DEBUG,
    filename='days/day09/out.log',
    # stream=sys.stdout,
    format=(
        '[%(asctime)s] '
        '%(levelname)s	'
        '<%(funcName)s:%(lineno)s>: '
        '%(message)s'
    )
)

VALID_WINDOW = 25
SUM_WITH = 2

def main():
    with open('days/day09/input.txt', 'r') as infile:
        data = infile.read()

    data = data.split('\n')[:-1]
    data = [int(i) for i in data]

    # Part 1
    for i in range(VALID_WINDOW, len(data)):
        s = i - VALID_WINDOW
        if not rec_sum(SUM_WITH, 0, list(), data[s:i], data[i]):
            pone = data[i]
            break
    
    ptwo = None
    for i in range(len(data)):
        logging.debug(f'Checking: {i}')
        s = data[i]
        j = i
        while s < pone:
            logging.debug(f's = {s} < pone = {pone}')
            j = j + 1
            s += data[j]
            if s == pone:
                logging.info(f'Hit: {i} - {j}')
                start = i
                end = j
                ptwo = min(data[i:j]) + max(data[i:j])
                break
        if ptwo: break
        logging.debug(f'Miss: {i}')

    return pone, ptwo


if __name__ == '__main__':
    print(main())