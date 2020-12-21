import re
import logging, sys
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


POLICY_SPLIT = ': '
POLICY_PATTERN = r'(?P<min>\d+)-(?P<max>\d+)\s(?P<char>.{1})'

def main():
    with open('days/02/input.txt', 'r') as infile:
        data = infile.read()
    
    valid1_count = 0
    valid2_count = 0
    data = data.split('\n')[:-1]
    logging.info(f'Checking {len(data)} passwords...')
    for item in data:
        item = item.split(POLICY_SPLIT)
        entry = {
            'pw': item[1],
            'policies': []
        }
        for m in re.finditer(POLICY_PATTERN, item[0]):
            entry['policies'].append(m.groupdict())
        
        # Part 1 check
        for p in entry['policies']:
            cc = entry['pw'].count(p['char'])
            if cc >= int(p['min']) and cc <= int(p['max']):
                valid1_count += 1
                logging.debug(f'GOOD: {entry}')
            else:
                logging.debug(f'BAD: {entry}')
        
        # Part 2 check
        for p in entry['policies']:
            print(entry)
            at_min = p['char'] == entry['pw'][int(p['min'])-1]
            at_max = p['char'] == entry['pw'][int(p['max'])-1]
            if (at_min != at_max):
                valid2_count += 1


    logging.info(f'Total valid passwords, part 1: {valid1_count}')
    logging.info(f'Total valid passwords, part 2: {valid2_count}')
    return {
        'part 1': valid1_count,
        'part 2': valid2_count
    }


if __name__ == '__main__':
    print(main())