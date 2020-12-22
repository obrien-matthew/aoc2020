import logging, sys
import numpy
from time import sleep
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

ROWS = 128
SEATS = 8

def seat_id(row, col):
    return (row * 8) + col

def get(bpass, rem, total=0):
    if len(bpass) == 0: return total
    to_add = total + (0 if bpass[0] in ['F', 'L'] else (rem//2))
    return get(bpass[1:], rem-(rem//2), to_add)

def main():
    with open('days/day05/input.txt', 'r') as infile:
        data = infile.read()
    
    data = data.split('\n')[:-1]
    all_ids = []
    for bpass in data:
        row = get(bpass[:7], ROWS)
        col = get(bpass[7:], SEATS)
        sid = seat_id(row, col)
        logging.info(f'{bpass}: {row}-{col} [{sid}]')
        all_ids.append(sid)
    
    all_ids.sort()
    for i in range(len(all_ids)):
        if all_ids[i+1] == all_ids[i]+2:
            return all_ids[i]+1
    
    
if __name__ == '__main__':
    print(main())