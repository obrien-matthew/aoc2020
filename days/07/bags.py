import logging, sys
import re, json
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

MY_BAG = 'shiny gold'
REGX = r'(?:\s)?(\d+)?(?:\s)?((?:\w+\s?){2}) bag[s?\.|,]'
BAG_LOOKUP = {}
COUNT_LOOKUP = {}

def process(input_data):
    
    data = input_data.split('\n')[:-1]
    all_bags = {}
    for d in data:
        m = re.findall(REGX, d)
        parent = m[0][1]
        all_bags[parent] = []
        i = 1
        print(f'Parent: {parent}')
        while i < len(m):
            count = 0 if m[i][1] == 'no other' else m[i][0]
            all_bags[parent].append({
                'count': count,
                'type': m[i][1]
            })
            print(f'\tAdded: {m[i]}')
            i += 1
    return all_bags

def can_contain(search_for, bag, dataset):
    print(f'---\nChecking for: [{search_for}] in [{bag}]')
    if bag == 'no other':
        BAG_LOOKUP[bag] = False
        return False
    try:
        return BAG_LOOKUP[bag]
    except KeyError:
        pass
    if search_for in [b['type'] for b in dataset[bag]]:
        BAG_LOOKUP[bag] = True
        return True
    else:
        BAG_LOOKUP[bag] = (True in [can_contain(search_for, b['type'], dataset) for b in dataset[bag]])
        return BAG_LOOKUP[bag]

def contains(bagtype, data):
    print(f'Checking: {bagtype}')
    try:
        return COUNT_LOOKUP[bagtype]
    except KeyError:
        pass

    csum = 0
    for b in data[bagtype]:
        if b['type'] != 'no other':
            csum += int(b['count']) * (contains(b['type'], data) + 1)
    
    COUNT_LOOKUP[bagtype] = csum
    return csum


def main():
    with open('days/07/input.txt', 'r') as infile:
        data = infile.read()
    
    data = process(data)
    # Part 1
    contain_count = 0    
    for bagtype in data.keys():
        if can_contain(MY_BAG, bagtype, data): contain_count += 1
    
    # Part 2
    contains_count = contains(MY_BAG, data)

    return contain_count, contains_count



if __name__ == '__main__':
    print(main())
