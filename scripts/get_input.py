#!venv/bin/python
import requests
import secrets
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

URL = 'https://adventofcode.com/2020/day/'

def main():
    try:
        day = sys.argv[1]
    except IndexError:
        print('Usage: python get_input.py <day>')
        exit(1)

    url = URL + day + '/input'
    logging.info(f'Fetching: {url}')
    r = requests.get(url, cookies=secrets.SESSION_COOKIE)
    r.raise_for_status()
    f = f'days/{day:0>2}/input.txt'
    logging.info(f'Writing to {f}')
    with open(f, 'wb+') as outfile:
        outfile.write(r.content)
    logging.info('Execution complete.')

if __name__ == '__main__':
    main()