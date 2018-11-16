
"""
Iterate over a MARC file, print out all title.

Example input file: https://is.gd/QUNyGk

    $ make clean && make
    $ python app.zip catalog.mrc | grep -i london
"""

import pymarc
import sys

if sys.version_info.major < 3:
    reload(sys)
    sys.setdefaultencoding("utf-8")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: %s FILE' % sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1], 'rb') as handle:
        reader = pymarc.MARCReader(handle, to_unicode=True, force_utf8=False)
        for record in reader:
            print(record.title())
