"""
Pork stores and retrieves text snippets from the command line.

Usage:
    pork
    pork KEY
    pork KEY VALUE
    pork (-d | --delete) KEY
    pork (-h | --help)
    pork (-v | --version)

Options:
    -h --help       Outputs usage information
    -v --version    Outputs the current version of Pork
    -d --delete     Deletes the specified key
"""

from docopt import docopt
import sys
import os

# For testing pork locally by running `python pork/cli.py`, add the project to
# sys.path so Python can find the pork module.
if __name__ == '__main__':
    package_path = os.path.abspath(os.path.join(__file__, '..', '..'))
    sys.path.insert(0, package_path)

import pork
from pork.data import Data

class CLI:
    def __init__(self):
        self.data = Data()

    def start(self, argv=None):
        args = docopt(__doc__, argv=argv, version=pork.__version__)
        self._process(args['KEY'], args['VALUE'], args['--delete'])

    def _process(self, key, value, delete):
        if key and delete:
            self.data.delete(key)
        elif key and value:
            self.data.set(key, value)
        elif key:
            v = self.data.get(key)
            if v is not None:
                print v
        elif self.data.is_empty():
            print __doc__.strip()
        else:
            items = self.data.list()
            padding = len(max(items, key=len))
            for k, v in self.data.list().iteritems():
                print "%s: %s" % (k.rjust(padding), v)

def main():
    CLI().start()

if __name__ == '__main__':
    main()
