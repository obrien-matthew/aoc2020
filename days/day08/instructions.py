from copy import deepcopy
import logging, sys
logging.basicConfig(
    level=logging.DEBUG,
    filename='days/08/out.log',
    # stream=sys.stdout,
    format=(
        '[%(asctime)s] '
        '%(levelname)s	'
        '<%(funcName)s:%(lineno)s>: '
        '%(message)s'
    )
)

def partone(instr):
    ip = 0
    acc = 0
    indexes = []
    while True:
        indexes.append(ip)
        if instr[ip][0] == 'nop':
            ip += 1
        elif instr[ip][0] == 'jmp':
            ip += instr[ip][1]
        elif instr[ip][0] == 'acc':
            acc += instr[ip][1]
            ip += 1
        else:
            logging.error(f'Unrecognized instruction: {instr[ip]}')
            exit(1)
        
        if ip in indexes: 
            return acc


def parttwo(ip, acc, indexes, instr, try_switch=True):
    logging.debug(f'IP: {ip}')
    if ip in indexes or ip > len(instr):
        logging.debug(f'Bad path.') 
        return None
    elif ip == len(instr):
        logging.debug(f'Good path. ACC: {acc}')
        return acc
    
    indexes.append(ip)
    
    if instr[ip][0] == 'acc':
        acc += instr[ip][1]
        nip = ip + 1
        return parttwo(nip, acc, deepcopy(indexes), instr, try_switch)
    
    if try_switch:
        if instr[ip][0] == 'nop':
            nip = ip + instr[ip][1]
            t = parttwo(nip, acc, deepcopy(indexes), instr, False)
        else:
            nip = ip + 1
            t = parttwo(nip, acc, deepcopy(indexes), instr, False)
    else:
        t = None

    if instr[ip][0] == 'nop':
        nip = ip + 1
        return t or parttwo(nip, acc, deepcopy(indexes), instr, try_switch)
    else:
        nip = ip + instr[ip][1]
        return t or parttwo(nip, acc, deepcopy(indexes), instr, try_switch)


def main():

    with open('days/day08/input.txt', 'r') as infile:
        data = infile.read()
    
    instructions = data.split('\n')[:-1]
    instr = []
    for row in instructions:
        r = row.split(' ')
        instr.append([r[0], int(r[1])])
    
    pone = partone(instr)
    ptwo = parttwo(0, 0, [], instr)

    return pone, ptwo


if __name__ == '__main__':
    print(main())