"""
This is a docstring for the Markov module.

>>> m = Markov('ab')
>>> m.predict('a')
'b'

"""

import argparse
import random
import sys
import urllib.request as req

def fetch_url(url, fname):
    fin = req.urlopen(url)
    data = fin.read()
    fout = open(fname, mode='wb')
    fout.write(data)
    fout.close()

def from_file(fname, size):
    fin = open(fname, encoding='utf8')
    txt = fin.read()
    return Markov(txt, size)

def repl(m):
    print("Welcome to the REPL.")
    print("Hit ctl-c to exit")
    while True:
        try:
            txt = input('> ')
        except KeyboardInterrupt:
            print('Goodbye')
            break
        try:
            res = m.predict(txt)
        except KeyError:
            print('Text not found, try again!')
        except IndexError:
            print('Too long try again!')
        else:
            print(res)

class Markov:
    def __init__(self, txt, size=1):
        self.tables = []
        for i in range(size):
            self.tables.append(get_table(txt, size=i+1))

    def predict(self, data_in):
        table = self.tables[len(data_in)-1]
        options = table.get(data_in, {})
        if not options:
            raise KeyError(f'{data_in} not found')
        possibles = []
        for key in options:
            count = options[key]
            for i in range(count):
                possibles.append(key)
        return random.choice(possibles)

def get_table(txt, size=1):
    """This is the function docstring

    >>> get_table('ab')
    {'a': {'b':1}}
    """

    results = {} # dictionary literal
    for i in range(len(txt)):
        chars = txt[i:i + size]
        try:
            out = txt[i+size]
        except IndexError:
            break
        char_dict = results.get(chars, {})
        char_dict.setdefault(out, 0)
        char_dict[out] += 1
        results[chars] = char_dict
    return results

def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--file', help='specify file')
    ap.add_argument('-s', '--size', help='Markov size (defualt 1)', default=1, type=int)
    opts = ap.parse_args(args)
    if opts.file:
        m = from_file(opts.file, opts.size)
        repl(m)

if __name__ == '__main__':
    # executing this file
    main(sys.argv[1:])
