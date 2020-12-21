import re, json
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
PP_FIELDS = [
    ['byr'],
    ['iyr'],
    ['eyr'],
    ['hgt'],
    ['hcl'],
    ['ecl'],
    ['pid']
    # 'cid'
]

# Part 2
PP_FIELDS = [
    ['byr', r'(^19[2-9][0-9]$|^200[0-2]$)'],
    ['iyr', r'(^201[0-9]$|^2020$)'],
    ['eyr', r'(^202[0-9]$|^2030$)'],
    ['hgt', r'(^1[5-8][0-9]cm$|^19[0-3]cm$|^59in$|^6[0-9]in$|^7[0-6]in$)'],
    ['hcl', r'^#[a-f0-9]{6}$'],
    ['ecl', r'^(amb|blu|brn|gry|grn|hzl|oth)$'],
    ['pid', r'^\d{9}$']
    # ['cid' r'.*']
]


def main():
    with open('days/04/input.txt', 'r') as infile:
        data = infile.read()
    
    data = data.split('\n\n')
    logging.info(f'Read in {len(data)} passports...')
    valid_count = 0
    invalid_count = 0
    for passport in data:
        fields = re.split(r' |\n', passport)
        fields = [f.split(':') for f in fields]
        jfields = {}
        for f in fields:
            if len(f) == 2: jfields[f[0]] = f[1]
    
        regex = len(PP_FIELDS[0]) == 2
        # logging.debug(f'Checking: {json.dumps(jfields, indent=4)}')
        valid = False
        for req_field in PP_FIELDS:
            if req_field[0] not in jfields.keys():
                logging.debug(f'{req_field[0]} NOT IN {jfields.keys()}')
                valid = False
                break

            if re.search(req_field[1], jfields[req_field[0]]):
                # logging.debug(f'{jfields[req_field[0]]} VALID')
                valid = True
            else: 
                logging.debug(f'{req_field[0]}: {jfields[req_field[0]]} INVALID')
                valid = False
                break
        
        if valid: valid_count += 1
        else: invalid_count += 1
        logging.debug(f'\tValid: {valid_count}')
        logging.debug(f'\tInvalid: {invalid_count}')
        logging.debug(f'_____________________\n')
    
    return valid_count


    

if __name__ == '__main__':
    print(main())