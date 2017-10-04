import sys
import os
import argparse
from collections import defaultdict


def search_doubles(dirpath):
    compare_files = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(dirpath):
        for fname in filenames:
            fsize = os.path.getsize(os.path.join(dirpath, fname))
            compare_files[(fname, fsize)].append(dirpath)
    return filter(lambda x: len(x[1]) > 1, compare_files.items())


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        help='start directory for searching duplicates',
                        required=True)
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    for found_file in search_doubles(args.path):
        for path in found_file[1]:
            print('%d %s/%s' % (found_file[0][1], path, found_file[0][0]))
