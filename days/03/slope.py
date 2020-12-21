import logging, sys
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
# Part 1
VELOCITIES = [
    [3, 1]
]

# Part 2

VELOCITIES = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

TREE = '#'

def main():
    with open('days/03/input.txt', 'r') as infile:
        data = infile.read()
    
    tdata = data.split('\n')
    data = []
    for row in tdata:
        data.append(list(row))
    
    prod = 1
    for vel in VELOCITIES:
        ypos = 0
        xpos = 0
        tree_count = 0
        pattern_len = len(data[0])
        while ypos < len(data)-1:
            # logging.debug(f'y:{ypos} x:{xpos%pattern_len}')
            if data[ypos][xpos%pattern_len] == TREE: 
                tree_count += 1

            xpos += vel[0]
            ypos += vel[1]

        prod = prod * tree_count

    return prod


if __name__ == '__main__':
    print(main())