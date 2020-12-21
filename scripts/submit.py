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
        level = sys.argv[2]
        ans = sys.argv[3]
    except IndexError:
        print('Usage: python submit.py <day> <level> <answer>')
        exit(1)

    url = URL + day + '/answer'
    data = {
        'level': level,
        'answer': ans
    }
    logging.info(f'URL: {url}')
    logging.info(f'Data: {data}')
    r = requests.post(url, data=data, cookies=secrets.SESSION_COOKIE)
    r.raise_for_status()
    if "That's not the right answer" in r.text:
        print("That's not the right answer...")
    elif "That's the right answer!" in r.text:
        print("That's the right answer!")
    else:
        print(r.text)
    return

if __name__ == '__main__':
    main()