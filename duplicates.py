import sys
import os
from collections import defaultdict

def search_doubles(dirpath):
    compare_files = defaultdict(list)
    for (dirpath, dirnames, filenames) in os.walk(dirpath):
        for fname in filenames:
            fsize = os.path.getsize('%s/%s' % (dirpath, fname))
            compare_files[(fname, fsize)].append(dirpath)
    return filter(lambda x: len(x[1]) > 1 ,compare_files.items())


if __name__ == '__main__':
    for found_file in search_doubles(sys.argv[1]):
        for path in found_file[1]:
            print('%d %s/%s' % (found_file[0][1], path, found_file[0][0]))
